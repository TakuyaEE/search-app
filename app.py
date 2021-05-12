from flask import Flask, render_template, request, redirect, url_for, Blueprint, abort, jsonify, session
from flask_sqlalchemy import SQLAlchemy
import pyrebase
import os
import json

from app_inquiry import inquiry
from app_search_hellowork import search_hellowork
# from app_search_shigotonavi import search_shigotonavi

# firebaseConfigの読み込み
with open("firebaseConfig.json") as f:
    firebaseConfig = json.loads(f.read())
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

app = Flask(__name__)

# 別モジュールをblueprintで呼び出し
# app.register_blueprint(search_shigotonavi)
app.register_blueprint(search_hellowork)
app.register_blueprint(inquiry)


# ルーティング処理

@app.route('/')
def index():
    return render_template('hellowork.html')


@app.route('/hellowork')
def hellowork():
    return render_template('hellowork.html')

# @app.route('/shigotonavi')
# def shigotonavi():
#     return render_template('shigotonavi.html')


@app.route('/inquiry')
def inquiry():
    return render_template('inquiry.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'GET':
#         return render_template("login.html",msg="")

#     email = request.form['email']
#     password = request.form['password']
#     try:
#         user = auth.sign_in_with_email_and_password(email, password)
#         session['usr'] = email
#         return redirect('/')
#     except:
#         return render_template("login.html", msg="メールアドレスまたはパスワードが間違っています。")

# @app.route('/logout')
# def logout():
#     del session['usr']
#     return redirect(url_for('login'))


@app.errorhandler(500)
def internal_server_error_html(error):
    return render_template('no_result.html'), 500


if __name__ == "__main__":
    app.run()
    # port = int(os.getenv("PORT", 8000))
    # app.run(host="0.0.0.0", port=port)
