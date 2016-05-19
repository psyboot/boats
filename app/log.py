# -*- coding: utf-8 -*-
import datetime


class Log():
    def __init__(self):
        pass

    def log(self, name, line):
        name_file = 'logs/' + name + '_' + str(datetime.datetime.now().strftime
                                               ('%y_%m_%d') + '.txt')
        print "*****: ", line
        try:
            lfile = open(name_file, 'a')
            lfile.write(line.encode('cp1251') + "\n")
            lfile.close()
        except Exception as e:
            print(str(e))
