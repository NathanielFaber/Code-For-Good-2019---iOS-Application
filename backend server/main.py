from json_utils import JUtil
from games_manager import GameManager
from password_manager import PasswordManager
from flask import Flask, jsonify, redirect
import json
import time
import os

app = Flask(__name__)

jsonUtils = JUtil()
gamesManager = GameManager()
passwordManager = PasswordManager()

REFERRALS  = "referral-links.json"
REFERRAL_URL = "url"
PASSW_PATH = "password.json"

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
    currentlist = jsonUtils.parse_json_file(PASSW_PATH)
    currentlist['password'] = new_pass
    currentlist['timeofchange'] = time.time()

    jsonUtils.write_json_file(currentlist, PASSW_PATH)

    return "New Password set to " + currentlist['password']

@app.route('/parentpassword/time/')
def get_time_diff():
    currentlist = jsonUtils.parse_json_file(PASSW_PATH)
    oldtime = currentlist['timeofchange']
    newtime = time.time()
    currentlist['timediff'] = newtime-oldtime

    jsonUtils.write_json_file(currentlist, PASSW_PATH)

    return "Time Diff is " + currentlist['timediff']
####


@app.route('/games')
def get_games():
    # Retrieves a dictionary of games in the database
    return gamesManager.get_games()

@app.route('/games/get/<game_name>')
def get_game_link(game_name):
    # Retrieves the link for a given game_name
    return gamesManager.get_game_link(game_name)

@app.route('/games/remove/<game_name>')
def remove_game(game_name):
    # Removes a game from the database
    return gamesManager.remove_game(game_name)

@app.route('/games/add/<game_name>/<game_url>')
def add_game(game_name, game_url):
    # Adds or updates a game to the json file
    return gamesManager.add_game(game_name, game_url)

@app.route('/games/update/<game_name>/<usage_time>')
def update_usage_statistic(game_name, usage_time):
    # Adds to the usage time of a given game
    return gamesManager.update_usage_statistic(game_name, usage_time)

@app.route('/games/stats/<game_name>')
def get_usage_statistic(game_name):
    # Returns the usage time of a given game
    return gamesManager.get_usage_statistic(game_name)

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

@app.route('/referrals/redirect/<referral_name>')
def redirect_referral_link(referral_name):
    referrals = parse_json_file(REFERRALS)
    link = referrals[referral_name][REFERRAL_URL]
    return redirect(link)

# Overwrites a json file with the given dictionary
def write_json_file(data, path):
    with open(path, "w") as write_file:
        json.dump(data, write_file)

if __name__ == '__main__':
    app.run()
