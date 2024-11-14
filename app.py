from flask import Flask, render_template, session

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

@app.route('/edit_user')
def edit_user():
    if check_user_is_admin():
        user_model = User()
        all_users = user_model.get_users()
        return render_template("edit_user.html", sin = all_users)
    else:
        return "Niet ingelogd of geen admin"

def check_user_is_admin():
    session['logged_user'] = {'name': 'test', 'admin': 1}  # test

    if 'logged_user' not in session:
        return False
    elif session['logged_user']['admin'] == 0:
        return False

    return True

if __name__ == "__main__":
    app.run(debug=True)