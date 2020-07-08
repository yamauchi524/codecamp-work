# coding:utf-8

#Flask,テンプレート,リクエスト読み込み
from flask import Flask, render_template, request
from flask import session

import datetime

app = Flask(__name__)
app.secret_key = 'ch20session'

@app.route("/session",methods=["GET", "POST"])
def index():
    count = session.get('count')
    last_date = session.get('now_date')

    dt_now = datetime.datetime.now()
    now_date = dt_now.strftime('%Y年%m月%d日 %H:%M:%S')

    if count is None:
        count = 1
    else:
        count = int(count) + 1

    if "delete_session" in request.form.keys():
        session["count"] = None
        session["last_date"] =  ""
        session["now_date"] = ""
    else:
        session["count"] = count
        session["last_date"] = last_date
        session["now_date"] = now_date

    return render_template("session.html",count=count,now_date=now_date,last_date=last_date)
