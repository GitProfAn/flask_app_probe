from flask import Flask 

app = Flask(__name__)

@app.route('/<name>')
def index(name):
    return f'<h1>Hello,  Big World! and {name}</h1>'

if __name__ == '__main__':
    app.run()