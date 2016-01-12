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
            fileboats = open("data/data.json", 'r')
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

    def saveboats(self, data):
        jsdata = json.loads(data)
        for s in jsdata:  # Считаем кто в море, кто нет
            if s["sea"] == True:
                self.insea = self.insea + 1
            else:
                self.notinsea = self.notinsea + 1
        ss = '{"insea":' + str(self.insea) + ', "notinsea":' + str(self.notinsea) + '}'
        data = '[' + data + ',' + ss + ']'
        jsondata = json.loads(data)
        try:
            # fileboats = io.open("data/data.json", 'w', encoding="utf-8")
            fileboats = open("data/data.json", 'w')
        except Exception as e:
            self.errors = "Error loading boats file: " + e
            return self.errors
        try:
            json.dump(jsondata, fileboats)
        except Exception as e:
            print("Error dump json:" + str(e))
