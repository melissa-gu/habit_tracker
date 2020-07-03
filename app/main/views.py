from flask import Blueprint, render_template, redirect

from app.models import EditableHTML

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return redirect('/daily')

@main.route('/daily')
def daily():
    editable_html_obj = EditableHTML.get_editable_html('daily')
    return render_template(
        'main/daily.html', editable_html_obj=editable_html_obj)

@main.route('/monthly')
def monthly():
    editable_html_obj = EditableHTML.get_editable_html('monthly')
    return render_template(
        'main/monthly.html', editable_html_obj=editable_html_obj)

@main.route('/habits')
def habits():
    editable_html_obj = EditableHTML.get_editable_html('habits')
    return render_template(
        'main/habits.html', editable_html_obj=editable_html_obj)
