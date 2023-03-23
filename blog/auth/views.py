from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import logout_user, login_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash

from blog.extensions import db
from blog.forms.user import UserRegisterForm
from blog.models import User

auth = Blueprint('auth', __name__, static_folder='../static')


@auth.route('/login', methods=('POST', 'GET',))
def login():
    if request.method == 'GET':
        if current_user.is_authenticated:
            return redirect(url_for('user.profile', pk=current_user.id))

        form = UserRegisterForm(request.form)
        errors = []
        if request.method == 'POST' and form.validate_on_submit():
            if User.query.filter_by(email=form.email.data).count():
                form.email.errors.append('email not uniq')
                return render_template('users/register.html', form=form)

            _user = User(
                email=form.email.data,
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                password=generate_password_hash(form.password.data),
            )

            db.session.add(_user)
            db.session.commit()

            login_user(_user)


        return render_template(
            'auth/login.html',
            form=form,
            errors=errors,
        )

    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Check your login details')
        return redirect(url_for('.login'))

    login_user(user)
    return redirect(url_for('user.profile', pk=user.id))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))
