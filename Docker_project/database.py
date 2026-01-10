from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

## Direccion de la base de datos
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

## Este es el motor de la base de datos
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )

# Crear las sesiones de la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos de la base de datos
Base = declarative_base()



class SensorReading(Base):
    __tablename__ = "sensor_readings"
    
    id = Column(Integer, primary_key = True, index = True)
    temperature = Column(Float)
    humidity = Column(Float)
    pressure = Column(Float)
