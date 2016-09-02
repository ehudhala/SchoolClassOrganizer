from sqlalchemy import create_engine, Column, Integer, String, Sequence, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from class_organizer.consts import DB_CONNECTION_STRING

MEDIUM_STR_LEN = 1024

Base = declarative_base()


class Child(Base):
    """
    A table that represents a child.
    """
    __tablename__ = 'children'

    id = Column(Integer, Sequence('child_id_sequence'), primary_key=True)
    name = Column(String(MEDIUM_STR_LEN))
    birth_date = Column(DateTime)
    address = Column(String(MEDIUM_STR_LEN))

    def __repr__(self):
        return u'Child({0})'.format(self.name)

engine = create_engine(DB_CONNECTION_STRING)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

