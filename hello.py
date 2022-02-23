'''
from flask import Flask

app = Flask(__name__)

# Flask类的一个对象是WSGI应用程序
# Flask类的route()函数是一个装饰器，它告诉应用程序哪个URL应该调用相关的函数
# app.route(rule, options)
# rule 参数表示与该函数的URL绑定
# options 是要转发给基础Rule对象的参数列表

@app.route('/')
def hello_name():
   return 'Hello world'
'''

# Flask构造函数使用当前模块（__name __）的名称作为参数
# Flask类的run()方法在本地开发服务器上运行应用程序

# app.run(host, port, debug, options)
# host：要监听的主机名。 默认为127.0.0.1（localhost）。设置为“0.0.0.0”以使服务器在外部可用
# port：默认值为5000
# debug：默认为false。 如果设置为true，则提供调试信息
# options：要转发到底层的Werkzeug服务器
'''
app.debug = True
app.run()
app.run(debug = True)


if __name__ == '__main__':
   app.run()
'''

'''路由
from flask import Flask

app = Flask(__name__)


# Flask中的route()装饰器用于将URL绑定到函数
@app.route('/hello')
def hello_world():
   return 'hello_world'


app.add_url_rule('/', 'hello', hello_world)

if __name__ == '__main__':
   app.run()
'''

'''
变量规则：通过向规则参数添加变量部分，可以动态构建URL
此变量部分标记为<variable-name>，它作为关键字参数传递给与规则相关联的函数
from flask import Flask

app = Flask(__name__)


# 1、字符串类型
@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name

# 2、整数
@app.route('/intnum/<int:num>')
def show_Intnum(num):
   return 'num %d' % num

# 3、浮点数
@app.route('/floatnum/<float:num>')
def show_Flaotnum(num):
   return 'floatnum %f' % num


# 4、用作目录分隔符的斜杠 /
@app.route('/python/')
def hello_python():
   return 'Hello Python'


if __name__ == '__main__':
    app.run()
'''

'''
# URL构建 - url_for()函数
from flask import Flask, redirect, url_for
app = Flask(__name__)


@app.route('/admin')
def hello_admin():
   return 'Hello Admin！'


@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest！' % guest


@app.route('/user/<name>')
def hello_user(name):
   if name == 'admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest', guest=name))


if __name__ == '__main__':
   app.run(debug=True)
'''
'''
# http
from flask import Flask, redirect, url_for, request
app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name


@app.route('/login', methods=['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success', name=user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success', name=user))


if __name__ == '__main__':
   app.run(debug=True)
'''

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('test.html')

'''
# 模版
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    my_int = 18
    my_str = '小杨'
    my_list = [1, 2, 5, 4, 3]
    my_dict = {
        'name': 'yzq',
        'age': 24
    }

    # render_template方法: 渲染模板
    # 参数1: 模板名称  参数n: 传到模板里的数据
    return render_template('hello.html',
                           my_int=my_int,
                           my_str=my_str,
                           my_list=my_list,
                           my_dict=my_dict)


if __name__ == '__main__':
    app.run(debug=True)
'''