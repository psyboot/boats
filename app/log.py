# -*- coding: utf-8 -*-
import datetime
import glob, os


class Log():
    def __init__(self):
        self.filenames = {}

    def log(self, name, line):
        name_file = 'logs/' + name + '_' + str(datetime.datetime.now().strftime
                                               ('%y_%m_%d') + '.txt')
        print "*****: ", line
        try:
            lfile = open(name_file, 'a')
            lfile.write(line.encode('utf-8') + "\n")
            lfile.close()
        except Exception as e:
            print(str(e))

    def getlogs(self):
        files = glob.glob('logs/*.txt')
        for file in files:
            logf = open(file, 'r')
            logarr = logf.readlines()
            logf.close()
            logarru = [i.decode('utf-8') for i in logarr]
            self.filenames[os.path.basename(file).decode('utf-8')] = logarru
        return self.filenames
