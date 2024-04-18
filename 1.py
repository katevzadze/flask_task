from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


# http://127.0.0.1:5000/world

@app.route('/world')
def world():
    return 'Весной природа прекрасна! Все расцветает, и появляются первые насекомые.'


if __name__ == '__main__':
    app.run()
