from flask import Blueprint, render_template, redirect

article = Blueprint('article', __name__, url_prefix='/articles', static_folder='../static')

ARTICLES = {
    1: 'Article 1',
    2: 'Article 2',
    3: 'Article 3',
}


@article.route('/')
def article_list():
    return render_template(
        'articles/list.html',
        articles=ARTICLES,
    )


@article.route('/<int:pk>')
def get_article(pk: int):
    try:
        article_name = ARTICLES[pk]
    except KeyError:
        return redirect('/articles')
    return render_template(
        'articles/details.html',
        article_name=article_name,
    )
