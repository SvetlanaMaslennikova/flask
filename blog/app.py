from flask import Flask, render_template

from blog.user.views import user
from blog.report.views import report
from blog.article.views import article


# app = Flask(__name__)
#
#
# @app.route("/")
# def index():
#     return render_template("index.html")


def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprint(app)
    return app


def register_blueprint(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(report)
    app.register_blueprint(article)
