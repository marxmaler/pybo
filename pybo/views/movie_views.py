from flask import Blueprint, render_template, request
from pybo.movieapi import collect_movie_data
from ..forms import NaverMovieForm
from ..naverapi import navermovie
bp = Blueprint('movie', __name__, url_prefix='/movie')

@bp.route('/rank', methods=('GET',))
def movie_rank():
    rankdata = collect_movie_data()
    return render_template('movie/movie_rank.html', rankdata=rankdata)

@bp.route('/search', methods=('GET','POST'))
def movie_search():
    form = NaverMovieForm()

    if request.method == "POST" and form.validate_on_submit():
        result = navermovie(form.search.data)
        # print(result)
        return render_template('movie/movie_search.html', movieinfo_list=result['items'], form=form) #포스트 방식일 때(검색한 후)

    return render_template('movie/movie_search.html', form=form) #겟 방식일 때(검색하기 전)

