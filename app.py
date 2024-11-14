from flask import Flask, render_template, session

from lib.model.user import *

app = Flask(__name__)
app.secret_key = "geheime_sleutel"

@app.route('/')
def home_page():
    session['logged_user'] = {'name': 'test', 'admin': 1}
    return "<p>Home Page <br></p><p><a href="'/list_users'">list users</a></p>"

@app.route('/list_users')
def list_user():
    if 'logged_user' not in session:
        return "<p>U bent niet ingelogt</p>"

    elif session['logged_user']['admin'] == 0:
        return "<p>U bent wel ingelogd, maar heeft niet de juiste rechten</p>"

    else:
        user_model = User()
        all_users = user_model.get_users()
        return render_template("user_list.html", all_users = all_users)

if __name__ == "__main__":
    app.run(debug=True)