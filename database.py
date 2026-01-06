from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

#engine = create_engine('sqlite:///test.db')
engine = create_engine('postgresql+psycopg2://postgres:password@localhost/loups')

db_session = scoped_session(sessionmaker(autoflush=False, autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    from models import game
    Base.metadata.create_all(bind=engine)