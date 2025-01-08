from model.database import Database
from datetime import datetime
from flask import jsonify

def prompt_overview():
    database = Database('./databases/database.db')
    cursor, conn = database.connect_db()
    prompt_overview_query = "SELECT prompts.prompts_id, prompts.prompt, users.display_name as Redacteur, prompts.questions_count, prompts.questions_correct FROM prompts JOIN users ON users.user_id = prompts.user_id; "
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

    # cursor.execute(insert_prompt,(?,?,?,?,?,today_date))

def delete_prompt(prompts_id):
    print(prompts_id)
    database = Database('./databases/database.db')
    cursor, conn = database.connect_db()
    cursor.execute("DELETE FROM prompts WHERE prompts_id = ?", (str(prompts_id),))
    conn.commit()