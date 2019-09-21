from flask import Flask, jsonify
import json

app = Flask(__name__)

REFERRALS  = "referral-links.json"
REFERRAL_URL = "url"

def parse_json_file(path):
    return json.load(open(path))

@app.route('/referrals')
def parse():
    # Sends a JSON response to the browser
    referrals = parse_json_file(REFERRALS)
    return jsonify(referrals)

@app.route('/referrals/get/<referral_name>')
def get_referral_link(referral_name):
    # Retrieves the link for a given referral_name
    referrals = parse_json_file(REFERRALS)
    return referrals[referral_name][REFERRAL_URL]

if __name__ == '__main__':
    app.run()
