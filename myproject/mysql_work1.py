# coding:utf-8

#Flask,テンプレート,リクエスト読み込み
from flask import Flask, render_template, request

import mysql.connector
from mysql.connector import errorcode

#自分をappという名称でインスタンス化
app = Flask(__name__)

@app.route("/mysql_work1")
def challenge_mysql_select():
    host = 'localhost' # データベースのホスト名又はIPアドレス
    username = 'root'  # MySQLのユーザ名
    passwd   = 'Hito05hito'    # MySQLのパスワード
    dbname   = 'my_database'    # データベース名

    select_job = ""
    if "select_job" in request.args.keys() :
            select_job = request.args.get("select_job")
            print(select_job)

    try:
        cnx = mysql.connector.connect(host=host, user=username, password=passwd, database=dbname)
        cursor = cnx.cursor()
        
        if select_job == "" or select_job == "all":
            query = 'SELECT * FROM emp_table'
        else:
            query = "SELECT * FROM emp_table WHERE job ='" + select_job + "'"

        cursor.execute(query)

        emps = []
        for (emp_id, emp_name, job, age) in cursor:
            emp_info = {"id":emp_id, "name": emp_name, "job":job, "age":age}
            emps.append(emp_info)

        params = {
        "mana_select" : select_job == "manager",
        "ana_select" : select_job == "analyst",
        "cle_select" : select_job == "clerk",
        "emps" : emps
        }

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("ユーザ名かパスワードに問題があります。")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("データベースが存在しません。")
        else:
            print(err)
    else:
        cnx.close()

    return render_template("mysql_work1.html", **params)
