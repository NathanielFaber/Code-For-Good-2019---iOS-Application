from flask import jsonify
from json_utils import JUtil
import time

PASSW_PATH = "password.json"
PASSW = "password"
PASSW_TIMEOFCHANGE = "timeofchange"
PASSW_TIMEDIFF = "timediff"


jsonUtils = JUtil()

class PasswordManager:
    def get_pass(self):
        # Retrieves the current parent password
        password = jsonUtils.parse_json_file(PASSW_PATH)
        return jsonify(password)

    def change_pass(self, new_pass):
        # Grab current password data
        currentlist = jsonUtils.parse_json_file(PASSW_PATH)
        currentlist['password'] = new_pass  # change
        currentlist['timeofchange'] = time.gmtime() # reset time since last change

        jsonUtils.write_json_file(currentlist, PASSW_PATH)

        return "New Password set to " + currentlist['password']

    def get_time_diff(self):
        #calculates the time since the last time the password was changed
        currentlist = jsonUtils.parse_json_file(PASSW_PATH)
        oldtime = currentlist['timeofchange']
        # newtime = time.time()
        # currentlist['timediff'] = newtime - oldtime
        res = time.strftime("%c", oldtime) # convert to a readable time format
        return res
