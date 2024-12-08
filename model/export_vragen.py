from model.database import Database
from flask import jsonify

def export_all_questions(save = False):
    database = Database('./databases/database.db')
    cursor, conn = database.connect_db()
    select_query = "SELECT questions_id, prompts_id, user_id, question, taxonomy_bloom, rtti, exported, date_created FROM questions"

    cursor.execute(select_query)
    rows = cursor.fetchall()

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

def export_question_with_prompt_id(save = False):
    database = Database('./databases/database.db')
    cursor, conn = database.connect_db()
    select_query = "SELECT questions_id, prompts_id, user_id, question, taxonomy_bloom, rtti, exported, date_created FROM questions WHERE prompts_id > 0 "

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
