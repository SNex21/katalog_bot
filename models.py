from db import Base
from sqlalchemy import Column, String, Integer, Boolean
from db import engine


class User(Base): # Модель пользователя

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    telid = Column(Integer, unique=True, index=True)
    username = Column(String(100), default = None, unique=True)
    register_date = Column(String(100), default = None)


class Device(Base): # Модель товара

    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    device_title = Column(String(200))
    params = Column(String(200))
    description = Column(String(400), default=None)
    company = Column(String(200), default=None)
    device_type = Column(String(200), default=None)
    price = Column(String(200), default=None)


Base.metadata.create_all(engine)# Обновление моделей БД