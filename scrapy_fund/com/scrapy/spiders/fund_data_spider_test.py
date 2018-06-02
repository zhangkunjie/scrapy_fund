import scrapy
from com.scrapy.items import FundValueItems
from com.scrapy.spiders.log import get_logger

class FundSpider1(scrapy.Spider):
    name = 'fundSpider2'
    start_urls = ['http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code=660102&page=1&per=50000']
    def parse(self, response):
        fundValueItem=FundValueItems()
        fund_values_trs=response.css("tr")
        for i in range(1,len(fund_values_trs)):
           tds=fund_values_trs[i].css("td")
           if len(tds)==7:
            #print(tds) 
            try:
                fundValueItem['fund_id']="00001"
                fundValueItem['name']="fund_name"
                fundValueItem['netvalue_date']=tds[0].css("::text").extract_first()
                fundValueItem['netvalue']=tds[1].css("::text").extract_first()
                fundValueItem['cumulativevalue']=tds[2].css("::text").extract_first()
                fundValueItem['daily_growth_rate']=tds[3].css("::text").extract_first()
                fundValueItem['apply_status']=tds[4].css("::text").extract_first()
                fundValueItem['redeem_status']=tds[5].css("::text").extract_first()
                fundValueItem['bonus']=tds[6].css("::text").extract_first()
                #my_logger = get_logger('fundValueSpider','')
                #my_logger.info('Info logger')
                #my_logger.error('Error logger')
                yield fundValueItem
            except Exception as e:  
              my_logger = get_logger('fundValueSpider','')
              my_logger.error(e)  
           #货币基金
           elif len(tds)==6:
            try:   
                fundValueItem['fund_id']="00001"
                fundValueItem['name']="fund_name"
                fundValueItem['netvalue_date']=tds[0].css("::text").extract_first()
                fundValueItem['netvalue']=tds[1].css("::text").extract_first()
                fundValueItem['cumulativevalue']=tds[1].css("::text").extract_first()
                fundValueItem['daily_growth_rate']=tds[2].css("::text").extract_first()
                fundValueItem['apply_status']=tds[3].css("::text").extract_first()
                fundValueItem['redeem_status']=tds[4].css("::text").extract_first()
                fundValueItem['bonus']=tds[5].css("::text").extract_first()
                yield fundValueItem
            except Exception as e:  
                my_logger = get_logger('fundValueSpider','')
                my_logger.error(e)