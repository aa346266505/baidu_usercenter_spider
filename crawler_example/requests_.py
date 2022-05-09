import requests
from lxml import etree
import json
# 将HTML转化为Element对象，Element对象具有xpath方法
def test1():

    url = 'http://a.xueshu.baidu.com/scholarID/CN-B875NK0J'
    # 模拟浏览器发送请求
    response = requests.get(url)

    # 此时返回的是状态码
    # response.status_code
    # 获取网页内容
    content = response.text
    html = response.content.decode()
    html = etree.HTML(html)

    ScholarID = html.xpath("//span[@class='p_scholarID_id']/text()")
    name = html.xpath("//div[@class='p_name']/text()")

    p_volume = html.xpath("//div[@class='p_volume']/text()")
    # 工作单位
    affiliate = html.xpath("//div[@class='p_affiliate']/text()")
    # 被引频次
    ach_num1 = html.xpath("//ul[@class='p_ach_wr']/li[1]/p[@class='p_ach_num']/text()")
    # 成果数目
    ach_num2 = html.xpath("//ul[@class='p_ach_wr']/li[2]/p[@class='p_ach_num']/text()")
    # H指数
    ach_num3 = html.xpath("//ul[@class='p_ach_wr']/li[3]/p[@class='p_ach_num']/text()")
    # G指数
    ach_num4 = html.xpath("//ul[@class='p_ach_wr']/li[4]/p[@class='p_ach_num']/text()")
    # 研究领域
    domain = html.xpath("//span[@class='person_domain person_text']/a/text()")

    # 论文发表数目--期刊：北大核心  CSCD   中国科技   EI    SCIE   其他期刊
    beida = html.xpath("//div[@class='pieBox journalBox']/p[1]/span[@class='boxnum']/text()")
    CSCD = html.xpath("//div[@class='pieBox journalBox']/p[2]/span[@class='boxnum']/text()")
    china_keji = html.xpath("//div[@class='pieBox journalBox']/p[3]/span[@class='boxnum']/text()")
    EI = html.xpath("//div[@class='pieBox journalBox']/p[4]/span[@class='boxnum']/text()")
    SCIE = html.xpath("//div[@class='pieBox journalBox']/p[5]/span[@class='boxnum']/text()")
    other = html.xpath("//div[@class='pieBox journalBox']/p[6]/span[@class='boxnum']/text()")

    # 论文发表数目--会议
    huiyi = html.xpath("//div[@class='pieBox conferenceBox']/p/span[@class='boxnum']/text()")

    # 成果数目--专著  百分比
    zhuanzhu_percent = html.xpath("//div[@class='pieBox booktitleBox']/h3/span[@class='boxPercent']/text()")
    zhuanzhu = html.xpath("//div[@class='pieBox booktitleBox']/h3/span[@class='boxNumber']/text()")

    # 其他成果
    other_ = html.xpath("//div[@class='pieBox otherBox']/h3/span[@class='boxNumber']/text()")
    other_percent = html.xpath("//div[@class='pieBox otherBox']/h3/span[@class='boxPercent']/text()")
    # 获取html结构的网址


    # 获取网页headers
    header = response.headers

    #response_new = requests.get(url,headers = header)

    print(html)

#test1()


def test2():

    #url = "http://a.xueshu.baidu.com/usercenter/data/authorchannel?cmd=inject_page&author=%E5%AD%99%E4%B9%90&affiliate="
    #url = "http://a.xueshu.baidu.com/usercenter/data/authorchannel?cmd=inject_page&author=%E5%AD%99%E4%B9%90&affiliate="
    url = "http://a.xueshu.baidu.com/usercenter/data/authorchannel?cmd=search_author&_token=34946211c992deeef352eba84ca6377ebe9307067c8e17a1465df7a87670c3bc&_ts=1651571037&_sign=2f0425c17ef6baf393a8ac6d3ae5a9dd&author=张仰森&affiliate=&curPageNum=1"
    # 模拟浏览器发送请求
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}
    response = requests.get(url)

    dic = json.loads(response.content)

    # 此时返回的是状态码
    # response.status_code
    # 获取网页内容

    html_new = dic['htmldata']
    html_new = etree.HTML(html_new)
    print(html_new)
    content = response.text
    #html = response.content.decode()
    #print(html)
    #html = etree.HTML(html)

    #next_url = html.xpath("//div[@class='searchResult_text']/a@href")
    name = html_new.xpath("//div[@class='searchResult_text']/a/text()")
    adrre = html_new.xpath("//div[@class='searchResult_text']/p/text()")
    href = html_new.xpath("//a[@class='searchResult_take']/@href")
    #adress = html.xpath("//div[@id='personalSearch_result']/div/div/p/text()")

    #name = html.xpath("//a[@class='personName']/text()")


    mm = 1

test2()