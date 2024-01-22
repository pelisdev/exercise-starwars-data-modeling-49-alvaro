import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    email = Column(String(50), nullable=False)
    name = Column(String(50), nullable=False)
    password = Column(String(250), nullable=False)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    species = Column(String(20), nullable=False)
    gender = Column(String(10), nullable=False)

class Location (Base):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    type = Column(String(20), nullable=False)
    dimension = Column(String(10), nullable=False)

class Episode (Base):
    __tablename__ = 'episode'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    air_date = Column(String(50), nullable=False)
    episode = Column(String(50), nullable=False)

class Favorite (Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user = relationship(User)
    user_id = Column(Integer,ForeignKey('user.id'))
    characters = relationship(Characters)
    characters_id = Column(Integer,ForeignKey('characters.id'))
    episode = relationship(Episode)
    episode_id = Column(Integer,ForeignKey('episode.id'))



    def to_dict(self):
        return {}

render_er(Base, 'diagram.png')