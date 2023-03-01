# -*-coding:utf-8-*-
from flask import Flask, request, views
from functools import wraps

app = Flask(__name__)

# # 视图函数
# def check_login(original_function):
#     @wraps(original_function)
#     def decorated_function(*args,**kwargs):
#         user = request.args.get("user")
#         if user and user == 'zhangsan':
#             return original_function(*args, **kwargs)
#         else:
#             return '请先登录'
#     return decorated_function
#
# @app.route('/page1')
# @check_login
# def page1():
#     return 'page1'
#
# @app.route('/page2')
# @check_login
# def page2():
#     return 'page2'
#
# app.run()


# 视图类
def check_login(original_function):
    @wraps(original_function)
    def decorated_function(*args, **kwargs):
        user = request.args.get("user")
        if user and user == "zhangsan":
            return original_function(*args, **kwargs)
        else:
            return '请先登录'
    return decorated_function


class Page1(views.View):
    decorators = [check_login]

    def dispatch_request(self):
        return 'Page1'


class Page2(views.View):
    decorators = [check_login]

    def dispatch_request(self):
        return 'Page2'


app.add_url_rule(rule='/page1/', wiew_func=Page1.as_view("Page1"))
app.add_url_rule(rule='/page2/', wiew_func=Page2.as_view("Page2"))

app.run()