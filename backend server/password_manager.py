from flask import jsonify
from json_utils import JUtil
import time

PASSW_PATH = "password.json"
PASSW = "password"
PASSW_TIMEOFCHANGE = "timeofchange"
PASSW_TIMEDIFF = "timediff"


jsonUtils = JUtil()

class PasswordManager:
    def __init__(self,password,timeofchange):
        self.password = password
        self.timeofchange = timeofchange

    def get_pass(self):
        # Retrieves the current parent password
        password = jsonUtils.parse_json_file(PASSW_PATH)
        return jsonify(password)

    def change_pass(self, new_pass):
        currentlist = jsonUtils.parse_json_file(PASSW_PATH)
        currentlist['password'] = new_pass
        currentlist['timeofchange'] = time.time()

        jsonUtils.write_json_file(currentlist, PASSW_PATH)

        return "New Password set to " + currentlist['password']

    def get_time_diff(self):
        currentlist = jsonUtils.parse_json_file(PASSW_PATH)
        oldtime = currentlist['timeofchange']
        newtime = time.time()
        currentlist['timediff'] = newtime - oldtime

        jsonUtils.write_json_file(currentlist, PASSW_PATH)

        return "Time Diff is " + currentlist['timediff']