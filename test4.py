# -*-coding:utf-8-*-
from flask import Flask, render_template, views
app = Flask(__name__)

# 父类
class BaseView(views.View):
    def get_template(self):
        raise NotImplementedError()

    def get_data(self):
        raise NotImplementedError()

    def dispatch_request(self):
        data = self.get_data()
        template = self.get_template()
        return render_template(template, **data)

# 子类
class UserView(BaseView):
    def get_template(self):
        return 'user.html'

    def get_data(self):
        return {
            'name': 'yzq',
            'gender': 'male',
        }

app.add_url_rule(rule='/User/', view_func=UserView.as_view('UserView'))
app.run()