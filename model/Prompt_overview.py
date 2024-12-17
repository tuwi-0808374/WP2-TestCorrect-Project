from model.database import Database
from datetime import datetime
from flask import jsonify

def prompt_overview():
    database = Database('./databases/database.db')
    cursor, conn = database.connect_db()
    prompt_overview_query = "SELECT prompts.prompt, users.display_name as Redacteur, prompts.questions_count, prompts.questions_correct FROM prompts JOIN users ON users.user_id = prompts.user_id; "
    cursor.execute(prompt_overview_query)
    data = cursor.fetchall()
    return data


def insert_prompt():
    database = Database('./databases/database.db')
    cursor, conn = database.connect_db()
    #to get the date
    today_date = datetime.today().strftime('%Y-%m-%d')

    #query
    insert_prompt("INSERT INTO prompts (prompts_id, user_id, prompt, qeustion_count, questions_correct, date_created) VALUES (?,?,?,?,?,?) ")

    cursor.execute(insert_prompt,(?,?,?,?,?,today_date))

