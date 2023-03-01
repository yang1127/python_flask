# -*-coding:utf-8-*-
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index2.html',
                           string1="yzq",
                           string2="helloyzq",
                           string3="abc")

if __name__ == '__main__':
    app.run()