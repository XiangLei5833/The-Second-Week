import os
import json
from flask import Flask, render_template, abort

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

path0 = "/home/shiyanlou/files"
name = os.listdir(path0)
file1_path = os.path.join(path0, name[0])
file2_path = os.path.join(path0, name[1])
with open(file1_path, 'r') as papers1:
    file_content1 = json.loads(papers1.read())
with open(file2_path, 'r') as papers2:
    file_content2 = json.loads(papers2.read())

@app.route('/')
def index():
    title = {
            'title1': file_content1['title'],
            'title2': file_content2['title']
            }

    return render_template('index.html',title=title,name=name)

@app.route('/files/<filename>')
def file(filename):
    if os.path.isfile(file1_path) and os.path.isfile(file2_path):          
        file_content = { 
                       'title1': file_content1['title'],
                       'title2': file_content2['title'],
                       'created_time1': file_content1['created_time'],
                       'created_time2': file_content2['created_time'],
                       'content1': file_content1['content'],
                       'content2': file_content2['content']
                       }
    return render_template('file.html', file_content=file_content, filename=filename)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404
    

if __name__ == '__main__':
    app.run()
