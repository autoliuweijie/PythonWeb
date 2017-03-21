# coding:utf-8
from flask import Flask, session, redirect, url_for, request


app = Flask(__name__)
app.secret_key = '\xf1\x92Y\xdf\x8ejY\x04\x96\xb4V\x88\xfb\xfc\xb5\x18F\xa3\xee\xb9\xb9t\x01\xf0\x96'  # 用于对session加密


@app.route("/", methods=['GET'])
def index():
    username = session.get('username')
    password = session.get('password')
    if username == 'Liu Weijie' and password == 'liuweijie':
        return "hello! Liu Weiijie"
    else:
        return "Please Loggin!"


@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        return "Login Successfully!"
    else:
        ret_view = """
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=text name=password>
            <p><input type=submit value=Login>
        </form>
        """
        return ret_view

@app.route("/logout", methods=['GET'])
def logout():
    session.pop('username', None)
    session.pop('password', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=7002)