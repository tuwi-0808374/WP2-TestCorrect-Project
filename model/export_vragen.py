from model.database import Database
from flask import jsonify

def export_alle_vragen(save):
    database = Database('./databases/database.db')
    cursor, conn = database.connect_db()
    select_query = "SELECT questions_id, prompts_id, user_id, question, taxonomy_bloom, rtti, date_created FROM questions"

    cursor.execute(select_query)
    rows = cursor.fetchall()

    data = []
    for row in rows:
        dictionary = {}
        dictionary['questions_id'] = row['questions_id']
        dictionary['question'] = row['question']
        dictionary['taxonomy_bloom'] = row['taxonomy_bloom']
        dictionary['rtti'] = row['rtti']
        data.append(dictionary)

    response = jsonify(data)

    if save:
        response.headers["Content-Disposition"] = "attachment; filename=questions.json"
        response.headers["Content-Type"] = "application/json"

    return response


