from flask import Flask
from config import  Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api, abort, reqparse
from flask_marshmallow import Marshmallow
import os
# from dotenv import load_dotenv
from flask_cors import CORS


app = Flask(__name__, static_folder="build", static_url_path='/', template_folder="build")
cors = CORS(app)
# load_dotenv()
app.config.from_object(Config)
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)
migrate = Migrate(app, db)
# app.secret_key = os.getenv('SECRET_KEY')

from app import routes, models



