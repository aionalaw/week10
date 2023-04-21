from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/greeting/')
def greeting():
    return 'Seasonal Greetings!'

@app.route('/merrychristmas/')
def greeting_christmas():
    return 'Merry Christmas!'

@app.route('/happynewyear/')
def greeting_newyear():
    return 'Happy New Year!'


if __name__ == "__main__":
    app.run()