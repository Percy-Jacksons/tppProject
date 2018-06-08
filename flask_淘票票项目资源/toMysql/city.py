# -*- coding:utf-8 -*-
import json
import pymysql

def readJsonFile(path):
    with open(path, "rb") as f:
        data = json.load(f)
        return data


arr = readJsonFile("city.json")


# db = pymysql.connect("127.0.0.1", "root", "rock1204", "movie")
# cursor = db.cursor()

# for item in arr:
#     print(item)
#     break



