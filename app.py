from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask('Mentr')
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Skill

if __name__ == '__main__':
    app.run(debug=True, port=8080)
