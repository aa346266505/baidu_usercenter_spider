'''
time: 2022.5.4
author: 刘帅康
'''
import csv
import os
import requests
from lxml import etree
import pandas as pd
from utils.config import Config
from utils.utils import read_txt
import json

url_list = []
url_ori = 'http://a.xueshu.baidu.com'
def GET_data(html):
    '''
    已知html获取其中的数据
    '''
    html = etree.HTML(html)

    data = []

    ScholarID = html.xpath("//span[@class='p_scholarID_id']/text()")
    if len(ScholarID):
        data.append(str(ScholarID[0]))
    else:
        data.append('')

    name = html.xpath("//div[@class='p_name']/text()")
    if len(name):
        data.append(str(name[0]))
    else:
        data.append('')

    p_volume = html.xpath("//div[@class='p_volume']/text()")
    if len(p_volume):
        data.append(str(p_volume[0]))
    else:
        data.append('')

    # 工作单位
    affiliate = html.xpath("//div[@class='p_affiliate']/text()")
    if len(affiliate):
        data.append(str(affiliate[0]))
    else:
        data.append('')

    # 被引频次
    ach_num1 = html.xpath("//ul[@class='p_ach_wr']/li[1]/p[@class='p_ach_num']/text()")
    if len(ach_num1):
        data.append(str(ach_num1[0]))
    else:
        data.append('')
    # 成果数目
    ach_num2 = html.xpath("//ul[@class='p_ach_wr']/li[2]/p[@class='p_ach_num']/text()")
    if len(ach_num2):
        data.append(str(ach_num2[0]))
    else:
        data.append('')

    # H指数
    ach_num3 = html.xpath("//ul[@class='p_ach_wr']/li[3]/p[@class='p_ach_num']/text()")
    if len(ach_num3):
        data.append(str(ach_num3[0]))
    else:
        data.append('')

    # G指数
    ach_num4 = html.xpath("//ul[@class='p_ach_wr']/li[4]/p[@class='p_ach_num']/text()")
    if len(ach_num4):
        data.append(str(ach_num4[0]))
    else:
        data.append('')

    # 研究领域
    domain = html.xpath("//span[@class='person_domain person_text']/a/text()")
    if len(domain):
        data.append(str(domain[0]))
    else:
        data.append('')

    # 论文发表数目--期刊：北大核心  CSCD   中国科技   EI    SCIE   其他期刊
    beida = html.xpath("//div[@class='pieBox journalBox']/p[1]/span[@class='boxnum']/text()")
    if len(beida):
        data.append(str(beida[0]))
    else:
        data.append('')

    CSCD = html.xpath("//div[@class='pieBox journalBox']/p[2]/span[@class='boxnum']/text()")
    if len(CSCD):
        data.append(str(CSCD[0]))
    else:
        data.append('')

    china_keji = html.xpath("//div[@class='pieBox journalBox']/p[3]/span[@class='boxnum']/text()")
    if len(china_keji):
        data.append(str(china_keji[0]))
    else:
        data.append('')

    EI = html.xpath("//div[@class='pieBox journalBox']/p[4]/span[@class='boxnum']/text()")
    if len(EI):
        data.append(str(EI[0]))
    else:
        data.append('')

    SCIE = html.xpath("//div[@class='pieBox journalBox']/p[5]/span[@class='boxnum']/text()")
    if len(SCIE):
        data.append(str(SCIE[0]))
    else:
        data.append('')

    other = html.xpath("//div[@class='pieBox journalBox']/p[6]/span[@class='boxnum']/text()")
    if len(other):
        data.append(str(other[0]))
    else:
        data.append('')

    # 论文发表数目--会议
    huiyi = html.xpath("//div[@class='pieBox conferenceBox']/p/span[@class='boxnum']/text()")
    if len(huiyi):
        data.append(str(huiyi[0]))
    else:
        data.append('')

    # 成果数目--专著  百分比
    zhuanzhu_percent = html.xpath("//div[@class='pieBox booktitleBox']/h3/span[@class='boxPercent']/text()")
    if len(zhuanzhu_percent):
        data.append(str(zhuanzhu_percent[0]))
    else:
        data.append('')

    zhuanzhu = html.xpath("//div[@class='pieBox booktitleBox']/h3/span[@class='boxNumber']/text()")
    if len(zhuanzhu):
        data.append(str(zhuanzhu[0]))
    else:
        data.append('')

    # 其他成果
    other_ = html.xpath("//div[@class='pieBox otherBox']/h3/span[@class='boxNumber']/text()")
    if len(other_):
        data.append(str(other_[0]))
    else:
        data.append('')

    other_percent = html.xpath("//div[@class='pieBox otherBox']/h3/span[@class='boxPercent']/text()")
    if len(other_percent):
        data.append(str(other_percent[0]))
    else:
        data.append('')

    print('已经获取: [' + str(name[0]) + ']的相关数据...')

    return data


