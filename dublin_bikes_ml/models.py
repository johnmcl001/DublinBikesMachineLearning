from sqlalchemy import Column, Integer, String, DATETIME, FLOAT, ForeignKey
from dublin_bikes_ml.db import Base


class Weather(Base):
    __tablename__ = "Weather"
    time = Column(DATETIME, primary_key=True)
    temp = Column(FLOAT)
    feels_like = Column(FLOAT)
    humidity = Column(FLOAT)
    wind_speed = Column(FLOAT)
    description = Column(String(80))

    def __init__(self, time, temp, feels_like, humidity, wind_speed, description):
        self.time = time
        self.temp = temp
        self.feels_like = feels_like
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.description = description

    def __repr__(self):
        repr = ""
        attributes = self.__dict__
        for key in attributes:
            repr += str("{%s: %sk, " % (key, attributes[key]))
        return str(self.__dict__)


class BikeStand(Base):
    __tablename__ = "BikeStand"
    id = Column(Integer, primary_key=True, autoincrement=True)
    time = Column(DATETIME, ForeignKey("Weather.time"))
    numberOfBikes = Column(Integer)

    def __init__(self, time, numberOfBikes):
        self.time = time
        self.numberOfBikes = numberOfBikes

    def __repr__(self):
        return "{Time: %d, numberOfBikes: %d}" % (self.time, self.numberOfBikes)
