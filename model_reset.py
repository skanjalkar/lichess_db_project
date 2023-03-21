from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import chess.pgn
import pry
from models import Players, Game, Moves, Event, db, app


with app.app_context():
    db.drop_all()
    db.create_all()