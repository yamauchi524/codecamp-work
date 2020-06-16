#実習課題1
#ひとこと掲示板

# coding:utf-8

#Flask,テンプレート,リクエスト読み込み
from flask import Flask, render_template, request

import mysql.connector
from mysql.connector import errorcode

#時間を取得
import datetime

#自分をappという名称でインスタンス化
app = Flask(__name__)

@app.route("/bbs", methods=["POST"])
def mysql_bbs():
    # import部分は省略
    host = 'localhost' # データベースのホスト名又はIPアドレス
    username = 'root'  # MySQLのユーザ名
    passwd   = 'Hito05hito'    # MySQLのパスワード
    dbname   = 'my_database'    # データベース名

    #初期値
    name=""
    comment=""

    #入力判定
    result = ""

    if "name" in request.form.keys():
        name = request.form.get("name")

    if "comment" in request.form.keys():
        comment = request.form.get("comment")
        #request.form.getで取得する値は全て文字列になっている！

    #時間の取得
    dt_now = datetime.datetime.now()
    #日付を文字列に変換
    date = dt_now.strftime('%Y-%m-%d %H:%M:%S')

    try:
        cnx = mysql.connector.connect(host=host, user=username, password=passwd, database=dbname)
        cursor = cnx.cursor()

        #常にテーブルを表示
        query = 'SELECT bbs_name, comment, bbs_date FROM bbs_table'

        #文字が入力されていない場合
        if name == "" or price == "":
            cursor.execute(query)
            result = ""

        else:
            try:
                add_query = "INSERT INTO bbs_table(bbs_name, comment, bbs_date) VALUES('" + name + "','" + comment +"','" + date + "')"
                cursor.execute(add_query)
                cnx.commit() # この処理が無いと変更が反映されません！

            except mysql.connector.Error as err:
                print(err)
                result = "指定文字数以内で入力してください。"
            
            cursor.execute(query)

        bbs = []
        for (name, comment, date) in cursor:
            item = {"name": name, "comment":comment, "date":date}
            bbs.append(item)

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("ユーザ名かパスワードに問題があります。")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("データベースが存在しません。")
        else:
            print(err)
    else:
        cnx.close()

    return render_template("bbs.html", bbs=bbs, result=result)

