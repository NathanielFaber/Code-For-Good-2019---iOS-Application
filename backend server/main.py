from flask import Flask, jsonify
from json_utils import JUtil
import json
import time
app = Flask(__name__)

jsonUtils = JUtil()

REFERRALS  = "referral-links.json"
REFERRAL_URL = "url"
GAMES_PATH = "games.json"
PASSW_PATH = "password.json"
GAMES_URL_KEYWORD = 'url'
GAMES_USAGE_KEYWORD = 'usage'

# Returns a dictionary formatted by the json file
class parentPassword:
    def __init__(self,password,timeofchange):
        self.password = password
        self.timeofchange = timeofchange

#### Retrieve Password
@app.route('/parentpassword')
def get_pass():
    # Retrieves the current parent password
    password = jsonUtils.parse_json_file(PASSW_PATH)
    return jsonify(password)

@app.route('/parentpassword/change/<new_pass>')
def change_pass(new_pass):
    passtoAdd = parentPassword(new_pass, time.time())
    currentlist = jsonUtils.parse_json_file(PASSW_PATH)
    currentlist.append(passtoAdd)

    jsonUtils.write_json_file(currentlist, PASSW_PATH)

    return "New Password set to " + passtoAdd.password

####


@app.route('/games')
def get_games():
    # Retrieves a dictionary of games in the database
    games = jsonUtils.parse_json_file(GAMES_PATH)
    return jsonify(games)

@app.route('/games/get/<game_name>')
def get_game_link(game_name):
    # Retrieves the link for a given game_name
    games = jsonUtils.parse_json_file(GAMES_PATH)
    return games[game_name][GAMES_URL_KEYWORD]

@app.route('/games/remove/<game_name>')
def remove_game(game_name):
    # Removes a game from the database
    games = jsonUtils.parse_json_file(GAMES_PATH)

    if game_name in games:
        del games[game_name]

    jsonUtils.write_json_file(games, GAMES_PATH)

    return "VErryYYy GooOd"

@app.route('/games/add/<game_name>/<game_url>')
def add_game(game_name, game_url):
    # Adds or updates a game to the json file
    games = jsonUtils.parse_json_file(GAMES_PATH)

    if games.get(game_name) is None:
        games[game_name] = {}
    games[game_name][GAMES_URL_KEYWORD] = game_url
    games[game_name][GAMES_USAGE_KEYWORD] = "0"

    jsonUtils.write_json_file(games, GAMES_PATH)

    return "VEry GOOD"

@app.route('/games/update/<game_name>/<usage_time>')
def update_usage_statistic(game_name, usage_time):
    # Adds to the usage time of a given game
    games = jsonUtils.parse_json_file(GAMES_PATH)

    if games.get(game_name) is None:
        return "VeRryY BAaaAd"

    current_usage = int(games[game_name][GAMES_USAGE_KEYWORD])
    current_usage += int(usage_time)
    games[game_name][GAMES_USAGE_KEYWORD] = str(current_usage)

    jsonUtils.write_json_file(games, GAMES_PATH)

    return "VeRrrY GooDO"

@app.route('/games/stats/<game_name>')
def get_usage_statistic(game_name):
    # Returns the usage time of a given game
    games = jsonUtils.parse_json_file(GAMES_PATH)

    if games.get(game_name) is None:
        return
    return games[game_name][GAMES_USAGE_KEYWORD]

@app.route('/referrals')
def parse():
    # Sends a JSON response to the browser
    referrals = jsonUtils.parse_json_file(REFERRALS)
    return jsonify(referrals)

@app.route('/referrals/get/<referral_name>')
def get_referral_link(referral_name):
    # Retrieves the link for a given referral_name
    referrals = jsonUtils.parse_json_file(REFERRALS)
    return referrals[referral_name][REFERRAL_URL]

if __name__ == '__main__':
    app.run()
