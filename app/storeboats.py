# -*- coding: utf-8 -*-
import json
# from flask import jsonify


class Store():
    def __init__(self):
        self.errors = ""
        self.boatsjson = {}
        self.test = "ttt"
        self.insea = 0
        self.notinsea = 0

    def loadboats(self):
        try:
            fileboats = open("data/data.json")
        except Exception as e:
            self.errors = "Error loading boats file: " + e
            return self.errors
        self.boatsjson = json.load(fileboats)
        for s in self.boatsjson[0]:  # Считаем кто в море, кто нет
            if s["sea"] == True:
                self.insea = self.insea + 1
            else:
                self.notinsea = self.notinsea + 1
        self.boatsjson[1]["insea"] = self.insea
        self.boatsjson[1]["notinsea"] = self.notinsea
        print(self.boatsjson)

    def saveboats(self, data):
        jsondata = []
        jsdata = json.loads(data)
        for s in jsdata:  # Считаем кто в море, кто нет

            if s["sea"] == True:
                self.insea = self.insea + 1
            else:
                self.notinsea = self.notinsea + 1
        jsondata.append(jsdata)
        jsondata.append({"insea": self.insea, "notinsea": self.notinsea})
        print(type(data))
        try:
            fileboats = open("data/data.json", 'w')
        except Exception as e:
            self.errors = "Error loading boats file: " + e
            return self.errors
        json.dump(jsondata, fileboats, indent=4, encoding="utf-8")
