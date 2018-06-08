# 声明数据库中表对应的模型类
from datetime import datetime

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, Column, String, ForeignKey, Boolean, DateTime, Float
from sqlalchemy.orm import relationship, backref



db = SQLAlchemy()

def init_db(app):
    db.init_app(app)
    Migrate(app, db)

class Letter(db.Model):
    __tablename__ = 't_letter'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(10))

class City(db.Model):

    __tablename__ = 't_city'
    id = Column(Integer, primary_key=True, autoincrement=True)
    parentId = Column(Integer, default=0)
    regionName = Column(String(30))
    cityCode = Column(Integer)
    pinYin = Column(String(50))

    letter_id = Column(Integer, ForeignKey(Letter.id))
    letter = relationship("Letter", backref=backref("citys", lazy=True))
class IdBase(object):
    id = Column(Integer, primary_key=True, autoincrement=True)

class Role(db.Model, IdBase):
    # 用户角色
    name = Column(String(20))
    rights = Column(Integer, default=1)

class User(db.Model):
    __tablename__ = 't_user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True)
    password = Column(String(50))
    nickname = Column(String(20))
    email = Column(String(50), unique=True)
    phone = Column(String(12), unique=True)
    is_active = Column(Boolean, default=False)
    is_life = Column(Boolean, default=True)
    regist_time = Column(DateTime, default=datetime.now())
    last_login_time = Column(DateTime)
    # 新增头像的属性
    photo_1 = Column(String(200),nullable=True)  # 原图
    photo_2 = Column(String(200), nullable=True)  # 小图

    # 权限(被管理员授权)
    rights = Column(Integer, default=1)
    # 用户角色
    role_id = Column(Integer, ForeignKey(Role.id))
    role = relationship('Role', backref=backref('users', lazy=True))

class Movies(db.Model, IdBase):

    showname = Column(String(200))
    shownameen = Column(String(200))
    director = Column(String(200))
    leadingRole = Column(String(200))
    type = Column(String(200))
    country = Column(String(200))
    language = Column(String(200))
    duration = Column(Integer)
    screeningmodel = Column(String(200))
    openday = Column(DateTime)
    backgroundpicture = Column(String(200))
    flag = Column(Integer)
    isdelete = Column(Boolean)

class Cinemas(db.Model, IdBase):

    name = Column(String(200))
    city = Column(String(200))
    district = Column(String(200))
    address = Column(String(200))
    phone = Column(String(200))
    score = Column(Float(precision=1))
    hallnum = Column(Integer)
    servicecharge = Column(Float(precision=2))
    astrict = Column(Integer, default=5)
    flag = Column(Integer)
    isdelete = Column(Boolean)


class Qx(db.Model, IdBase):
    name = Column(String(30))
    right = Column(Integer)






