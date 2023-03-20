from flask import render_template

from info import create_app,db,models  #导入models的作用是让整个应用程序知道models的存在
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from flask_sqlalchemy import SQLAlchemy

app=create_app('develop')


@app.errorhandler(404)  # 传入错误码作为参数状态
def error_date(error):  # 接受错误作为参数
    return render_template("404.html"), 404  # 返回对应的http状态码，和返回404错误的html文件

#创建manage对象，管理app
manager = Manager(app)

#使用Migrate关联app，db
Migrate(app,db)

#给manager添加一条操作命令
manager.add_command("db",MigrateCommand)



if __name__ == '__main__':


    manager.run()
