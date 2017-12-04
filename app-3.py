from flask import Flask, render_template, abort
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime
from pymongo import MongoClient

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root@localhost/shiyanlou'
db = SQLAlchemy(app)
client = MongoClient('127.0.0.1',27017)
db_client = client.shiyanlou

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

    def add_tag(self, tag_name):
        file_tag = {'file_id': self.id, 'tag_name': tag_name}
        db_client.tag.insert_one(file_tag)

    def remove_tag(self, tag_name):
        delete_tag = db_client.tag.find_one({'file_id': self.id})
        if 'tag_name' in delete_tagvalues():
            db_client.tag.delete_one({'file_id': self.id})
        else:
            print('tag_name not been found')
     
    @property
    def tags(self):
        tags = []
        find_tag = db_client.tag.find({'file_id': self.id})
        for tag in find_tag:
            tags.append(tag['tag_name'])
        return tags

            
class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))
    
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return '<Category %s>' % self.name

@app.route('/')
def index():
    titles = File.query.all()
    return render_template('index.html',titles=titles)

@app.route('/files/<file_id>')
def file(file_id):
    file_name = File.query.filter_by(id=file_id).first()
    file_content = {
            'title': file_name.title,
            'created_time': file_name.created_time,
            'content': file_name.content,
            'type': file_name.category
            }
    file_list = list(file_content.values())
    return render_template('file.html', file_list=file_list)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404
    

if __name__ == '__main__':
    app.run()
