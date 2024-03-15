from db import engine
from models import User, Device
from random import randint
from sqlalchemy.orm import sessionmaker
from datetime import datetime


session = sessionmaker(bind=engine)
s = session()


def check_user(db: session(), telid: str) -> bool: # Функция проверки пользователя на зарегестрированность
    zn = db.query(User).filter(User.telid == telid).group_by(User).first()

    if zn == None:
        return False
    return True


def create_user(db: session(), user: dict) -> None: # Функция создания юзера
    date = datetime.utcnow()
    user = User(telid = user['telid'], username = user['username'], register_date=date)
    db.add(user)
    db.commit()


def create_device(db: session(), device: dict) -> None: # Функция создания девайса
    dev = Device(device_title = device['device_title'],params = device['params'], description = device['description'], company = device['company'], device_type = device['device_type'], price = device['price'])

    db.add(dev)
    db.commit()


def get_all_dev_types(db: session()) -> list:
    devs = s.query(Device).all()
    return devs


def get_dev_by_id(db: session(), id: int) -> list:
    dev = s.query(Device).filter(Device.id == id).first()
    return dev


def get_dev_by_title(db: session(), title: str) -> list:
    dev = s.query(Device).filter(Device.device_title == title).all()
    return dev


def get_dev_by_title_and_params(db: session(), title: str, params: str) -> Device:
    dev = s.query(Device).filter(Device.device_title == title).filter(Device.params == params).first()
    return dev