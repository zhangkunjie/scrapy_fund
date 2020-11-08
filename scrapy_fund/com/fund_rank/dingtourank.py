# -*- coding:utf8 -*-
import urllib.request
import pymysql



# 获取的增长率为空转为0
from bs4 import BeautifulSoup
from scrapy_fund.com.constant import constant
from scrapy_fund.com.utils import utils


def   format_data(data,html,default_value):
      if data is None:
          return  default_value
      else:
         if  data.find(html) is None:
             return  default_value
         else:
             return  data.find(html).string.replace('%','')

# 通过传入的地址参数获取接口数据
def get_fund_array(url):
    header={
      'Referer':'http: // fund.eastmoney.com / data / fundranking.html',
      'Host':'fund.eastmoney.com' ,
      'Cookie':'em_hq_fls=js; HAList=d-hk-00690%2Cd-hk-00699%2Cf-0-000001-%u4E0A%u8BC1%u6307%u6570%2Cf-0-399001-%u6DF1%u8BC1%u6210%u6307; qgqp_b_id=c7bba1151846a1d5594336a9208f04ba; intellpositionL=1152px; intellpositionT=1003px; searchbar_code=270023; EMFUND0=null; EMFUND1=null; EMFUND2=null; EMFUND3=null; EMFUND4=null; EMFUND5=null; EMFUND6=null; EMFUND7=null; EMFUND8=08-05%2009%3A56%3A57@%23%24%u5E7F%u53D1%u5168%u7403%u7CBE%u9009%u80A1%u7968%28QDII%29@%23%24270023; EMFUND9=08-27 11:25:49@#$%u94F6%u6CB3%u521B%u65B0%u6210%u957F%u6DF7%u5408@%23%24519674; st_si=90406282820242; st_sn=11; st_psi=20200911183051235-0-6987461032; st_asi=delete; ASP.NET_SessionId=vqc34jhjjm1kytmpub1zn55k; _adsame_fullscreen_18186=1; st_pvi=65835005885084; st_sp=2020-02-10%2021%3A29%3A17; st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Fs'
    }
    #response = urllib.request.url(url,headers=header)
    req = urllib.request.Request(url,headers=header)
    response = urllib.request.urlopen(req)
    content = response.read()
    content = content.decode('utf-8')
    return  content


def save_fund(content, category):
    conn = pymysql.connect(host=constant.HOST, user=constant.USER, passwd=constant.PASSWORD, db=constant.DB,
                           port=constant.PORT, charset=constant.CHARSET)
    cur = conn.cursor()  # 获取一个游标
    insertSQL = " insert into dingtou_rank(fund_id,fund_name,net_asset_value,oneyear," \
                "twoyear,threeyear,fiveyear,grade_no,category) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    soup = BeautifulSoup(content, 'lxml')
    table = soup.table.tbody
    value_list = []
    for row in table:
        tds = row.findAll('td')
        fund_id=format_data(tds[2],'a',0)
        fund_name=format_data(tds[3],'a','')
        net_asset_value=format_data(tds[5],'span',0)
        oneyear=format_data(tds[7],'span',0)
        twoyear=format_data(tds[8],'span',0)
        threeyear=format_data(tds[9],'span',0)
        fiveyear=format_data(tds[10],'span',0)
        grade_no =format_data(tds[11],'span','0')
        if grade_no!=0:
           grade_no=str(len(grade_no))
        value_list.append((fund_id, fund_name, net_asset_value, oneyear, twoyear, threeyear, fiveyear, grade_no,category))
    try:
        #print(value_list)
        cur.executemany(insertSQL,value_list)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
        print('插入失败')
    finally:
     cur.close()  # 关闭游标
     conn.close()  # 释放数据库资源


# 开始组合函数
public_url = constant.DTRANK_URL
#fund_category = {'1':'gp','2':'hh','3':'zq','4':'zs','5':'qdii'}
fund_category = {'1':'gp','2':'hh','3':'zq','4':'zs','5':'qdii'}
# 清空表
utils.truncate_table("dingtou_rank")
# 插入抓取的数据
for category in fund_category:
    dingtou_url = public_url + category
    print(dingtou_url)
    fund_array = get_fund_array(dingtou_url)
    save_fund(fund_array, fund_category[category])
