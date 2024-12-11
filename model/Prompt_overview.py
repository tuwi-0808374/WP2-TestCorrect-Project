from model.database import Database
from flask import jsonify

def prompt_overview():
    database = Database('./databases/database.db')
    cursor, conn = database.connect_db()
    prompt_overview_query = "SELECT prompts.prompt, users.display_name as Redacteur, prompts.questions_count, prompts.questions_correct FROM prompts JOIN users ON users.user_id = prompts.user_id; "
    cursor.execute(prompt_overview_query)
    data = cursor.fetchall()


def insert_prompt():
    database = Database('./databases/database.db')
    cursor, conn = database.connect_db()
    insert_prompt("")