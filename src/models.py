import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    username = Column(String(30), nullable=False)
    password = Column(String(30), nullable=False)

    def serialize(self):
        return {
            "email": self.email,
            "username": self.username
        }

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    diameter = Column(String(30), nullable=False)
    rotation_period = Column(String(30), nullable=False)
    orbital_period = Column(String(30), nullable=False)
    gravity = Column(String(30), nullable=False)
    population = Column(String(30), nullable=False)
    climate = Column(String(30), nullable=False)
    terrain = Column(String(30), nullable=False)
    description = Column(String(30), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period":self.orbital_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "description": self.description
        }

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)
    manufacturer = Column(String(50), nullable=True)
    cost_in_credits = Column(String(50), nullable=True)
    length = Column(String(50), nullable=True)
    max_atmosphering_speed = Column(String(50), nullable=True)
    crew_id = Column(String(50), nullable=True)
    passengers_id = Column(String(50), nullable=True)
    cargo_capacity = Column(String(50), nullable=True)
    consumables = Column(String(50), nullable=True)
    vehicle_class = Column(String(50), nullable=True)
    pilots_id = Column(String(50), nullable=True)
    films = Column(String(50), nullable=True)
    # crew = relationship(Characters)
    # passengers = relationship(Characters)
    # pilots = relationship(Characters)


    def serialize(self):
        return {
            "name": self.name,
            "model": self.model,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "length": self.length,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "crew": self.crew,
            "passengers": self.passengers,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables,
            "vehicle_class": self.vehicle_class,
            "pilots": self.pilots,
            "films": self.films

        }

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    height = Column(String(50), nullable=True)
    mass = Column(String(50), nullable=True)
    hair_color = Column(String(50), nullable=True)
    skin_color = Column(String(50), nullable=True)
    eye_color = Column(String(50), nullable=True)
    birth_year = Column(String(50), nullable=True)
    gender = Column(String(50), nullable=True)
    planet_id = Column(Integer, ForeignKey('planets.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    description = Column(String(50), nullable=True)
    planet = relationship(Planets)
    vehicle = relationship(Vehicles)

    def serialize(self):
        return {
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "gender": self.gender,
            "planet_id": self.planet_id,
            "vehicle_id": self.vehicle_id

        }

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('characters.id'))
    planet_id = Column(Integer, ForeignKey('planets.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))

    user = relationship(User)
    characters = relationship(Characters)
    planets = relationship(Planets)
    vehicles = relationship(Vehicles)

    def serialize(self):
        return {
            "user_id": self.user_id,
            "character_id": self.character_id,
            "planet_id": self.planet_id,
            "vehicle_id": self.vehicle_id
        }

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
