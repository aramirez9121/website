from flask import Flask, render_template
app = Flask(__name__)

valid_users = ['Randy', 'Amy', 'Yo', 'Amy']


@app.route("/")
def hello():
    return render_template('hello.html')


@app.route('/login')
def testing():
    return render_template('403.html')


@app.route("/goodbye")
def goodbye():
    return render_template('goodbye.html', users=valid_users)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
