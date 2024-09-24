import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Get the PostgreSQL connection string from environment variables
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://<Spandan>:< atgs41UAZ*rK>@<clouddevops.postgres.database.azure.com>:5432/<database=postgres>")

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db = SQLAlchemy(app)
