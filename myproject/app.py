from flask import Flask
from flask import render_template

app = Flask(__name__)

#第7章
#@app.route("/")
#def hello():
#    return "Hello, World!"

#第8章
#@app.route("/")
#def index():
#    return "Index Page"

#@app.route("/hello")
#def hello():
#    return render_template('hello.html', name="コード太郎")

#@app.route("/user/<username>")
#def show_user_profile(username):
#    return "User {}".format(username)

#@app.route("/post/<int:post_id>")
#def show_post(post_id):
    # show the post with the given id, the id is an integer
#    return "Post {}".format(post_id)

#
#@app.route("/path/<path:subpath>")
#def show_subpath(subpath):
    # show the subpath after /path/
#    return "Subpath {}".format(subpath)

#第9章
#@app.route('/hello/')
#@app.route('/hello/<name>')
#def hello(name=None):
#    return render_template('hello.html', name = name)

@app.route('/users')
def show_users():
    users = ["太郎", "花子", "一浪"]
    return render_template('users.html', users=users)

#第10章
@app.route("/send")
def send():
    return render_template('send.html')

from flask import request
@app.route("/receive", methods=["GET"])
def receive():
    if "my_name" in request.args.keys() :
        return "ここに入力した名前を表示： {}".format(request.args.get("my_name"))
    else:
        return "名前が未入力です"

#検索結果へのリンク
#GET
@app.route("/get_sample")
def get_sample():
    return render_template('get_sample.html', query=request.args.get("query") )

#POST
@app.route("/post_sample", methods=["GET"])
def sample(gender=""):
    return render_template('post_sample.html', gender=gender)

@app.route("/post_sample", methods=["POST"])
def post_sample():
    gender = request.form.get("gender","")
    return sample(gender)


