from sqlalchemy import Column, Integer, String
from database import Base

class game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), unique=True)

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return f'{self.title}'
    