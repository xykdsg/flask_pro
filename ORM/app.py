from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)  # 初始化一个SQLAlchemy对象

db.create_all()


# create table article(
#     id int primary key autoincrement,主键,id自增长
#     title varchar(100) not null,
#     content text not null,
# )


class Article(db.Model):  # 相当于创建一张表
    __tablename__ = "article"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 设置主键
    title = db.Column(db.String(100), nullable=False)  # varchar类型，100个字符长度，不能为空
    content = db.Column(db.TEXT, nullable=False)  # 创建text类型


db.create_all()


@app.route('/')
def index():
    # 增加：
    # article1 = Article(title='aaa', content='bbb')
    # db.session.add(article1)
    # # 事务，需要对事务进行提交
    # db.session.commit()

    # 查
    # Select * from article where title='aaa'
    # result = Article.query.filter(Article.title == 'aaa').all()
    # article1 = result[0]
    # article1 = Article.query.filter(Article.title == 'aaa').first()
    # print('title:', article1.title)
    # print('content:', article1.content)

    # 改
    # # 1.先把需要改的数据查出来
    # article1 = Article.query.filter(Article.title == 'aaa').first()
    # # 2.该条记录，需要修改的地方进行修改
    # article1.title = 'new title'
    # # 3.提交事务
    # db.session.commit()

    # 删
    # 1.需要删除的数据查找出来
    article1 = Article.query.filter(Article.content == 'bbb').first()
    # 2.各条数据删除
    db.session.delete(article1)
    # 3.事务提交
    db.session.commit()
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
