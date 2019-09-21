from flask import jsonify
from json_utils import JUtil
from datetime import date
import datetime
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
        currentlist['timeofchange'] = time.time() # reset time since last change
    #    return str(currentlist['timeofchange'])
        jsonUtils.write_json_file(currentlist, PASSW_PATH)

        return "New Password set to " + currentlist['password']

    def get_time_diff(self):
        #calculates the time since the last time the password was changed
        currentlist = jsonUtils.parse_json_file(PASSW_PATH)
        oldtime = currentlist['timeofchange']
        # convert from num to date string
        #res = str(oldtime[1]) + "/" + str(oldtime[2]) + "/" + str(oldtime[0])
        # [2019, 9, 21, 13, 7, 35, 5, 264, 0]

        # newtime = time.time()
        # currentlist['timediff'] = newtime - oldtime
        #res = time.strftime("%c", res) # convert to a readable time format
        # return oldtime
        return datetime.datetime.fromtimestamp(oldtime).strftime('%c')
