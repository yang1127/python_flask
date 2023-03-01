# -*-coding:utf-8-*-
from flask import Blueprint, render_template

blueprint = Blueprint('new', __name__, url_prefix='/news', template_folder='templates', static_folder='static')
"""
参数1：蓝图名称
参数2：__name__ 该蓝图所在模块，该蓝图实现文件是 new.py，因此__name__是 'news'
参数3：指定页面的 URL 前缀为 '/news'
"""


@blueprint.route('/society/')
def society_news():
    return render_template('society.html')


@blueprint.route('/tech/')
def tech_news():
    return render_template('tech.html')