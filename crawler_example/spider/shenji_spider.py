'''
time: 2022.5.4
author: 刘帅康
'''
import requests
import os
from lxml import etree
import csv
from contextlib import closing
# href="/service/zcfzb_000002.html"

# http://quotes.money.163.com/f10/zcfzb_000002.html#01c05/service/zcfzb_000002.html


# http://quotes.money.163.com/service/zcfzb_000002.html

# 主要财务指标
# http://quotes.money.163.com/service/zycwzb_000002.html?type=report

# 财务报表摘要
# http://quotes.money.163.com/service/cwbbzy_000002.html

# 资产负债表
# http://quotes.money.163.com/service/zcfzb_000002.html

# 利润表
# http://quotes.money.163.com/service/lrb_000002.html

# 现金流量表
# http://quotes.money.163.com/service/xjllb_000002.html

# 历史交易数据
# http://quotes.money.163.com/trade/lsjysj_000002.html

# 成交明细
# http://quotes.money.163.com/cjmx/2022/20220429/1000002.xls





def save_csv(outpath_name,url):

    with open(outpath_name,'wb') as f:
        csv_ = requests.get(url).content
        f.write(csv_)

def read_():
    path1 = '../shenji_data/A股房地产上证主板.txt'
    path2 = '../shenji_data/A股房地产深圳主板.txt'

    A_list = []
    with open(path1,'r',encoding='utf-8') as f:
        line = f.readline()
        mm = 1
        while line:
            lis = list(line.split('\n'))[0]
            A_list.append(list(lis.split(' ')))
            line = f.readline()
            mm += 1
            #if mm >5:
            #    break

    with open(path2,'r',encoding='utf-8') as f:
        line = f.readline()
        while line:
            lis = list(line.split('\n'))[0]
            A_list.append(list(lis.split(' ')))
            line = f.readline()

    return A_list


def main():

    item1 = ['财务报表摘要','资产负债表','利润表','现金流量表','历史交易数据']
    item2 = ['cwbbzy_','zcfzb_','lrb_','xjllb_','lsjysj_','']

    print('加载股票代码...')
    print('*'*24)
    A_name_list = read_()

    print('开始逐个下载...')
    print('*'*24)
    for item in A_name_list:
        mkdir_path = "../shenji_data/"+str(item[0])+str(item[1])+'/'
        if not os.path.exists(mkdir_path):
            os.mkdir(mkdir_path)
        print('已经创建：['+str(item[0])+str(item[1])+']的文件夹...')
        print('下载主要财务指标...')
        url = 'http://quotes.money.163.com/service/zycwzb_'+str(item[1])+'.html?type=report'
        save_csv(mkdir_path+'主要财务指标'+str(item[1])+'.csv', url)

        for i in range(len(item1)):
            print('下载'+str(item1[i])+'...')
            url = 'http://quotes.money.163.com/service/'+ str(item2[i]) + str(item[1]) + '.html'
            save_csv(mkdir_path + str(item1[i]) + str(item[1]) + '.csv', url)

        print(str(item[0])+str(item[1])+'> 的财务表格已经下载完成...')
        print('*>'*12)



if __name__ == '__main__':
    main()



