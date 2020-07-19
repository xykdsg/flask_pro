# 从flask框架中导入Flask这个类
from flask import Flask, url_for
import config
import json

# 初始化一个Flask对象
# 需要传递一个参数__name__
# 1.方便flask框架去寻找资源
# 2.方便flask插件出现错误时，好去寻找问题所在的位置
app = Flask(__name__)
# 配置文件来设置参数
app.config.from_object(config)


# 装饰器的作用：做一个url和视图函数的映射
@app.route('/')
def hello_world():
    print(url_for("article", param="111"))
    return json.dumps({"胡润丽": "大傻逼"}, ensure_ascii=False)


@app.route('/article/<param>')
def article(param):
    return f"{param}"


# 如果当前这个文件是作为入口程序运行，就执行app.run()
if __name__ == '__main__':
    # 启动一个应用服务器，来接受用户的请求
    # 相当于
    # while True:
    #     listen()
    app.run(host="0.0.0.0", port=8080)
