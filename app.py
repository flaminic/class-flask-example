from flask import Flask, render_template, request

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


@app.route("/profiles")
def profiles():
    usuarios = ['celi', 'belu', 'flami', 'santa claus']
    return render_template('profiles.html', usuarios = usuarios)


@app.route("/profile/<nombre>")
def profile(nombre):
    return render_template('profile.html', first_name = nombre)

@app.route("/register-profile")
def register_profile():
    name = request.args['firstName']
    name2 = request.args['lastName']
    password = request.args['password']
    nascita = request.args['birthdate']
    return render_template('register-profile.html', name=name, name2 = name2, nascita=nascita)

@app.route("/register")
def register():
    return render_template('register.html')


if __name__ == "__main__":
    app.run()

