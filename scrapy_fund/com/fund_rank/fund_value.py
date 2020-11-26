import json
import time
import urllib.request
import pymysql


# 获取的增长率为空转为0

from scrapy_fund.com.constant import constant
from scrapy_fund.com.utils import utils


def clean_data(data):
    if data == '' or data=='--':
        return  0
    else:
        return  data.strip('%')
# 通过传入的地址参数获取接口数据
def get_fund_array(url):
    header={
      'Referer':'http://fundf10.eastmoney.com/jjjz_110011.html',
      'Host':'api.fund.eastmoney.com' ,
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:82.0) Gecko/20100101 Firefox/82.0'
    }
    req = urllib.request.Request(url,headers=header)
    response = urllib.request.urlopen(req)
    content = response.read()
    content = content.decode('utf-8')
    return  content

def save(fund_id,data_array):
    conn = pymysql.connect(host=constant.HOST, user=constant.USER, passwd=constant.PASSWORD, db=constant.DB,
                           port=constant.PORT, charset=constant.CHARSET)
    cur = conn.cursor()  # 获取一个游标
    insertSQL = " insert into fund_value(fund_id,fsrq,dwjz,ljjz,jzzzl) values(%s,%s,%s,%s,%s)"
    value_list = []
    fund_value_list=json.loads(data_array).get('Data').get('LSJZList')
    for item in fund_value_list:
        fund_id=fund_id
        fsrq=item.get('FSRQ')
        dwjz=item.get('DWJZ')
        ljjz=item.get('LJJZ')
        jzzzl=item.get('JZZZL')
        value_list.append((fund_id,fsrq,dwjz,ljjz,jzzzl))
    try:
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
public_url = constant.FUND_VALUE_URL
# 清空表
utils.truncate_table("fund_value")
#基金代码列表
fund_ids=constant.HOLD_FUND_IDS
pageSize='20000'
pageIndex='1'
#开始日期
startDate='2020-11-01'
#当然日期
endDate=time.strftime("%Y-%m-%d",time.localtime(time.time()))
# 插入抓取的数据
for fund_id in fund_ids:
    url = public_url+'startDate='+startDate+'&endDate='+endDate+'&pageSize='+pageSize+'&pageIndex='+pageIndex+'&fundCode='+fund_id
    print(url)
    time.sleep(5)
    data_array = get_fund_array(url)
    save(fund_id,data_array)
