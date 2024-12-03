from model.database import Database

def insert_upload_to_database(data):

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
