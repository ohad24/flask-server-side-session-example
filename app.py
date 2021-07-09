import os

os.environ["FLASK_ENV"] = "development"
from flask import Flask, request, render_template, redirect, sessions, url_for, session
from flask_login import (
    LoginManager,
    current_user,
    UserMixin,
    login_user,
    login_required,
    logout_user,
)
from flask_socketio import SocketIO
from flask_session import Session
from datetime import timedelta
from time import time

app = Flask(__name__)
app.secret_key = "1234"  # os.environ['SECRET_KEY']
login_manager = LoginManager()
login_manager.init_app(app)
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
socketio = SocketIO(app, manage_session=False)

db = {1: {"user_id": 1, "name": "ohad"}, 2: {"user_id": 2, "name": "nico"}}


class User(UserMixin):
    def __init__(self, user_id: int):
        self.id = int(user_id)
        self.user_id = self.id
        self.name = db.get(self.user_id).get("name")


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


@app.before_request
def make_session_permanent():
    session["t"] = time()
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)


@app.route("/")
def index():
    print(f"session_sid: {session.sid}")
    print(f"session: {session}")
    return render_template("index.html")


@app.route("/protected")
@login_required
def protected():
    # print(f'cur user: {current_user.is_authenticated}')
    return render_template("protected.html")


@app.route("/login")
def login():
    user_id = request.args.get("user_id", int)
    user = User(user_id)
    login_user(user)
    return redirect(url_for("index"))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


if "__main__" == __name__:
    app.run(debug=True)
