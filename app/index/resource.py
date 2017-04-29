"""Controller module handling requests."""
from flask import render_template, request
import requests

from app.index import ind


intent_map = {"0": "Problem Discovery",
              "1": "Feature Request",
              "2": "Information Seeking",
              "3": "Information Giving"}

inf_map = {"1": "Informative",
           "-1": "Non Informative"}


@ind.route('/', methods=['GET', 'POST'])
def _index():
    return render_template('index.html')


@ind.route('summarise', methods=['GET', 'POST'])
def _summary():
    url = "http://172.18.0.1/api/predict"
    review = request.form['text']
    data = [{"id": "0", "review": review, "rating": '5'}]
    response = requests.post(url, json=data)
    data = response.json()[0]
    data = _parse_response(data)
    return render_template('review.html', review=data.get('review'),
                           sentences=data.get('sentences'),
                           intent=data.get('intent'), sentiment=data.get('sentiment'),
                           topics=data.get('topics'))


def _parse_response(response_json):
    if response_json['sentences']:
        for key in response_json['sentences']:
            value = response_json['sentences'].get(key)
            response_json['sentences'][key] = inf_map[value]
    for key in response_json['intent']:
        value = response_json['intent'].get(key)
        response_json['intent'][key] = intent_map[value]
    return response_json
