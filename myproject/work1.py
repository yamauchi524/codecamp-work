# coding:utf-8

from flask import Flask
#テンプレートを読み込む
from flask import render_template
#リクエスト
from flask import request

#自分をappという名称でインスタンス化
app = Flask(__name__)


#HTMLの読み込み
#@app.route("/work1", methods=["GET"])
#def work1_send():
#    return render_template('work1.html')

#送信
@app.route("/work1", methods=["GET"])
def work1(my_name="",gender="",mail=""):
    return render_template('work1.html',my_name=my_name,gender=gender,mail=mail)

#受け取り
@app.route("/work1", methods=["POST"])
def work1_post():
    my_name = request.form.get("my_name","")
    gender = request.form.get("gender","")
    mail = request.form.get("mail","")
    return work1(my_name, gender, mail)