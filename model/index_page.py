import json

from flask import *

from lib.gpt.bloom_taxonomy import gpt_model_map, get_taxonomy
from model.database_model import get_question, set_taxonomy


def display_question(question_id):
    question =  get_question(question_id)
    if question["taxonomy_bloom"]:
        question["taxonomy_bloom"] = json.loads(question["taxonomy_bloom"])

    return render_template('index_page.html', question=question, models=gpt_model_map)

def update_taxonomy(question_id):
    question = get_question(question_id)

    taxonomy = get_taxonomy(question["question"], False, "rac_test")

    set_taxonomy(question_id, False, taxonomy)

    return redirect(url_for('index_page', question_id=question_id))

