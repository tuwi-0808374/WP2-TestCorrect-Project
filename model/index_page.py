import json

from flask import *

from lib.gpt.bloom_taxonomy import gpt_model_map, get_taxonomy
from model.database_model import *


def display_question(question_id):
    question =  get_question(question_id)
    if question["taxonomy_bloom"]:
        question["taxonomy_bloom"] = json.loads(question["taxonomy_bloom"])

    prompts = get_prompts()

    for prompt in prompts:
        prompt["error_margin"] = int((prompt["questions_correct"] / prompt["questions_count"]) * 100)

    return render_template('index_page.html', question=question, models=gpt_model_map, prompts=prompts)

def update_taxonomy(question_id):
    question = get_question(question_id)

    taxonomy = get_taxonomy(question["question"], False, "rac_test")

    set_taxonomy(question_id, False, taxonomy)

    return redirect(url_for('index_page', question_id=question_id))

