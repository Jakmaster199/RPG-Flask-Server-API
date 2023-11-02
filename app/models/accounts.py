from app import myDb
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
import bcrypt


class Account(myDb.Model):

    __tablename__ = "Accounts"

    account_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(24), nullable=False)
    password = Column(String(62), nullable=False)
    email = Column(String(64))
    access_level = Column(Integer)
    registration_date = Column(DateTime, default=datetime.utcnow())
    last_modification = Column(DateTime, default=datetime.utcnow())

    def __init__(self, username: str, password: str, email: str):
        self.username = username
        self.password = password # self.encrypt_password(password.encode('utf-8'), "00".encode('utf-8'))
        self.email = email
        self.access_level = 0

        self.registration_date = datetime.utcnow()
        self.last_modification = datetime.utcnow()

    def encrypt_password(self, password: bytes, salt: bytes = None):
        salt = self.registration_date if not salt else salt

        return bcrypt.hashpw(password, salt)
