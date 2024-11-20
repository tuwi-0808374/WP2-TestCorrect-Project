from model.database import Database

database = Database('./databases/database.db')
cursor, conn = database.connect_db()

def insert_upload_to_database(data):
    
    """
    Inserts multiple records into the `questions` table.

    :param data: A list of dictionaries where each dictionary represents a row to be inserted.
    """
    insert_query = """
        INSERT INTO questions (
            questions_id,
            prompts_id,
            user_id,
            question,
            taxonomy_bloom,
            rtti,
            exported,
            date_created
        ) VALUES (?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
    """
    
    try:
        for item in data:
            print(item)
            questions_id = item.get("questions_id")
            prompts_id = item.get("prompts_id")
            user_id = item.get("user_id")
            question = item.get("question")
            taxonomy_bloom = item.get("taxonomy_bloom", None)
            rtti = item.get("rtti", None) 
            exported = item.get("exported", False)

            cursor.execute(insert_query, (
                questions_id,
                prompts_id,
                user_id,
                question,
                taxonomy_bloom,
                rtti,
                exported
            ))
        
        conn.commit()
        print("Data inserted successfully.")

    except IntegrityError as e:
        print(f"Integrity error occurred: {e}")
        conn.rollback()  # Rollback in case of error

    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()  # Rollback in case of error