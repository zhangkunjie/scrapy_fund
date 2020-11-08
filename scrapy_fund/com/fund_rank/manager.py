# -*- coding:utf8 -*-
import time
import urllib.request
import pymysql



# 获取的增长率为空转为0
from scrapy_fund.com.constant import constant
from scrapy_fund.com.utils import utils


def clean_data(data):
    if data == '':
        return  "--"
    else:
        return  data.strip('%')
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
    content = content[content.index(":[") + 1:content.index("]],") + 2]
    data_array = eval(content)
    if data_array!=[]:
        return data_array


def save_fund(data_array):
    conn = pymysql.connect(host=constant.HOST, user=constant.USER, passwd=constant.PASSWORD, db=constant.DB,
                           port=constant.PORT, charset=constant.CHARSET)
    cur = conn.cursor()  # 获取一个游标
    insertSQL = " insert into fund_manager(manager_id,manager_name,company_id,company_name,fund_id,fund_name,work_day,scale,now_best_fund_id,now_best_fund_name,now_best_fund_yields,his_best_fund_yields) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    value_list = []
    for item in data_array:
        manager_id = clean_data(item[0])
        manager_name = clean_data(item[1])
        company_id = clean_data(item[2])
        company_name = clean_data(item[3])
        managed_fumd_ids_array = item[4].split(",")
        managed_fumd_names_array = item[5].split(",")
        work_day = clean_data(item[6])
        scale = clean_data(item[10])
        now_best_fund_yields = clean_data(item[7])
        now_best_fund_id = clean_data(item[8])
        now_best_fund_name = item[9]
        his_best_fund_yields = clean_data(item[11])
        for i in range(0, len(managed_fumd_ids_array)):
            fund_id = clean_data( managed_fumd_ids_array[i])
            fund_name = clean_data(managed_fumd_names_array[i])
            value_list.append((manager_id,manager_name,company_id,company_name,fund_id,fund_name,work_day,scale,now_best_fund_id,now_best_fund_name,now_best_fund_yields,his_best_fund_yields))
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

# 清空表
utils.truncate_table("fund_manager")
# 开始组合函数
for  i in  range(1):
  manager_url = constant.MANAGER_URL+"&pn=2500&pi="+str(i)
  # 插入抓取的数据
  data_array = get_data_array(manager_url)
  time.sleep(1)
  save_fund(data_array)
