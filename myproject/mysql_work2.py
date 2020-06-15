# coding:utf-8

#Flask,テンプレート,リクエスト読み込み
from flask import Flask, render_template, request

import mysql.connector
from mysql.connector import errorcode

#自分をappという名称でインスタンス化
app = Flask(__name__)

@app.route("/mysql_work2")
def challenge_mysql_insert():
    # import部分は省略
    host = 'localhost' # データベースのホスト名又はIPアドレス
    username = 'root'  # MySQLのユーザ名
    passwd   = 'Hito05hito'    # MySQLのパスワード
    dbname   = 'my_database'    # データベース名

    #入力した商品名と価格を取得
    name = ""
    price = ""

    #priceが整数か否かを判定する
    result = "追加成功"

    if "name" in request.args.keys():
        name = request.args.get("name")

    if "price" in request.args.keys():
        price = request.args.get("price")
        #request.args.getで取得する値は全て文字列になっている！
        
        #priceが文字列か否かを判定
        #if type(price) is int == True:
        #    result = "追加成功" 
        #else:
        #    result = "追加失敗"

    try:
        cnx = mysql.connector.connect(host=host, user=username, password=passwd, database=dbname)
        cursor = cnx.cursor()

        #初期画面
        if name == "" and price == "":
            query = 'SELECT goods_name, price FROM goods_table'
            cursor.execute(query)
            result = ""

        else:
            try:
                query = "INSERT INTO goods_table(goods_name, price) VALUES('" + name + "'," + price +")"
                cursor.execute(query)
                cnx.commit() # この処理が無いと変更が反映されません！
            except mysql.connector.Error as err:
                print(err)
                result = "追加失敗"
            
            query = 'SELECT goods_name, price FROM goods_table'
            cursor.execute(query)

        goods = []
        for (name, price) in cursor:
            item = {"name": name, "price":price}
            goods.append(item)

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("ユーザ名かパスワードに問題があります。")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("データベースが存在しません。")
        else:
            print(err)
    else:
        cnx.close()

    return render_template("mysql_work2.html", goods=goods, result=result)

