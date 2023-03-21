from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import chess.pgn
import pry
import json
# from helper_functions import convert_sec_to_min, compareTime, pretty_print
from tabulate import tabulate
# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)

class Players(db.Model):
    # headers = ['Name', 'Elo', 'Title', 'Last Active Date', 'Last Active Time']

    name = db.Column(db.String(255), primary_key = True)
    player_elo = db.Column(db.Integer)
    title = db.Column(db.String(255), nullable = True)
    last_active_date = db.Column(db.String)
    last_active_time = db.Column(db.String)

    def __repr__(self):
        table = {
            'Name': self.name,
            'Player Elo': self.player_elo,
            'Title': self.title,
            'Last Active Date': self.last_active_date,
            'Last Active Time': self.last_active_time
            }

        # return tabulate(table, headers=self.headers)
        return table
        # return f'Player: {self.name}, Elo: {self.player_elo}, Title: {self.title}, Last active date, time: {self.last_active_date},  {self.last_active_time}'

class Event(db.Model):

    event_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    event_type = db.Column(db.Enum('Game', 'Tournament'), nullable = False)
    date = db.Column(db.String)
    tournament_url = db.Column(db.String(2048), nullable = True)

    def __repr__(self) -> str:
        return f'Event {self.name}'

class Game(db.Model):
    lichess_url = db.Column(db.String(2048), primary_key = True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.event_id'))
    white_player_name = db.Column(db.Integer, db.ForeignKey('players.name'))
    black_player_name = db.Column(db.Integer, db.ForeignKey('players.name'))
    result = db.Column(db.String(255))
    white_rating_diff = db.Column(db.Integer)
    black_rating_diff = db.Column(db.Integer)
    eco = db.Column(db.String(255))
    opening = db.Column(db.String(255))
    termination = db.Column(db.String(255))
    time_control = db.Column(db.String(255))
    utc_date = db.Column(db.String)
    utc_time = db.Column(db.String)

    event = db.relationship('Event', backref = 'games')
    white_player = db.relationship('Players', foreign_keys = [white_player_name], backref = 'games_as_white')
    black_player = db.relationship('Players', foreign_keys = [black_player_name], backref = 'games_as_black')

    def __repr__(self) -> str:
        return f'Game {self.game_id}'

class Moves(db.Model):

    move_num = db.Column(db.Integer, primary_key = True)
    lichess_url = db.Column(db.String(2048), db.ForeignKey('game.lichess_url'), primary_key = True)
    white_move = db.Column(db.String)
    black_move = db.Column(db.String, nullable = True)

    game = db.relationship('Game', foreign_keys = [lichess_url], backref = 'move_detail')

    def __repr__(self) -> str:
        return f'Move_num {self.move_num}'


