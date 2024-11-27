from model.database import Database

def export_alle_vragen():
    database = Database('./databases/database.db')
    cursor, conn = database.connect_db()
    select_query = "SELECT questions_id, prompts_id, user_id, question, date_created FROM questions"

    cursor.execute(select_query)
    rows = cursor.fetchall()
    for row in rows:
        print(row['question'])