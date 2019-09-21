from flask import jsonify, redirect
from json_utils import JUtil
import os

REFERRALS  = "referral-links.json"
REFERRAL_URL = "url"

jsonUtils = JUtil()

# Cleaner look for the referrals code, keeping it all in one place

class ReferralManager:
    # Sends a JSON response to the browser
    def get_referral(self):
        referrals = jsonUtils.parse_json_file(REFERRALS)
        return jsonify(referrals)

    # Retrieves the link for a given referral_name
    def get_referral_link(self, referral_name):
        referrals = jsonUtils.parse_json_file(REFERRALS)
        return referrals[referral_name][REFERRAL_URL]

    # Adds referral URLs received from partner companies
    def add_referral(self, referral_name, referral_url):
        referrals = jsonUtils.parse_json_file(REFERRALS)

        if referrals.get(referral_name) is None:
            referrals[referral_name] = {}
        referrals[referral_name][REFERRAL_URL] = referral_url

        jsonUtils.write_json_file(referrals, REFERRALS)

        return "i have the power of god and anime on my side"

    # Removes a game from the database
    def remove_referral(self, referral_name, referral_url):
        referrals = jsonUtils.parse_json_file(REFERRALS)

        if referral_name in referrals:
            del referrals[referral_name]

        jsonUtils.write_json_file(referrals, REFERRALS)

        return "ahhhhhhhhhhhhhhhhhhhhhh"

    def redirect_referral_link(self, referral_name):
        referrals = jsonUtils.parse_json_file(REFERRALS)
        link = referrals[referral_name][REFERRAL_URL]
        return redirect(link)
