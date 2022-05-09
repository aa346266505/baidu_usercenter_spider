'''
time: 2022.5.4
author: 刘帅康（梓轩）
'''

import csv
import json
import xlrd
import pandas as pd
from utils.config import Config

def read_xlsx():
    '''
    读取xlsx文件
    '''
    pass

def read_csv():
    '''
    读取sv文件
    '''
    path = '../data/expert.csv'
    with open(path,'r',encoding='utf-8') as f:
        lines = csv.reader(f,skipinitialspace=True)
        return lines

def read_txt():
    path = Config.read_path
    with open(path, 'r', encoding='utf-8') as f:
        results = []
        line = f.readline()
        line = f.readline()
        mm = 0
        while line:
            lis = list(line.split('\n'))[0]

            results.append(list(lis.split('\t')))
            line = f.readline()
            mm += 1
            if mm > 100:
                break

    return results

read_txt()

