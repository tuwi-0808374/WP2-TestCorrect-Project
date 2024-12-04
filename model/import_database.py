from flask import jsonify

from model.database import Database

required_keys = [
    "question_id",
    "question",
    "answer",
    "vak",
    "onderwijsniveau",
    "leerjaar",
    "question_index"
]

def insert_upload_to_database(data):
        errors = []
        filtered_data = []

        for index, item in enumerate(data):
            missing_or_invalid = []

            for key in required_keys:
                if key not in item or item[key] in [None, ""]:
                    missing_or_invalid.append(key)

            if missing_or_invalid:
                errors.append({
                    "item_index": index,
                    "error": 'Invalid keys in json item: ' + ', '.join(missing_or_invalid)
                })
                continue

            questions = get_questions()
            duplicate = False

            if item['question_id'] in questions:
                errors.append({
                    "item_index": index,
                    "error": 'Question already exists ' + str(id)
                })
                duplicate = True

            if not duplicate:
                filtered_data.append(item)

        if not errors:
            database = Database('./databases/database.db')
            cursor, conn = database.connect_db()

            insert_query = "INSERT INTO questions (questions_id, prompts_id, user_id, question, date_created) VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)"

            for item in data:
                questions_id = item.get("question_id")
                prompts_id = 0
                user_id = '1234'  # PLACEHOLDER EXAMPLE
                question = item.get("question")

                cursor.execute(insert_query, (
                    questions_id,
                    prompts_id,
                    user_id,
                    question
                ))

            conn.commit()
            conn.close()

            return jsonify({'error': False, 'message': 'Data successfully uploaded!'})
        else:
            # Add function to fix missing keys to questions

            return jsonify({
                'error': True,
                'message': 'JSON file error',
                'details': errors
            }), 400

def get_questions():
    database = Database('./databases/database.db')
    cursor, conn = database.connect_db()

    questions = cursor.execute("SELECT questions_id FROM questions")

    question_ids = []

    for question in questions:
        question_id = question[0]
        question_ids.append(question_id)

    conn.commit()
    conn.close()

    return question_ids
