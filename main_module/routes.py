from main_module import main_app
from flask import render_template


@main_app.route('/')
@main_app.route('/index')
def index():
    return render_template('index.html', title='Mops')


@main_app.route('/team')
def team():
    return None


@main_app.route('/podcasts')
def podcasts():
    return None


@main_app.route('/news')
def news():
    return None
