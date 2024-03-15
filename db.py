from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os


load_dotenv()


SQLALCHEMY_DATABASE_URL = os.getenv('BASE_URL')

# "postgresql://myuser:Snex20242025go@shop_bot_postgres_1:5432/bot_database"

engine = create_engine(SQLALCHEMY_DATABASE_URL)


Base = declarative_base()
