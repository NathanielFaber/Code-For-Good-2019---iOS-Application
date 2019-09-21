import json

class JUtil:
    #### Retrieving referral URL data
    def parse_json_file(self, path):
        return json.load(open(path))

    # Overwrites a json file with the given dictionary
    def write_json_file(self, data, path):
        with open(path, "w") as write_file:
            json.dump(data, write_file)
