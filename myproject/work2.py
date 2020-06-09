# coding:utf-8

from flask import Flask
#テンプレートを読み込む
from flask import render_template
#リクエスト
from flask import request

#自分をappという名称でインスタンス化
app = Flask(__name__)

#POSTの場合
#入力画面
@app.route("/work2")
def send():
    return render_template('work2_send.html')

#出力画面
@app.route("/work2", methods=["POST"])
def receive():
    my_name = request.form.get("my_name","")
    return render_template('work2_recieve.html',my_name=my_name)

