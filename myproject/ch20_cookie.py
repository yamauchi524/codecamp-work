# coding:utf-8

#Flask,テンプレート,リクエスト読み込み
from flask import Flask, render_template, request
from flask import make_response

import datetime
#import tkinter

#自分をappという名称でインスタンス化
app = Flask(__name__)

@app.route("/cookie",methods=["GET", "POST"])
def index():
    count = request.cookies.get('count')
    #now_dataに入っている情報を呼び出す
    last_date = request.cookies.get('now_date',"")

    dt_now = datetime.datetime.now()
    now_date = dt_now.strftime('%Y年%m月%d日 %H:%M:%S')

    if count is None:
        count = 1
    else:
        count = int(count) + 1

    response = make_response(render_template("cookie.html",count=count,now_date=now_date,last_date=last_date))

    if "delete_cookie" in request.form.keys():
        response.set_cookie('count', str(count),expires=0)
        response.set_cookie('now_date', now_date,expires=0)
        response.set_cookie('last_date', last_date,expires=0)
        #response.set_cookie('count', 0)
        #response.set_cookie('now_date', "")
        #response.set_cookie('last_date', "")

    else:
        response.set_cookie('count', str(count))
        response.set_cookie('now_date', now_date)
        response.set_cookie('last_date', last_date)

    return response