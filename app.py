from flask import Flask, render_template

from lib.model.User import *

app = Flask(__name__)

@app.route('/')
def home_page():
    return "<p>Home Page</p><p><a href="'/list_users'">list users</a></p>"

@app.route('/list_users')
def list_user():
    user_model = User()
    all_users = user_model.get_users()
    return render_template("user_list.html", all_users = all_users)

if __name__ == "__main__":
    app.run(debug=True)