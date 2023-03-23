# lichess_db_project
Personal side project for a full stack attempt at Database project

1. What is Lichess?

Lichess is a free, open-source chess server that allows users to play chess games online. It offers a variety of game modes, including casual games, rated games, and tournaments, as well as analysis tools and a community of players. Lichess is popular among both casual and competitive players, and it has a large and active user base.

2. What is a PGN?

PGN stands for Portable Game Notation, and it is a standard format for recording chess games. PGN files can be used to record games played online, in-person, or in chess software, and they can be easily shared and analyzed. PGN files contain information about the moves played, the players, the date and location of the game, and other metadata. PGN files can be opened and analyzed in many chess software programs, as well as online tools. The PGN I used can be found [here](https://database.lichess.org/).

3. This is the naive ERD I came up with for the database, it still needs to add more complexity, but for now I think it is decently complicated.

![ERD Diagram]('./LichessERD.png')


3. How to run the code?

To run the Lichess database code, you will need to have Python 3 installed on your computer, as well as Flask and SQLAlchemy libraries. Once you have these installed, you can clone the repository to your local machine and navigate to the root directory. Then in order to install the dependenceis you can do the follwing.

```git clone --recursive git@github.com:zen1405/lichess_db_project.git```


```pip install -r requirements.txt```

After you have run the aboe command you can run the codes.
To run the code, you can execute the following command in your terminal:

```python3 model_creator.py ```


This will create the database in a new directory instance. If you want to erase the database, you can do so by running

```python3 model_reset.py```

In order to interact with the database, you can run the following command

```python3 start.py```

This will start the Flask application, and you can then access it in your web browser at http://localhost:5000/. From there, you can use the API endpoints to retrieve and manipulate data from the Lichess database. You can modify the front end for each of the queries by modifying or creating new files in templates directory.

This is still a work in progress repo, but if you have any question, please create a pull request.
