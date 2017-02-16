'''
    Reference: http://docs.jinkan.org/docs/flask/quickstart.html#routing
'''
from flask import Flask, request, url_for


app = Flask(__name__)


@app.route('/')
def hello_world():
    '''
        Example: http://127.0.0.1:5000/
    '''
    return "Hello World!"


@app.route('/user', methods=['POST'])
def hello_user():
    '''
        Example: http://127.0.0.1:5000/user
    '''
    return "Hello User!"


@app.route('/user/<id>', methods=['GET'])
def hello_id(id):
    '''
        Example: http://127.0.0.1:5000/user/123
    '''
    return "Hello %s"%(id)


@app.route('/query_user', methods=['GET'])
def query_user():
    '''
        Example: http://127.0.0.1:5000/query_user?id=123
    '''
    id = request.args.get('id')
    return "Query user %s"%(id)


@app.route('/query_user_post', methods=['POST'])
def query_user_post():
    '''
        Example: http://127.0.0.1:5000/query_user_post
                 POST Body: id=1
    '''
    if request.method == 'POST':
        id = request.form['id']
    else:
        id = 0
    return "Query user %s"%(id)


@app.route('/query_url/<fun_name>', methods=['GET'])
def query_url(fun_name):
    '''
        Example: http://127.0.0.1:5000/query_url/query_user
    '''
    url = url_for(fun_name)  # query url of function
    return 'Query url: %s'%(url)


if __name__ == "__main__":
    app.run()