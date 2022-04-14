from flask import render_template, request, Blueprint
from myapp.models import MovieList

core = Blueprint('core', __name__)

@core.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    movie_list = MovieList.query.order_by(MovieList.genre.asc()).paginate(page=page, per_page=5)
    return render_template('index.html', movie_list=movie_list)