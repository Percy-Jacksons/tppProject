class Config():
    ENV = 'development'
    DEBUG = True
    #  配置数据库连接
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@10.35.163.1:3306/tpp'


    # 配置邮箱
    MAIL_SERVER = 'smtp.163.com'  # 邮箱服务器
    MAIL_USERNAME = '18700908960@163.com'
    MAIL_PASSWORD = 'hzy8888'  #授权码
    # 配置安全密钥
    SECRET_KEY = '@#$%^&dghjkedfg'

class QX():
    QUERY_QX = 1
    EDIT_QX = 2
    DELETE_QX = 4
    ADD_QX = 8
    MAIL_QX = 16
    PLAY_QX = 32



