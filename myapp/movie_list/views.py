from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db 
from myapp.models import MovieList
from myapp.movie_list.forms import MovieListForm

movie_list = Blueprint('movie_list', __name__)

@movie_list.route('/create', methods=['GET', 'POST'])
@login_required
def create_movie():
    form = MovieListForm()
    if form.validate_on_submit():
        movie = MovieList(title=form.title.data, genre=form.genre.data, user_id=current_user.id)
        db.session.add(movie)
        db.session.commit()
        flash('Movie Created')
        print('Movie was created')
        return redirect(url_for('core.index'))
    return render_template('create_movie.html', form=form)

@movie_list.route('/<int:movie_id>')
def movie(movie_id):
    movie = MovieList.query.get_or_404(movie_id) 
    return render_template('movie.html', title=movie.title, date=movie.date, item=movie)
