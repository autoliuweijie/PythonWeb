from flask import Flask, render_template
from models import User


app = Flask(__name__)


@app.route('/')
def hello_world():
    content = "Hello World!"
    return render_template('index.html', content=content)


@app.route('/user')
def hello_user():
    user = User('liuweijie', 1)
    return render_template('index_user.html', user=user)


@app.route('/user/<user_id>')
def hello_user_id(user_id):
    if int(user_id) == 1:
        user = User('liuweijie', 1)
    else:
        user = None
    return render_template('if_temp.html', user=user)


@app.route('/users')
def hello_users():
    users = []
    for id in range(10):
        users.append(User('liuweijie', id))
    return render_template('for_temp.html', users=users)


@app.route('/pages/<idx>')
def query_page(idx):
    idx = int(idx)
    if idx == 1:
        return render_template('one_base.html')
    else:
        return render_template('two_base.html')


if __name__ == "__main__":
    app.run()