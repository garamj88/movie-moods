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
        movie = MovieList(title=form.title.data, genre=form.genre.data, mood=form.mood.data, director=form.director.data, release_year=form.release_year.data, user_id=current_user.id)
        db.session.add(movie)
        db.session.commit()
        flash('Movie Created')
        print('Movie was created')
        return redirect(url_for('core.index'))
    return render_template('create_movie.html', form=form)

@movie_list.route('/<int:movie_id>')
@login_required
def movie(movie_id):
    movie = MovieList.query.get_or_404(movie_id) 
    return render_template('movie.html', title=movie.title, date=movie.date, movie=movie)

@movie_list.route('/<int:movie_id>/update',methods=['GET','POST'])
@login_required
def update(movie_id):
    movie = MovieList.query.get_or_404(movie_id)

    if movie.author != current_user:
        abort(403)

    form = MovieListForm()

    if form.validate_on_submit():
        movie.title = form.title.data
        movie.genre = form.genre.data
        movie.mood = form.mood.data
        movie.director = form.director.data
        movie.release_year = form.release_year.data
        db.session.commit()
        flash('Movie Updated')
        return redirect(url_for('movie_list.movie',movie_id=movie.id))

    elif request.method == 'GET':
        form.title.data = movie.title
        form.genre.data = movie.genre
        form.mood.data = movie.mood
        form.director.data = movie.director
        form.release_year.data = movie.release_year

    return render_template('create_movie.html',title='Updating',form=form)

@movie_list.route('/<int:movie_id>/delete',methods=['GET','POST'])
@login_required
def delete_movie(movie_id):

    movie = MovieList.query.get_or_404(movie_id)
    if movie.author != current_user:
        abort(403)

    db.session.delete(movie)
    db.session.commit()
    flash('Movie Deleted')
    return redirect(url_for('core.index'))