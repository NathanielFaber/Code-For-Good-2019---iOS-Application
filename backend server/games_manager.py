from flask import jsonify
from json_utils import JUtil

GAMES_PATH = "games.json"
GAMES_URL_KEYWORD = 'url'
GAMES_USAGE_KEYWORD = 'usage'
GAMES_AGE_KEYWORD = 'age'

jsonUtils = JUtil()

# Helps manage the games.json file
class GameManager:
    def get_games(self):
        # Retrieves a dictionary of games in the database
        games = jsonUtils.parse_json_file(GAMES_PATH)
        return jsonify(games)

    def get_game_link(self, game_name):
        # Retrieves the link for a given game_name
        games = jsonUtils.parse_json_file(GAMES_PATH)
        return games[game_name][GAMES_URL_KEYWORD]

    def remove_game(self, game_name):
        # Removes a game from the database
        games = jsonUtils.parse_json_file(GAMES_PATH)

        if game_name in games:
            del games[game_name]

        jsonUtils.write_json_file(games, GAMES_PATH)

        return "VErryYYy GooOd"

    def add_game(self, game_name, game_url, age):
        # Adds or updates a game to the json file
        games = jsonUtils.parse_json_file(GAMES_PATH)

        if games.get(game_name) is None:
            games[game_name] = {}
        games[game_name][GAMES_URL_KEYWORD] = game_url
        games[game_name][GAMES_AGE_KEYWORD] = age
        games[game_name][GAMES_USAGE_KEYWORD] = "0"

        jsonUtils.write_json_file(games, GAMES_PATH)

        return "VEry GOOD"

    def update_usage_statistic(self, game_name, usage_time):
        # Adds to the usage time of a given game
        games = jsonUtils.parse_json_file(GAMES_PATH)

        if games.get(game_name) is None:
            return "VeRryY BAaaAd"

        current_usage = int(games[game_name][GAMES_USAGE_KEYWORD])
        current_usage += int(usage_time)
        games[game_name][GAMES_USAGE_KEYWORD] = str(current_usage)

        jsonUtils.write_json_file(games, GAMES_PATH)

        return "VeRrrY GooDO"

    def get_usage_statistic(self, game_name):
        # Returns the usage time of a given game
        games = jsonUtils.parse_json_file(GAMES_PATH)

        if games.get(game_name) is None:
            return
        return games[game_name][GAMES_USAGE_KEYWORD]

    def get_age_range(self, game_name):
        # Returns the age range of a given game
        games = jsonUtils.parse_json_file(GAMES_PATH)

        if games.get(game_name) is None:
            return
        return games[game_name][GAMES_AGE_KEYWORD]

    def set_age_range(self, game_name, age):
        # Sets the age range of a given game
        games = jsonUtils.parse_json_file(GAMES_PATH)

        if games.get(game_name) is None:
            return
        games[game_name][GAMES_AGE_KEYWORD] = age
        
        jsonUtils.write_json_file(games, GAMES_PATH)

        return 'VeRy GooD'