from flask import Blueprint, render_template, redirect, request

from flask_login import current_user

from app.models import EditableHTML
from app.main.forms import HabitForm
from app.models import Habit

from app import db, csrf

main = Blueprint('main', __name__)


@main.route('/')
def index():
    if current_user.is_authenticated:
        return redirect('/daily')
    else:
        editable_html_obj = EditableHTML.get_editable_html('index')
        return render_template(
            'main/index.html', editable_html_obj=editable_html_obj)
    

@csrf.exempt
@main.route('/daily', methods=['GET', 'POST'])
def daily():
    editable_html_obj = EditableHTML.get_editable_html('daily') 
    
    if request.method == 'POST':
        data = request.get_json()
        id = int(data['id'])
        habit = Habit.query.get(id)
        habit.complete = data['complete']
        db.session.commit()
    habits = current_user.habits
    return render_template(
        'main/daily.html', editable_html_obj=editable_html_obj, habits=habits)

@main.route('/monthly')
def monthly():
    editable_html_obj = EditableHTML.get_editable_html('monthly')
    return render_template(
        'main/monthly.html', editable_html_obj=editable_html_obj)

@main.route('/habits')
def habits():
    editable_html_obj = EditableHTML.get_editable_html('habits')
    habits = current_user.habits
    return render_template(
        'main/habits.html', editable_html_obj=editable_html_obj, habits=habits)

@main.route('/add-habit', methods=['GET', 'POST'])
def add_habit():
    form = HabitForm()
    
    if form.validate_on_submit():
        habit = Habit(description=form.description.data, complete=form.complete.data, parent_id=current_user.id)
        db.session.add(habit)
        db.session.commit()
        return redirect('/habits')
    return render_template('main/add_habit.html', form=form)