from flask import Blueprint, render_template,redirect,url_for,request ,flash
from flask_login import login_user,logout_user,login_required,current_user

from .model import User,Workout
from . import db
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html',name = current_user.name)

# This is GET Request Handler
@main.route('/new')
@login_required
def new_workout():
    return render_template('create_workout.html')


# This is POST Request Handler
@main.route('/new',methods=['POST'])
@login_required
def new_workout_post():
    pushups = request.form.get('pushups')
    comment = request.form.get('comment')
    workout  = Workout(pushups=pushups, comment=comment, author = current_user)
    db.session.add(workout)
    db.session.commit()

    flash("your workout has been added")

    return redirect(url_for('main.user_workouts'))

@main.route('/all')
@login_required
def user_workouts():
    page = request.args.get('page',1,type=int)
    user = User.query.filter_by(name = current_user.name).first_or_404()
    workouts = Workout.query.filter_by(author=user).paginate(page = page,per_page = 3)
    return render_template('all_workouts.html', workouts = workouts,user=user)

@main.route('/workout/<int:id>/update', methods = ['GET','POST'])
@login_required 
def Edit_workouts(id):
    workout = Workout.query.get_or_404(id)
    if request.method == 'POST':
        workout.pushups = request.form.get('pushups',workout.pushups)
        workout.comment = request.form.get('comment',workout.comment)
        db.session.commit()
        flash("your workout has been updated!!!")
        return redirect(url_for('main.user_workouts'))
    
    return render_template('edit_workouts.html',workout=workout)

@main.route('/workout/<int:id>/delete', methods = ['GET','POST'])
@login_required 
def delete_workout(id):
     workout = Workout.query.get_or_404(id)
     db.session.delete(workout)
     db.session.commit()
     flash("your workout has been deleted")
     return redirect(url_for('main.user_workouts'))