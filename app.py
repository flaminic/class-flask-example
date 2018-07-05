from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return 'Hello'

@app.route("/celiyfede")
def otra():
    return render_template('celifede.html')


@app.route("/welcome")
def welcome():
    return render_template('welcome.html')\

@app.route("/template")
def template():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()

