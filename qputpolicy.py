#coding=utf-8
from time import time
import copy
import json


class PutPolicy(object):
    def __init__(self, scope, expires=3600):
        self.scope = scope
        self.expires = expires
        return

    def data(self):
        self.deadline = int(time()) + self.expires
        b = copy.deepcopy(self.__dict__)
        if "expires" in b:
            del b["expires"]
        return json.dumps(b)

    def __setattr__(self, key, value):
        if key != "data":
            self.__dict__[key] = value
            return

    def __str__(self):
        return self.data()