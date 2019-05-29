from flask import Flask


app = Flask(__name__)


@app.route('/team')
def hello_world():
    return 'OSS!'


@app.route('/team/<string:name>')
def ping(name):
    return 'team %s' % name
