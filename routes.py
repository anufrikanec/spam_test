from flask import Flask, request, jsonify
from application import app
from spam_classifer import calc_spam
spam_class = calc_spam()

@app.route('/hello_user', methods=['POST'])
def hello_user():
    data = request.json
    user = data['user']
    number = data['num']
    number = int(number)+1
    return f'{number}'

@app.route('/hello')
def hello():

    return f'Привет!'

@app.route('/classify_text', methods=['POST'])
def classify_text():
    data = request.json
    text = data['text']

    result = spam_class.classify(text)
    return jsonify({'result': result})
