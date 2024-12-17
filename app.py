
from flask import *

from lib.gpt.bloom_taxonomy import get_taxonomy
from model.database_model import insert_upload_to_database
from model.toetsvragen import Toetsvragen

from model.database_model import insert_upload_to_database
from model.index_page import display_question, update_taxonomy

from model.user import *
from model.export_vragen import *
from model.Prompt_overview import *

app = Flask(__name__)
app.secret_key = "geheime_sleutel"

@app.route('/')
def home_page():
    return "<p>Home Page <br></p><p><a href="'/login_screen'">login</a><br> <a href="'/list_users'">list users</a><br><a href="'/export_vragen'">Export vragen</a><br> <a href="'/prompt_overview'">prompt overview</a></p> <br><p><a href="'/toetsvragenScherm'">toetsvragenScherm</a></p>"


@app.route('/list_users')
def list_user():
    if check_user_is_admin():
        user_model = User()
        all_users = user_model.get_users()
        return render_template("user_list.html", all_users = all_users)
    else:
        return "Niet ingelogd of geen admin"


@app.route('/toetsvragenScherm', methods=['GET'])
def toetsvragenScherm():
    if check_user_is_admin():
        page = int(request.args.get('page', 1))
        zoekwoord = request.args.get('zoekWoord', '')
        taxonomy_filter = request.args.get('taxonomy') == 'true'
        limit = 10
        start = (page - 1) * limit

        toetsvragen_model = Toetsvragen()

        if taxonomy_filter:
            query = 'SELECT * FROM questions WHERE taxonomy_bloom IS NOT NULL LIMIT ? OFFSET ?'
            all_questions = toetsvragen_model.cursor.execute(query, (limit, start)).fetchall()
            total_questions_query = 'SELECT COUNT(*) FROM questions WHERE taxonomy_bloom IS NOT NULL'
            total_questions = toetsvragen_model.cursor.execute(total_questions_query).fetchone()[0]
        else:
            all_questions = toetsvragen_model.getToetsvragen(start=start, limit=limit, search=zoekwoord)
            total_questions = toetsvragen_model.getTotalQuestions(search=zoekwoord)

        has_previous = start > 0
        has_next = start + limit < total_questions

        return render_template(
            "toetsvragenScherm.html",
            all_questions=all_questions,
            page=page,
            has_previous=has_previous,
            has_next=has_next,
            zoekwoord=zoekwoord,
            taxonomy_filter=taxonomy_filter
        )
    else:
        return "Niet ingelogd of geen admin"

@app.route('/login_screen', methods=['GET', 'POST'])
def login_screen():

    if request.method == "POST":
        #Get login from form
        login = request.form['login']
        password = request.form["password"]
        print(login, password)

        #basic validation
        if not login or not password:
            return "Login or password missing. Please fill in all fields."

        #placeholder
        if login == "admin" and password == "admin":
            return render_template ( "user_list.html",user=login)
        else:
            return "Incorrect login or password, please try again."

    return render_template("login_screen.html")


@app.route('/edit_user/<user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    if check_user_is_admin():
        user_model = User()
        if request.method == 'POST':
            display_name = request.form['display_name']
            login = request.form['login']
            password = request.form['password']
            is_admin = request.form['is_admin']

            update_user_status = user_model.update_user(user_id, login, password, display_name, is_admin)
            if update_user_status:
                return redirect(url_for('list_user'))
        else:
            user = user_model.get_user(user_id)
            return render_template("edit_user.html", user = user)
    else:
        return "Niet ingelogd of geen admin"

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if check_user_is_admin():
        user_model = User()
        if request.method == 'POST':
            display_name = request.form['display_name']
            login = request.form['login']
            password = request.form['password']
            is_admin = request.form['is_admin']

            create_user_status = user_model.create_user(login, password, display_name, is_admin)
            if create_user_status:
                return redirect(url_for('list_user'))
        else:
            return render_template("add_user.html")
    else:
        return "Niet ingelogd of geen admin"

@app.route('/delete_user/<user_id>')
def delete_user(user_id):
    if check_user_is_admin():
        user_model = User()
        user_model.delete_user(user_id)
        return redirect(url_for('list_user'))
    else:
        return "Niet ingelogd of geen admin"

@app.route('/add_test_user')
def add_test_user():
    if check_user_is_admin():
        user_model = User()
        user_model.create_user("naam test1245", "pass", "display1345", "1")
        return redirect(url_for('list_user'))
    else:
        return "Niet ingelogd of geen admin"

# Import page & functions

@app.route('/import')
def import_page():
   return render_template('import_screen.html')

@app.route('/import', methods=['POST'])
def import_json():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    json_file = request.files['file']

    if json_file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    json_data = json.load(json_file)

    return insert_upload_to_database(json_data)

@app.route('/index/<question_id>')
def index_page(question_id):
    return display_question(question_id)

@app.route('/update_taxonomy', methods=['POST'])
def call_update_taxonomy():
    question_id = request.form.get('question_id')
    prompt  = request.form.get('prompt')
    prompt = clean_prompt(prompt)
    
    return update_taxonomy(question_id, prompt)

def clean_prompt(prompt_with_error_margin):
    return prompt_with_error_margin.split(" - ", 1)[-1]

def check_user_is_admin():
    session['logged_user'] = {'name': 'test', 'admin': 1}  # test

    if 'logged_user' not in session:
        return False
    elif session['logged_user']['admin'] == 0:
        return False

    return True

@app.route('/export_vragen', methods=['POST','GET'])
def export_vragen():
    if request.method == 'POST':
        print(request.form.to_dict())
        download_json = request.form['export_option'] == "1"
        has_tax = request.form.get('has_tax')
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')
        use_date = request.form.get('between_date')
        mark_exported = request.form.get('exported')
        export_status_type = int(request.form.get('export_status_type'))
        limit = int(request.form.get('limit'))
        if use_date is None:
            start_date = end_date = None
        return export_question_to_json(download_json, has_tax, start_date, end_date, mark_exported, export_status_type, limit)
    return render_template('export_vragen.html')

@app.route('/prompt_overview', methods=['GET', 'POST'])
def prompt_tabel():
    prompts = prompt_overview()

    if request.method == 'POST':
        return render_template("add_prompt.html")

    prompt_overview_data = {
        "prompt": prompt_overview(prompts.prompt),
        "redacteur": prompt_overview(redacteur),
        "toetsvragen": prompt_overview(prompts.question_count),
        "correct": prompt_overview(prompts.questions_correct),
    }
    return render_template("prompt_tabel.html", data=prompt_overview_data)

@app.route('/prompt_input', methods=['GET', 'POST'])
def prompt_input():
    prompt_title = request.form['prompt-title']
    prompt = request.form['prompt']

if __name__ == "__main__":
    app.run(debug=True)