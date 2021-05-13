from flask import Blueprint, render_template, request

from pybo.naverapi import naverbook
from ..forms import NaverBookForm

bp = Blueprint('naver', __name__, url_prefix='/naver')

@bp.route('/book', methods=('GET','POST'))
def book():
    form = NaverBookForm()

    if request.method == "POST" and form.validate_on_submit():
        result = naverbook(form.search.data)
        return render_template('naver/naverbook.html', bookinfo_list=result['items'], form=form) #포스트 방식일 때(검색한 후)

    return render_template('naver/naverbook.html', form=form) #겟 방식일 때(검색하기 전)