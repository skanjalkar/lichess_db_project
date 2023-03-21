from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import chess.pgn
import pry
from helper_functions import convert_sec_to_min, compareTime
from models import Players, Moves, Game, Event, db, app


with app.app_context():
    pgn = open("./../lichess_elite_2020-06.pgn")
    player_count = 1
    event_count = 1
    # while (True):
    for i in range(1000):
        game = chess.pgn.read_game(pgn)
        # if not game:
        #     print("------------------------DONE-------------------------")
        #     break
        event_name = game.headers["Event"]
        date = game.headers['Date']
        result = game.headers['Result']
        white = game.headers['White']
        white_elo = game.headers['WhiteElo']
        white_rating_diff = game.headers['WhiteRatingDiff'] if 'WhiteRatingDiff' in game.headers else 0
        white_title = game.headers['WhiteTitle'] if 'WhiteTitle' in game.headers else None
        black = game.headers['Black']
        black_elo = game.headers['BlackElo']
        black_rating_diff = game.headers['BlackRatingDiff'] if 'BlackRatingDiff' in game.headers else 0
        black_title = game.headers['BlackTitle'] if 'BlackTitle' in game.headers else None
        eco = game.headers['ECO']
        lichess_url = game.headers['LichessURL']
        opening = game.headers['Opening']
        termination = game.headers['Termination']
        utc_date = game.headers['UTCDate']
        utc_time = game.headers['UTCTime']
        time_control = game.headers['TimeControl']
        time_control = convert_sec_to_min(time_control)

        # check if player exists, if he does not then create one
        white_player = Players.query.filter_by(name=white).first()
        if not white_player:
            white_player = Players(name=white, player_elo=white_elo, title=white_title, last_active_date=utc_date, last_active_time=utc_time)
            db.session.add(white_player)

        if (compareTime(white_player.last_active_date, utc_date, white_player.last_active_time, utc_time)):
            white_player.last_active_date = utc_date
            white_player.last_active_time = utc_time
            white_player.player_elo = white_elo

        black_player = Players.query.filter_by(name=black).first()
        if not black_player:
            black_player = Players(name=black, player_elo=black_elo, title=black_title, last_active_date=utc_date, last_active_time=utc_time)
            db.session.add(black_player)

        if (compareTime(black_player.last_active_date, utc_date, black_player.last_active_time, utc_time)):
            black_player.last_active_date = utc_date
            black_player.last_active_time = utc_time
            black_player.player_elo = black_elo


        eventType = event_name.split()

        if (eventType[2] == 'tournament'):
            event_name = eventType[0] + eventType[1] + eventType[2]
            event = Event(event_id = event_count, name=event_name, event_type='Tournament', date=date, tournament_url=eventType[3])
        else:
            event = Event(event_id = event_count, name=event_name, event_type='Game', date=date)
        event_count += 1
        db.session.add(event)


        match = Game(
            lichess_url = lichess_url,
            event_id = event.event_id,
            white_player_name = white_player.name,
            black_player_name = black_player.name,
            result = result,
            white_rating_diff = white_rating_diff,
            black_rating_diff = black_rating_diff,
            eco = eco,
            termination = termination,
            opening = opening,
            time_control = time_control,
            utc_date = utc_date,
            utc_time = utc_time,
        )

        ## check time
        ### TODO Change move to accept white nad black, check for NULL as well ###
        game_moves = []
        board = game.board()

        for move in game.mainline_moves():
            san_move = board.san(move)
            game_moves.append(san_move)
            board.push(move)


        count = 1
        white_moves = game_moves[::2]
        black_moves = game_moves[1::2]
        for i in range(len(white_moves)):
            m = Moves(
                    move_num = i+1,
                    lichess_url = lichess_url,
                    white_move = white_moves[i],
                    black_move = black_moves[i] if i < len(black_moves) else None
                )

            db.session.add(m)

        db.session.add(match)
        db.session.commit()
