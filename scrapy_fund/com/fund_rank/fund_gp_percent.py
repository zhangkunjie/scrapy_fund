# -*- coding:utf8 -*-
import re
import time
import urllib.request
import pymysql
import demjson
from bs4 import BeautifulSoup

from scrapy_fund.com.constant import constant
from scrapy_fund.com.utils import utils

# 通过传入的地址参数获取接口数据
def get_data_array(url):
    header={
      'Referer':'http: // fund.eastmoney.com / data / fundranking.html',
      'Host':'fund.eastmoney.com' ,
      'Cookie':'em_hq_fls=js; HAList=d-hk-00690%2Cd-hk-00699%2Cf-0-000001-%u4E0A%u8BC1%u6307%u6570%2Cf-0-399001-%u6DF1%u8BC1%u6210%u6307; qgqp_b_id=c7bba1151846a1d5594336a9208f04ba; intellpositionL=1152px; intellpositionT=1003px; searchbar_code=270023; EMFUND0=null; EMFUND1=null; EMFUND2=null; EMFUND3=null; EMFUND4=null; EMFUND5=null; EMFUND6=null; EMFUND7=null; EMFUND8=08-05%2009%3A56%3A57@%23%24%u5E7F%u53D1%u5168%u7403%u7CBE%u9009%u80A1%u7968%28QDII%29@%23%24270023; EMFUND9=08-27 11:25:49@#$%u94F6%u6CB3%u521B%u65B0%u6210%u957F%u6DF7%u5408@%23%24519674; st_si=90406282820242; st_sn=11; st_psi=20200911183051235-0-6987461032; st_asi=delete; ASP.NET_SessionId=vqc34jhjjm1kytmpub1zn55k; _adsame_fullscreen_18186=1; st_pvi=65835005885084; st_sp=2020-02-10%2021%3A29%3A17; st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Fs'
    }
    req = urllib.request.Request(url,headers=header)
    response = urllib.request.urlopen(req)
    content = response.read()
    content = content.decode('utf-8')
    return  content
def get_fund_gp_percent(fund_id,fund_name):
    gp_list=[]
    fund_scale=0
    fund_detail_url="http://fund.eastmoney.com/"+fund_id+".html"
    fund_detail_html=get_data_array(fund_detail_url)
    soup = BeautifulSoup(fund_detail_html, 'lxml')
    fund_scale_info = soup.select("div.infoOfFund>table>tr>td")[1].text
    #基金规模
    fund_scale_re = re.search(r'([0-9]+(\.[0-9]+)?)', fund_scale_info, re.M | re.I)
    if fund_scale_re:
        fund_scale=fund_scale_re.group()
    #股票持仓
    gp_info_tr = soup.find('li',id='position_shares').select('div.poptableWrap>table.ui-table-hover>tr')[1:]
    if len(gp_info_tr)==10:
        for row in gp_info_tr:
            gp_name=row.contents[1].text
            gp_percent=str(row.contents[3].text).replace("%",'')
            gp_list.append([fund_id,fund_name,fund_scale,gp_name,gp_percent])
    return gp_list
def save():
    conn = pymysql.connect(host=constant.HOST, user=constant.USER, passwd=constant.PASSWORD, db=constant.DB,
                       port=constant.PORT, charset=constant.CHARSET)
    cur = conn.cursor()  # 获取一个游标
    #先查询出基金的id和url主页地址
    query_fund_info_sql=" select fund_id,fund_name from fund_ids"
    insert_fund_gp_percent_sql= " insert into fund_gp_percent (fund_id,fund_name,fund_scale,gp_name,gp_percent) values(%s,%s,%s,%s,%s)"
    try:
       cur.execute(query_fund_info_sql)
       fund_info_list=cur.fetchall()
       for fund_info in fund_info_list:
           #得到股票列表
           fund_id=fund_info[0]
           fund_name=fund_info[1]
           fund_gp_percent_list=get_fund_gp_percent(fund_id,fund_name)
           if fund_gp_percent_list!=[]:
              cur.executemany(insert_fund_gp_percent_sql, fund_gp_percent_list)
              conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
        print('插入失败')
    finally:
        cur.close()  # 关闭游标
        conn.close()  # 释放数据库资源
# 清空表
utils.truncate_table("fund_gp_percent")
save()
