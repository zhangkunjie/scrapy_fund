# -*- coding:utf8 -*-
import urllib.request
import pymysql



# 获取的增长率为空转为0
from bs4 import BeautifulSoup

from com.constant import constant


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
    req = urllib.request.Request(url,headers=header)
    response = urllib.request.urlopen(req)
    content = response.read()
    content = content.decode('gbk')
    return  content


def save_fund(fund_id_list):
    conn = pymysql.connect(host=constant.HOST, user=constant.USER, passwd=constant.PASSWORD, db=constant.DB,
                           port=constant.PORT, charset=constant.CHARSET)
    cur = conn.cursor()  # 获取一个游标
    insertSQL = " insert into fund_ids(fund_id,info_url,topic_url,archive_url) values(%s,%s,%s,%s)"
    value_list = []
    for fund in fund_id_list:
        fund_id=fund[0],
        info_url=fund[1],
        topic_url=fund[2],
        archive_url=fund[3]
        value_list.append((fund_id,info_url,topic_url,archive_url))
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
all_fund_url = constant.ALLFUND_URL
fund_array = get_fund_array(all_fund_url)
soup = BeautifulSoup(fund_array, 'lxml')
fund_info_text=soup.select("ul.num_right>li>div")
fund_id_list=[]
for item in fund_info_text:
    fund_text=item.contents[0].text
    fund_id=fund_text[1:7]
    fund_name=fund_text[8:]
    info_url='http://fund.eastmoney.com/'+fund_id+'/.html'
    topic_url = 'http://jijinba.fund.eastmoney.com/topic,' + fund_id + '/.html'
    archive_url = 'http://fund10.eastmoney.com/' + fund_id + '/.html'
    fund_id_list.append([fund_id,info_url,topic_url,archive_url])
save_fund(fund_id_list)