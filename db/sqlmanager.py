import datetime

from sqlalchemy import create_engine, Column, String, Date, Integer, Boolean, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Link(Base):
    __tablename__ = 'main_links'

    id = Column(Integer, primary_key=True)
    url = Column(String)
    title = Column(String)
    pub_date = Column(Date, nullable=True)
    text = Column(String)
    scrapped = Column(Boolean, default=False)
    created_at = Column(Date, default=datetime.datetime.now())


class SqlManager:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(cls, SqlManager).__new__(cls)
        return cls.instance

    def __init__(self, settings):
        url = URL(**settings)
        self.engine = create_engine(url, echo=True)
        self.session = sessionmaker(bind=self.engine)()

    def add_to_base(self, data):
        for elem in data:
            link = Link(
                url=elem['url'],
                title=elem['title'],
                pub_date=elem['pub_date'],
                text=elem['text']
                        )
            self.session.add(link)

        self.session.commit()

    def create_table(self):
        metadata = Base.metadata
        metadata.bind = self.engine
        metadata.create_all()

