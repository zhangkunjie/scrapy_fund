import scrapy
from com.scrapy.items import FundInfoItems

class FundSpider1(scrapy.Spider):
    name = 'fundSpider1'
    #start_urls = ['http://fund.eastmoney.com/000007.html']
    start_urls = ['http://fund.eastmoney.com/004490.html']
    def parse(self, response):
        infoOfFund=response.css(".infoOfFund td")
        print(infoOfFund[2].css("::text").extract())
        #print(staticItems[1])
