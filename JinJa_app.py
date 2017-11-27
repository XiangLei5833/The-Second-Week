#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True    # 每当模板改变，自动重新渲染

@app.route('/')
def index():
    teacher = {
            'name':'Aiden',
            'email':'luojin@simplecloud.cn'
            }

    course = {
            'name':'Python Basic',
            'teacher':teacher,
            'user_count':5348,
            'price':199.0,
            'lab': None,
            'is_private': False,
            'is_member_course': True,
            'tags':['python', 'big data', 'linux']
            }
    return render_template('JinJa_index.html', course=course)
   
