from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_cors import CORS

app =Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)



from app import routes ,models
from app.models import users_models, notes_models