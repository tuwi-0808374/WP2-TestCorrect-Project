import json

from flask import *

from lib.gpt.bloom_taxonomy import gpt_model_map, get_taxonomy
from model.import_database import get_question

def display_question(question_id):
    question =  get_question(question_id)

    return render_template('index_page.html', question=question, models=gpt_model_map)

def update_taxonomy(question_id):
    data = request.json

    updated_question = get_question(question_id)

    return jsonify({
        "taxonomy_bloom": updated_question.get("taxonomy_bloom", {}),
        "rtti": updated_question.get("rtti", "")
    })