from turtledemo.penrose import start

from model.database import Database
from flask import jsonify

def export_question_to_json(save = False, has_tax = False, start_date = None, end_date = None):
    database = Database('./databases/database.db')
    cursor, conn = database.connect_db()

    select_query = "SELECT questions_id, prompts_id, user_id, question, taxonomy_bloom, rtti, exported, date_created FROM questions"
    if has_tax and start_date and end_date:
        select_query += " WHERE taxonomy_bloom IS NOT NULL OR rtti IS NOT NULL AND date_created BETWEEN ? AND ?"
        cursor.execute(select_query, (start_date, end_date))
    elif start_date and end_date:
        select_query += " WHERE date_created BETWEEN ? AND ?"
        cursor.execute(select_query, (start_date, end_date))
    elif has_tax:
        select_query += " WHERE taxonomy_bloom IS NOT NULL OR rtti IS NOT NULL"
        cursor.execute(select_query)
    else:
        cursor.execute(select_query)

    rows = cursor.fetchall()

    return create_json(rows, save)

def export_all_questions(save = False):
    database = Database('./databases/database.db')
    cursor, conn = database.connect_db()
    select_query = "SELECT questions_id, prompts_id, user_id, question, taxonomy_bloom, rtti, exported, date_created FROM questions"

    cursor.execute(select_query)
    rows = cursor.fetchall()

    return create_json(rows, save)

def export_question_with_prompt_id(save = False):
    database = Database('./databases/database.db')
    cursor, conn = database.connect_db()
    select_query = "SELECT questions_id, prompts_id, user_id, question, taxonomy_bloom, rtti, exported, date_created FROM questions WHERE taxonomy_bloom IS NOT NULL OR rtti IS NOT NULL; "

    cursor.execute(select_query)
    rows = cursor.fetchall()

    return create_json(rows, save)

def export_questions_date_range(save, start_date, end_date):
    database = Database('./databases/database.db')
    cursor, conn = database.connect_db()
    select_query = "SELECT questions_id, prompts_id, user_id, question, taxonomy_bloom, rtti, exported, date_created FROM questions WHERE date_created BETWEEN start_date AND end_date"

    cursor.execute(select_query)
    rows = cursor.fetchall()

    return create_json(rows, save)

def create_json(rows, save = False):
    data = []
    for row in rows:
        dictionary = {}
        dictionary['questions_id'] = row['questions_id']
        dictionary['prompts_id'] = row['prompts_id']
        dictionary['question'] = row['question']
        dictionary['taxonomy_bloom'] = row['taxonomy_bloom']
        dictionary['rtti'] = row['rtti']
        dictionary['exported'] = row['exported']
        dictionary['date_created'] = row['date_created']
        data.append(dictionary)

    response = jsonify(data)

    if save:
        response.headers["Content-Disposition"] = "attachment; filename=questions.json"
        response.headers["Content-Type"] = "application/json"

    return response