# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
def dbHandle():
        conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='mysql',db='test',charset='utf8')
        return conn
class WriteToMysqlPipeline(object):
    def process_item(self, item, spider):
     if spider.name=='fundInfoSpider':
        dbObject =dbHandle()
        cursor = dbObject.cursor()
        sql=('''insert into fund_info
        (
        fund_id,
        name,
        type,
        scale,
        manager,
        setup_date,
        admin,
        grade,
        trade_first_status,
        trade_sencond_status  
        )
        values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''')
        cursor.execute(
        sql,
        (
        item['fund_id'],
        item['name'],
        item['type'],
        item['scale'],
        item['manager'],
        item['setup_date'],
        item['admin'],
        item['grade'],
        item['trade_first_status'],
        item['trade_sencond_status']
         ))
        dbObject.commit()
        cursor.close()
        dbObject.close()
     elif  spider.name=='fundValueSpider':
            dbObject =dbHandle()
            cursor = dbObject.cursor()
            sql=('''insert into fund_value
            (
            fund_id,
            name,
            netvalue_date,
            netvalue,
            cumulativevalue,
            daily_growth_rate,
            apply_status,
            redeem_status,
            bonus
            )
            values (%s,%s,%s,%s,%s,%s,%s,%s,%s)''')
            cursor.execute(
            sql,
            (
            item['fund_id'],
            item['name'],
            item['netvalue_date'],
            item['netvalue'],
            item['cumulativevalue'],
            item['daily_growth_rate'],
            item['apply_status'],
            item['redeem_status'],
            item['bonus']
             ))
            dbObject.commit()
            cursor.close()
            dbObject.close()
     return item