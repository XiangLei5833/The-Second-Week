from flask import render_template,Flask

app = Flask(__name__)

@app.route('/user/<username>')
def user_index(username):
    return render_template('user_index.html', uaername=username)

if __name__ == '__main__':
    app.run()
