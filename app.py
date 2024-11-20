from selectors import SelectSelector

from flask import *

from model.import_database import insert_upload_to_database
from model.user import *

app = Flask(__name__)
app.secret_key = "geheime_sleutel"

@app.route('/')
def home_page():
    return "<p>Home Page <br></p><p><a href="'/list_users'">list users</a></p>"

@app.route('/list_users')
def list_user():
    if check_user_is_admin():
        user_model = User()
        all_users = user_model.get_users()
        return render_template("user_list.html", all_users = all_users)
    else:
        return "Niet ingelogd of geen admin"

@app.route('/login_screen', methods=['GET', 'POST'])
def login_screen():
    if request.method == "GET":
        login = request.form['login']
        password = request.form['password']
        return render_template("login_screen.html", get_login = login, password = password )
    else:
        return "Niet ingelogd onjuist login of wachtwoord "


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

required_keys = [
    "question_id",
    "question",
    "answer",
    "vak",
    "onderwijsniveau",
    "leerjaar",
    "question_index"
]

@app.route('/import')
def import_page():
   return render_template('import_screen.html')

@app.route('/import', methods=['POST'])
def import_json():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    try:
        json_data = json.load(file)

        errors = []
    
        for index, item in enumerate(json_data):
            missing_or_invalid = []
            
            for key in required_keys:

                if key not in item or item[key] in [None, ""]:
                    missing_or_invalid.append(key)
            
            if missing_or_invalid:
                errors.append({
                    "item_index": index,
                    "missing_or_invalid_keys": missing_or_invalid
                })

        if errors is not []:
            return jsonify({'error': True, 'JSON File heeft missende keys': errors})
        else:
            insert_upload_to_database(json_data)
            return jsonify({'error': True, 'Test?': errors})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    

def check_user_is_admin():
    session['logged_user'] = {'name': 'test', 'admin': 1}  # test

    if 'logged_user' not in session:
        return False
    elif session['logged_user']['admin'] == 0:
        return False

    return True

if __name__ == "__main__":
    app.run(debug=True)