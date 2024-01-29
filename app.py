from flask import Flask
import people_also_ask
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
@cross_origin()
def home():
    return 'Hello World!'


@app.route('/getPaa/<a>')
@cross_origin()
def get_paa(a):
    faqData = []
    questions = people_also_ask.get_related_questions(a)
    for question in questions:
        answer = people_also_ask.get_simple_answer(question)
        faqData.append({
            "question": question,
            "answer": answer
        })
    return faqData
