import json
import requests

class TrainAPI:
    _url = "https://rti-giken.jp/fhc/api/train_tetsudo/delay.json"
    @classmethod
    def get_data(cls):
        res = requests.get(cls._url)
        if res.status_code == 200:
            dict_list = res.json()
        else:
            raise Exception(res.status_code)
        obj_list = TrainDataList()
        for data in dict_list:
             obj_list.append(TrainData(data["name"], data["company"], data["lastupdate_gmt"], data["source"]))
        return obj_list

class TrainData:
    def __init__(self, name, company, last_update_gmt, source):
        self.__name = name
        self.__company = company
        self.__last_update_gmt = last_update_gmt
        self.__source = source

    @property
    def name(self):
        return self.__name

    @property
    def company(self):
        return self.__company

    @property
    def last_update_gmt(self):
        return self.__last_update_gmt

    @property
    def source(self):
        return self.__source

    def to_dict(self):
        return {"name": self.__name, "company": self.__company, "last_update_gmt": self.last_update_gmt, "source": self.__source}

class TrainDataList:
    __data_list = []
    def __init__(self):
        self.__data_list = []

    @property
    def data_list(self):
        return self.__data_list

    def append(self, data):
        self.__data_list.append(data)

    def find_by_name(self, name):
        for data in self.__data_list:
            if data.name == name:
                return data
        return None

class TragetTrain:
    names = ["横浜線","小田原線"]
    @classmethod
    def get(cls):
        tmp_data = TrainAPI.get_data()
        return_data = []
        for name in cls.names:
            if tmp_data.find_by_name(name):
                return_data.append(tmp_data.find_by_name(name).to_dict())
        return return_data