def init_csv():
    cloms = ['百度学者ID', '姓名', '访问量', '工作单位', '被引频次', '成果数目',
             'H指数', 'G指数', '研究领域', '北大核心', 'CSCD', '中国科技核心',
             'EI', 'SCIE', '其他期刊', '会议', '专著占比', '专著数目', '其他成果', '其他成果占比']
    df = pd.DataFrame(columns=cloms)
    df.to_csv(Config.output_path + 'baidu_expert.csv', mode='a', index=False)

def Save_Data(data):

    df = pd.DataFrame([data])
    df.to_csv(Config.output_path+'baidu_expert.csv',mode='a',index=False,header=False)
    print('已经保存: [' + str(data[1]) + ']的相关数据...')
    print('........')

def Make_Url(name,adrres):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}

    m = 1
    url = 'http://a.xueshu.baidu.com/usercenter/data/authorchannel?cmd=search_author&_token=34946211c992deeef352eba84ca6377ebe9307067c8e17a1465df7a87670c3bc&_ts=1651571037&_sign=2f0425c17ef6baf393a8ac6d3ae5a9dd&author='+name+'&affiliate='+adrres+'&curPageNum='+str(m)
    response = requests.get(url,headers = header)
    # <p class="tipWords">为您检索到如下结果：
    dic = json.loads(response.content)
    html_new = dic['htmldata']
    html_new = etree.HTML(html_new)
    title = html_new.xpath("//p[@class='tipWords']/text()")
    # p class="personInstitution color_666" title[0] == '为您检索到如下结果'：
    while len(title):
        name_ = html_new.xpath("//div[@class='searchResult_text']/a/text()")
        adrre = html_new.xpath("//div[@class='searchResult_text']/p/text()")
        href = html_new.xpath("//a[@class='searchResult_take']/@href")
        for i in range(len(name_)):
            if name_[i] == name and adrres in adrre[i]:
                url_list.append(str(url_ori+str(href[i])))
                print('正在处理: [' + name + ']的百度学者url...')
                response_ = requests.get(str(url_ori+str(href[i])), headers=header)
                html_ = response_.content.decode()
                data_ = GET_data(html_)
                Save_Data(data_)
        m += 1
        url = 'http://a.xueshu.baidu.com/usercenter/data/authorchannel?cmd=search_author&_token=34946211c992deeef352eba84ca6377ebe9307067c8e17a1465df7a87670c3bc&_ts=1651571037&_sign=2f0425c17ef6baf393a8ac6d3ae5a9dd&author=' + name + '&affiliate=' + adrres + '&curPageNum=' + str(
            m)
        response = requests.get(url,headers=header)
        # <p class="tipWords">为您检索到如下结果：
        dic = json.loads(response.content)
        html_new = dic['htmldata']
        html_new = etree.HTML(html_new)
        title = html_new.xpath("//p[@class='tipWords']/text()")


def main():
    expert_ = read_txt()
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}
    # 获取url_list
    print('生成百度学者url列表')
    for lis in expert_:
        Make_Url(lis[0],lis[1])
    print('生成完成')
    print('*'*12)
    print('获取数据并保存')
    for url in url_list:
        response = requests.get(url,headers = header)
        html = response.content.decode()
        data = GET_data(html)
        Save_Data(data)
    print('数据全部保存完成...')

# 边爬边保存
def main_():
    init_csv()
    expert_ = read_txt()

    # 获取url_list
    print('开始爬虫...')
    mmm = 1
    for lis in expert_:
        Make_Url(lis[0], lis[1])
        print('*'*24)
        percent = round((mmm*100)/len(expert_),2)

        print('当前进度：['+str(percent)+'%]....')
        print('*'*24)
        mmm += 1
    print('爬虫完成')
    print('*' * 12)
    print('数据已经全部保存...')


if __name__ == '__main__':
    main_()

