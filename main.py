from flask import Flask, render_template, request
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


@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['name'] in valid_users:
            return render_template('hello.html', user=request.form['name'])
        else:
            return render_template('goodbye.html')
    return render_template('login.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
