# -*-coding:utf-8-*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

user = 'root'
password = 'yyy1536520643'
database = 'school'
uri = 'mysql+pymysql://%s:%s@localhost:3306/%s' % (user, password, database)
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True


# 创建数据库实例
db = SQLAlchemy(app)

# 建立类与表之间的映射
# 创建类 Student 继承于 db.Model
class Student(db.Model):
    __tablename__ = 'students'
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    age = db.Column(db.Integer)

    def dump(self):
        print(self.sno, self.name, self.age)


def create_table():
    db.drop_all()  # 调用 db.drop_all() 删除数据库 school 中的所有表格
    db.create_all()  # 调用 db.create_all() 创建已经建立映射关系的表 students，表 students 已经被映射到类 Student


# 增
def insert_students():
    # 单个增
    yzq = Student(sno=4, name='yzq', age=18)
    db.session.add(yzq)
    db.session.commit()

    # 批量增
    zdz = Student(sno=5, name='zdz', age=18)
    zz = Student(sno=6, name='zz', age=19)
    db.session.add_all([zdz, zz])
    db.session.commit()


# 删
def delete_students():
    students = Student.query.filter_by(name="tom")
    students.delete()
    db.session.commit()


# 查
def query_students():
    # 3.1 查询所有学生
    students = Student.query.all()
    for student in students:
        student.dump()
    print()

    # 3.2 指定查询
    # 例如：查询年龄是18的学生
    students1 = Student.query.filter_by(age=18)
    for student1 in students1:
        student1.dump()
    print()

    # 3.3 查询第一个符合条件的数据
    # 例如：查询第一个年龄为18的学生
    students3 = Student.query.filter_by(age=18)
    student3 = students3.first()
    student3.dump()
    print()

    # 3.4 组合查询
    # 例如：查询姓名为zz，且年龄为19的学生
    students4 = Student.query.filter_by(age=19, name='zz')
    for student4 in  students4:
        student.dump()


# 改
def update_studnets():
    students = Student.query.filter_by(name='zz')
    students.update({'name': 'ZZ'})
    print()

