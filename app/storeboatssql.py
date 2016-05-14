# -*- coding: utf-8 -*-
import json
from app import models
# from flask import jsonify


class Store():
    def __init__(self):
        self.errors = ""
        self.boatsjson = {}
        self.test = "ttt"
        self.insea = 0
        self.notinsea = 0
        self.boatsoutsql = []

    def loadboatssql(self):
        try:
            boatssql = models.Boats.query.all()
        except Exception as e:
            self.errors = "Error loading boats from database: " + str(e)
            return self.errors
        for b in boatssql:
            self.boatsoutsql.append({"pier": b.pier, "name": b.name, "number": b.number, "license": b.license, "sea": b.sea})
        self.boatsjson[0] = self.boatsoutsql
        for s in self.boatsoutsql:  # Считаем кто в море, кто нет
            if s["sea"] == True:
                self.insea = self.insea + 1
            else:
                self.notinsea = self.notinsea + 1
        self.boatsjson[1] = {"insea": self.insea, "notinsea": self.notinsea}

    def saveboatssql(self, data):
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
                print("TRue true!!")
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
