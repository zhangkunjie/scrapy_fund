# -*- coding:utf8 -*-
import urllib.request
import pymysql



# 获取的增长率为空转为0
from scrapy_fund.com.constant import constant
from scrapy_fund.com.utils import utils


def clean_data(data):
    if data == '':
        return '0'
    else:
        return "'" + data + "'"


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
    data_array = eval(content[content.index("["):content.index("]") + 1])
    return  data_array


def save_fund(data_array, category):
    conn = pymysql.connect(host=constant.HOST, user=constant.USER, passwd=constant.PASSWORD, db=constant.DB,
                           port=constant.PORT, charset=constant.CHARSET)
    cur = conn.cursor()  # 获取一个游标
    for datas in data_array:
        data = datas.split(",")
        fund_id = "'" + data[0] + "'"
        fund_name = "'" + data[1] + "'"
        fund_name_abbr = "'" + data[2] + "'"
        if data[3] == '':
            cal_date = clean_data('1900-01-01')
        else:
            cal_date = "'" + data[3] + "'"
        net_asset_value = clean_data(data[4])
        accumulative = clean_data(data[5])
        one_day = clean_data(data[6])
        one_week = clean_data(data[7])
        onemonth = clean_data(data[8])
        threemonth = clean_data(data[9])
        sixmonth = clean_data(data[10])
        oneyear = clean_data(data[11])
        twoyear = clean_data(data[12])
        threeyear = clean_data(data[13])
        thisyear = clean_data(data[14])
        setup = clean_data(data[15])
        score = 0
        insertSQL = " insert into fund_info(fund_id,fund_name,fund_name_abbr,cal_date,net_asset_value,accumulative,oneday,oneweek,onemonth,threemonth,sixmonth,oneyear,twoyear,threeyear,thisyear,setup,category,score) values(" + fund_id + "," + fund_name + "," + fund_name_abbr + "," + cal_date + "," + net_asset_value + "," + accumulative + "," + one_day + "," + one_week + "," + onemonth + "," + threemonth + "," + sixmonth + "," + oneyear + "," + twoyear + "," + threeyear + "," + thisyear + "," + setup + ",'" + category + "'," + str(
            score) + ")"
        print(insertSQL)
        cur.execute(insertSQL)
        conn.commit()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源


# 开始组合函数
public_url = constant.FUNRRANK_URL
fund_category = constant.FUND_CATEGORY
# 清空表
utils.truncate_table("fund_rank")
# 插入抓取的数据
for category in fund_category:
    print(public_url)
    fund_url = public_url + category
    fund_array = get_fund_array(fund_url)
    save_fund(fund_array, category)
