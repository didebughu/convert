import json
from queue import Queue


class JsonFile(object):

    def __init__(self, file_name):
        self.file = file_name
        self.key = ""

    def __search_key(self, keys_list):
        for key in keys_list:
            if key == self.key:
                return True
        return False

    def get_value(self, key):
        if type(key) != str or key == "":
            return None
        self.key = key
        with open(self.file) as r:
            data = json.load(r)
        value = []
        if type(data) is list:
            data = data[0]
        if self.__search_key(data.keys()):
            value.append(data[self.key])
        q = Queue()
        q.put(data)
        while q.empty() is not True:
            temp_data = q.get()
            for temp_key in temp_data.keys():
                print(temp_key)
                if type(temp_data[temp_key]) is list:
                    if len(temp_data[temp_key]) != 0:
                        temp_dict = temp_data[temp_key][0]
                        print(temp_dict)
                        q.put(temp_dict)
                        if self.__search_key(temp_dict.keys()):
                            value.append(temp_dict[self.key])
                if type(temp_data[temp_key]) is dict:
                    print(temp_data[temp_key])
                    q.put(temp_data[temp_key])
                    if self.__search_key(temp_data[temp_key].keys()):
                        value.append(temp_data[temp_key][self.key])
        return value
