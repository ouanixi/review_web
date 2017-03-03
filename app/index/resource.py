from flask import render_template

from app.index import index


@index.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
