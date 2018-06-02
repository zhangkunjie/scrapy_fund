# -*- coding:utf8 -*-
import urllib.request
import pymysql
from scrapy_fund.com.constant import constant


# 获取的增长率为空转为0
def clean_data(data):
    if data == '':
        return '0'
    else:
        return "'" + data + "'"


# 通过传入的地址参数获取接口数据
def get_fund_array(url):
    response = urllib.request.urlopen(url)
    content = response.read()
    content = content.decode('utf-8')
    data_array = eval(content[content.index("["):content.index("]") + 1])
    return data_array


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
        insertSQL = " insert into fund_rank(fund_id,fund_name,fund_name_abbr,cal_date,net_asset_value,accumulative,oneday,oneweek,onemonth,threemonth,sixmonth,oneyear,twoyear,threeyear,thisyear,setup,category,score) values(" + fund_id + "," + fund_name + "," + fund_name_abbr + "," + cal_date + "," + net_asset_value + "," + accumulative + "," + one_day + "," + one_week + "," + onemonth + "," + threemonth + "," + sixmonth + "," + oneyear + "," + twoyear + "," + threeyear + "," + thisyear + "," + setup + ",'" + category + "'," + str(
            score) + ")"
        print(insertSQL)
        cur.execute(insertSQL)
        conn.commit()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源


def truncate_table(table_name):
    conn = pymysql.connect(host=constant.HOST, user=constant.USER, passwd=constant.PASSWORD, db=constant.DB,
                           port=constant.PORT, charset=constant.CHARSET)
    truncateSQL = "truncate " + table_name;
    cur = conn.cursor()
    cur.execute(truncateSQL)
    conn.commit()
    cur.close()  # 关闭游标
    conn.close()  # 释放数据库资源


# 开始组合函数
public_url = constant.FUNRRANK_URL
fund_category = constant.FUND_CATEGORY
# 清空表
truncate_table("fund_rank")
# 插入抓取的数据
for category in fund_category:
    fund_url = public_url + category
    fund_array = get_fund_array(fund_url)
    save_fund(fund_array, category)
