from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

load_dotenv()
app = Flask(__name__)

CORS(app)
engine = create_engine(
    os.getenv("DATABASE_URL"),
    echo=True, plugins=["geoalchemy2"]
    )

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
