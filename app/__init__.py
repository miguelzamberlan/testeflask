"""Initialize app."""
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


"""Construct the core application."""
app = Flask(__name__)

# Application Configuration
app.config.from_object('config.Config')

db = SQLAlchemy(app)

# Import parts of our application
# BluePrints

from app.notes import notes_routes
app.register_blueprint(notes_routes.notes_blueprint)

