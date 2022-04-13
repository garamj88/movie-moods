from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db 
from myapp.models import MovieList
from myapp.movie_list.forms import MovieListForm

movie_list = Blueprint('movie_list', __name__)