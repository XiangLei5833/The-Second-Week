from flask import Flask

app = Flask(__name__)

@app.route('/user/<username>')
def user_index(username):
    return 'Hello {}'.format(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post{}'.format(post_id)

if __name__ == '__main__':
    app.run()
