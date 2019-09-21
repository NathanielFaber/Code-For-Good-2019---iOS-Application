from flask import jsonify
from json_utils import JUtil
import time

PASSW_PATH = "password.json"
PASSW = "password"
PASSW_TIMEOFCHANGE = "timeofchange"
PASSW_TIMEDIFF = "timediff"


jsonUtils = JUtil()

class parentPassword:
    def __init__(self,password,timeofchange):
        self.password = password
        self.timeofchange = timeofchange

    def get_pass(self):
        # Retrieves the current parent password
        password = jsonUtils.parse_json_file(PASSW_PATH)
        return jsonify(password)

    def change_pass(new_pass):
        passtoAdd = parentPassword(new_pass, time.time())
        currentlist = jsonUtils.parse_json_file(PASSW_PATH)
        currentlist.append(passtoAdd)

        jsonUtils.write_json_file(currentlist, PASSW_PATH)

        return "New Password set to " + passtoAdd.password