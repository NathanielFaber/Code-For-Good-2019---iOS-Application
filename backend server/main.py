from json_utils import JUtil
from games_manager import GameManager
from password_manager import PasswordManager
from referrals_manager import ReferralManager
from flask import Flask, jsonify, redirect

app = Flask(__name__)

jsonUtils = JUtil()
gamesManager = GameManager()
passwordManager = PasswordManager()
referralsManager = ReferralManager()

PASSW_PATH = "password.json"

#### Retrieve Password
@app.route('/parentpassword')
def get_pass():
    # Retrieves the current parent password
    return passwordManager.get_pass()

@app.route('/parentpassword/change/<new_pass>')
def change_pass(new_pass):
    # Changes the current password
    return passwordManager.change_pass(new_pass)

@app.route('/parentpassword/time/')
def get_time_diff():
    # Amount of time since you've changed your password
    return passwordManager.get_time_diff()
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

@app.route('/games/add/<game_name>/<game_url>/<game_age>')
def add_game(game_name, game_url, game_age):
    # Adds or updates a game to the json file
    return gamesManager.add_game(game_name, game_url, game_age)

@app.route('/games/update/<game_name>/<usage_time>')
def update_usage_statistic(game_name, usage_time):
    # Adds to the usage time of a given game
    return gamesManager.update_usage_statistic(game_name, usage_time)

@app.route('/games/stats/<game_name>')
def get_usage_statistic(game_name):
    # Returns the usage time of a given game
    return gamesManager.get_usage_statistic(game_name)

@app.route('/games/get/age/<game_name>')
def get_age_range(game_name):
    # Returns the age range of a given game
    return gamesManager.get_age_range(game_name)

@app.route('/games/set/age/<game_name>/<age>')
def set_age_range(game_name, age):
    # Sets the age of a given game
    return gamesManager.set_age_range(game_name, age)

@app.route('/referrals')
def get_referral():
    # Sends a JSON response to the browser
    return referralsManager.get_referral()

@app.route('/referrals/get/<referral_name>')
def get_referral_link(referral_name):
    # Retrieves the link for a given referral_name
    return referralsManager.get_referral_link(referral_name)

@app.route('/referrals/add/<referral_name>/<referral_url>')
def add_referral(referral_name, referral_url):
    # Adds referral URLs received from partner companies
    return referralsManager.add_referral(referral_name, referral_url)

@app.route('/referrals/remove/<referral_name>/<referral_url>')
def remove_referral(referral_name, referral_url):
    # Removes a game from the database
    return referralsManager.remove_referral(referral_name, referral_url)

@app.route('/referrals/redirect/<referral_name>')
def redirect_referral_link(referral_name):
    # Redirects the user to the given link
    return referralsManager.redirect(referral_name)

if __name__ == '__main__':
    app.run()
