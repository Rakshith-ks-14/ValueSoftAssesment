import datetime
import re

from utility.Paths import Paths
import json

class ReadJson:

    def __read_json_file(self):
        file_path = list(Paths.get_file_path('configs', 'json'))[0]
        with open(file=file_path, mode='r') as file:
            data = json.loads(file.read())
        return data

    def get_data(self, key_name):
        json_data = self.__read_json_file()
        return json_data[key_name]

print(re.sub(r'-|:| ', '_', str(datetime.datetime.now().replace(microsecond=0))))