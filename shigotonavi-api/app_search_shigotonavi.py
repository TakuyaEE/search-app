from flask import Flask, render_template, request, redirect, url_for, Blueprint
import json

SN_API_KEY = "392567d8aa2c64385f619d1f448e52f4"


# search_shigotonavi = Blueprint('app_search_shigotonavi', __name__)


# @search_shigotonavi.route('/results', methods=['POST'])
# def results():
#     if request.method == 'POST':
#         # POSTから受け取り
#         prefecture = request.form.get('prefecture')
#         classfication = request.form.get('classfication')
#         free_word = ""
#         free_word = request.form.get('free_word')

classfication = "008"
prefecture = "0302000"
free_word = ""

response_json = request("http://www.shigotonavi.co.jp/api/search/?key=" + SN_API_KEY + "&sjt1=" + classfication + "&swt1=002&spc=" + prefecture + "&skw=" + free_word)
data = json.loads(response_json)
print(json.dumps(data, indent=2))
