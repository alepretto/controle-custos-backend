from pathlib import Path
from configparser import ConfigParser

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


root_path = Path(__file__).resolve().parent
config = ConfigParser()
config.read(f"{root_path}\\environment.cfg")
infos_db = config["DB_POSTGRESS"]

DB_URL = f"{infos_db['driver']}://{infos_db['user']}:{infos_db['password']}@{infos_db['host']}:{infos_db['port']}/{infos_db['database']}"
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()