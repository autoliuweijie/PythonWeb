from flask import Flask, render_template, abort


app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


@app.route('/<user_id>')
def querry_user(user_id):
    if int(user_id) == 1:
        return "User found"
    else:
        abort(404)


if __name__ == '__main__':
    app.run()
