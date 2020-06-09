# coding:utf-8

from flask import Flask
#テンプレートを読み込む
from flask import render_template
#リクエスト
from flask import request

#random関数を使う
import random

#自分をappという名称でインスタンス化
app = Flask(__name__)

#POSTの場合
#入力画面
@app.route("/work3")
def send():
    return render_template('work3.html')

#出力画面
@app.route("/work3", methods=["POST"])
def receive():
    jibun = request.form.get("jibun","")

    #相手が出す手
    pc = ["グー","チョキ","パー"]
    aite = random.choice(pc)

    if jibun == aite:
        result = "DRAW"
    else:
        if jibun == "グー":
            if aite == "チョキ":
                result = "Win!!"
            else:
                result = "Lose..."
        elif jibun == "チョキ":
            if aite == "パー":
                result = "Win!!"
            else:
                result = "Lose..."
        else:
            if aite == "グー":
                result = "Win!!"
            else:
                result = "Lose..."

    return render_template('work3.html',jibun=jibun, aite=aite, result=result)