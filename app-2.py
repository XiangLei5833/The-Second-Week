from flask import Flask, render_template, abort
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root@localhost/shiyanlou'
db = SQLAlchemy(app)

class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    content = db.Column(db.Text)
    created_time = db.Column(db.DateTime)
    category = db.relationship('Category', backref = db.backref('files'))
    
    def __init__(self, title,  category, content, created_time=None):
        self.title = title
        self.category = category
        self.content = content
        if created_time is None:
            created_time = datetime.utcnow()
        self.created_time = created_time
    def __repr__(self):
        return '<File %s>' % self.title

class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))
    
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return '<Category %s>' % self.name

titles = File.query.all()
news1 = titles[0]
news2 = titles[1]
@app.route('/')
def index():
    title = {
            'title1': news1.title,
            'title2': news2.title
            }
    return render_template('index.html',title=title, titles=titles)

@app.route('/files/<file_id>')
def file(file_id):
    file_content = {
            'title1': news1.title,
            'title2': news2.title,
            'created_time1': news1.created_time,
            'created_time2': news2.created_time,
            'content1': news1.content,
            'content2': news2.content,
            'type1': news1.category,
            'type2': news2.category
            }
    return render_template('file.html', file_content=file_content, file_id=file_id, titles=titles)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404
    

if __name__ == '__main__':
    app.run()
