# -*- coding:UTF-8 -*-

import csv

class DataOutput():
    def __init__(self,data):
        self.data = data

    def data_to_txt(self,filename):
        with open(filename,'a+',newline = '') as f:
            f.write(self.data + '\n')
        return filename

    def data_to_csv(self,filename):
        with open(filename, 'w',newline='') as csvfile:
            writer = csv.writer(csvfile)            
            writer.writerow(self.data)