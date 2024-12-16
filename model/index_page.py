import json

from flask import render_template

from lib.gpt.bloom_taxonomy import gpt_model_map
from model.import_database import get_question

def index_question(question_id):
    question =  get_question(question_id)

    return render_template('index_page.html', question=question, models=gpt_model_map)