
from flask import *
from model.import_database import insert_upload_to_database, get_questions
from model.user import *
from model.export_vragen import *

app = Flask(__name__)
app.secret_key = "geheime_sleutel"

@app.route('/')
def home_page():
    return "<p>Home Page <br></p><p><a href="'/login_screen'">login</a><br> <a href="'/list_users'">list users</a></p> <br><p><a href="'/toetsvragenScherm'">toetsvragenScherm</a></p>"


@app.route('/list_users')
def list_user():
    if check_user_is_admin():
        user_model = User()
        all_users = user_model.get_users()
        return render_template("user_list.html", all_users = all_users)
    else:
        return "Niet ingelogd of geen admin"

@app.route('/toetsvragenScherm')
def toetsvragenScherm():
    if check_user_is_admin():
        user_model = User()
        all_users = user_model.get_users()
        return render_template("/toetsvragenScherm.html")
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
        if use_date is None:
            start_date = end_date = None
        return export_question_to_json(download_json, has_tax, start_date, end_date, mark_exported)
    return render_template('export_vragen.html')

@app.route('/export_vragen_json/<get>', methods=['POST','GET'])
def export_vragen_json(get):
    start_date = request.args.get("start_date", default="")
    end_date = request.args.get("end_date", default="")
    # print(request.args.get("start_date", default=""))

    if start_date != "" and end_date != "":
        print("date questions")
        return export_questions_date_range(get == "download", start_date, end_date)
    else:
        print("all questions")
        return export_all_questions(get == "download")

@app.route('/export_beoordeelde_vragen/<get>')
def export_beoordeelde_vragen(get):
    return export_question_with_prompt_id(get == "download")

if __name__ == "__main__":
    app.run(debug=True)