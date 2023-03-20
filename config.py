import logging
import os
from datetime import timedelta
from redis import StrictRedis

basedir = os.path.abspath(os.path.dirname(__file__))


#配置信息类的基类
class Config(object):
    #配置调试信息
    DEBUG = True
    SECRET_KEY = 'KIRI'

    #配置数据库信息
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, r'db\FD.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    #配置redis信息
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    #配置session信息
    SESSION_TYPE='redis' #设置session存储类型
    SESSION_REDIS=StrictRedis(host=REDIS_HOST,port=REDIS_PORT) #设置session存储的redis服务器
    SESSION_USE_SIGNER = True  #设置签名存储
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=30) #设置session的有效期，两天时间

    #配置日志级别
    LEVEL_NAME=logging.DEBUG

#开发环境配置信息
class DevelopConfig(Config):
    pass


#生产环境配置信息
class ProductConfig(Config):
    DEBUG = False
    LEVEL_NAME = logging.ERROR


#测试环境配置信息
class TestConfig(Config):
    pass


#提供统一的访问入口
config_dict={
    'develop':DevelopConfig,
    'product':ProductConfig,
    'test':TestConfig
}

