from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('hello.html')


@app.route("/goodbye")
def goodbye():
    return render_template('goodbye.html')


@app.route("/users/<string:user>")
def user(user):
    return render_template('goodbye.html', user=user)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
