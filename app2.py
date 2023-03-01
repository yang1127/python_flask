# -*-coding:utf-8-*-
from flask import Flask
from news import news
from products import products

app = Flask(__name__)

app.register_blueprint(news.blueprint)  # 注册蓝图对象 news.blueprint
app.register_blueprint(products.blueprint)  # 注册蓝图对象 products.blueprint

app.run()