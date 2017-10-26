# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import request
from flask_babel import Babel
from flask_babel import gettext

app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    return str(request.accept_languages)

@app.route('/')
def hello_world():
    print(gettext('user_name_label'))
    return render_template('index.html',
                           user_name='ash84')
                           # user_name_label=gettext('user_name_label'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)