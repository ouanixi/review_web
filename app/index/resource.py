from flask import render_template, request
import requests

from app.index import ind


REVIEW = {'review': 'I was using this app fir the first time tonight to buy a ticket from lima to cusco and evreytime time after I accept the payment it got me out of the payment and back to the app so I was sure their is a problem but then I went to star peru website and I can see that I have five resevation under my name. I cant do nothing about it now I just hope that I wont pay for all of them', 'intent': {'i was using this app fir the first time tonight to buy a ticket from lima to cusco and evreytime time after i accept the payment it got me out of the payment and back to the app': 'Information Giving', 'so i was sure their is a problem but then i went to star peru website and i can see that i have five resevation under my name.': 'Problem Discovery', 'i cant do nothing about it now i just hope that i wont pay for all of them': 'Information Giving'}, 'sentences': {'i was using this app fir the first time tonight to buy a ticket from lima to cusco and evreytime time after i accept the payment it got me out of the payment and back to the app': 'Informative', 'so i was sure their is a problem but then i went to star peru website and i can see that i have five resevation under my name.': 'Informative', 'i cant do nothing about it now i just hope that i wont pay for all of them': 'Informative'}, 'rating': '5', 'sentiment': '-1', 'id': '0'}

intent_map = {"0": "Problem Discovery",
              "1": "Feature Request",
              "2": "Information Seeking",
              "3": "Information Giving"}

inf_map = {"1": "Informative",
           "-1": "Non Informative"}


@ind.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@ind.route('summarise', methods=['GET', 'POST'])
def summary():
    url = "http://localhost/api/predict"
    review = request.form['text']
    data = [{"id": "0", "review": review, "rating": '5'}]
    response = requests.post(url, json=data)
    data = response.json()[0]
    data = parse_response(data)
    return render_template('review.html', review=data.get('review')
                                        , sentences=data.get('sentences')
                                        , intent=data.get('intent')
                                        , sentiment=data.get('sentiment'))


def parse_response(response_json):
    if response_json['sentences']:
        for key in response_json['sentences']:
            value = response_json['sentences'].get(key)
            response_json['sentences'][key] = inf_map[value]
    for key in response_json['intent']:
        value = response_json['intent'].get(key)
        response_json['intent'][key] = intent_map[value]
    return response_json
