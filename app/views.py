from app import app
from flask import render_template
from random import randint

@app.route('/')
def lucky_static():
    #template name comes before template variables
    return render_template('simple.html',
        lucky_num=randint(1, 100))
