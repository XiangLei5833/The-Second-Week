from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('user_index', username='default'))

@app.route('/user/<username>')
def user_index(username):
    return render_template('user_index.html', username=username)


if __name__ == '__main__':
    app.run()
