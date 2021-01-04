from flask import Flask, render_template, request, redirect, url_for, Blueprint, abort
from flask_sqlalchemy import SQLAlchemy
import os

from app_inquiry import inquiry
from app_search_hellowork import search_hellowork

# 別モジュールをblueprintで呼び出し
app.register_blueprint(search_hellowork)
app.register_blueprint(inquiry)


# ルーティング処理

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hellowork.html')

@app.route('/hellowork')
def hellowork():
    return render_template('hellowork.html')

@app.route('/inquiry')
def inquiry():
    return render_template('inquiry.html')

@app.errorhandler(500)
def internal_server_error_html(error):
    return render_template('no_result.html'), 500


if __name__ == "__main__":
    # app.run()
    port = int(os.getenv("PORT", 8000))
    app.run(host="0.0.0.0", port=port)