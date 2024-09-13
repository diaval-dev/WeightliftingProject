import os
from dotenv import load_dotenv

load_dotenv()

# Database
DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_PASS = os.getenv("DATABASE_PASS")
DATABASE_PORT = os.getenv("DATABASE_PORT")

TIME_ZONE = os.getenv("TIME_ZONE")


APP_NAME = os.getenv("APP_NAME")
APP_VERSION = os.getenv("APP_VERSION")

