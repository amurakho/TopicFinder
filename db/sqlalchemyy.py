from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

if os.path.exists('../some.db'):
    os.remove('../some.db')
engine = create_engine('sqlite:///some.db', echo=True)


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String(50))

Base.metadata.create_all(engine)

session = sessionmaker(bind=engine)()

ed_user = User(name='Artem', fullname='Mur', nickname='asd')

session.add(ed_user)

session.commit()