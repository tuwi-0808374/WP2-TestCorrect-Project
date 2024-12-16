import json

from model.import_database import get_question

def index_question(question_id):
    question =  get_question(question_id)
    print(json.dumps(question, indent=4, ensure_ascii=False))