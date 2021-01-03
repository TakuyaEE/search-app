from flask import Flask, render_template, request, redirect, Blueprint, abort
from linebot import  LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import os

# 問い合わせフォーム
# フォームで入力されたデータをラインボットで送信する
inquiry = Blueprint('app_inquiry', __name__)

# LineMessageAPIのキー 環境変数から受け取る
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]
line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)



@inquiry.route("/inquiry_send", methods=['POST'])
def inquiry_send():
    # POSTから受け取り
    name = str(request.form.get('name'))
    email = str(request.form.get('email'))
    inquiry_category = str(request.form.get('inquiry_category'))
    content = str(request.form.get('Content'))

    messages = TextSendMessage( '名前:' + name + '\nメール:' + email + '\nカテゴリ:' + inquiry_category +'\n' + content )

    line_bot_api.broadcast(messages=messages)

    return render_template('inquiry_send.html', name = name, email = email, inqurity_category = inquiry_category, content = content)
