import scrapy
from com.scrapy.items import FundInfoItems

class FundSpider(scrapy.Spider):
    name = 'fundInfoSpider'
    #start_urls = ['http://fund.eastmoney.com/000007.html']
    start_urls = ['http://fund.eastmoney.com/allfund.html']
    def parse(self, response):
        fund_info_list=response.css(".num_right>li>div")
        #f=open("/Users/user/Desktop/fund_info","w+")
        for fund in fund_info_list:
            #print(fund.css("a::attr(href)").extract_first())
            fund_detail_url=fund.css("a::attr(href)").extract_first()
            yield scrapy.Request(fund_detail_url,
                   callback=self.pares_fund_detail)
    def pares_fund_detail(self,response):   
        fundInfoItem=FundInfoItems()
        #基金id和基金名称
        fundInfoItem['fund_id']=response.css(".fundDetail-tit div span[class='ui-num']::text").extract_first()
        fundInfoItem['name']=response.css(".fundDetail-tit div::text").extract_first()
        #估值、净值、累计净值和6项增长率
        """
        valueItems=infoOfFund=response.css("div .dataOfFund")[1].css("dl dd span[class~='ui-num']::text").extract()
        fundInfoItem['estimate_value']=0
        fundInfoItem['estimate_value_rose']=0
        fundInfoItem['unit_value']=0
        fundInfoItem['unit_value_rose']=0
        fundInfoItem['cumulative_value']=0
        fundInfoItem['last_month']=valueItems[0]
        fundInfoItem['last_3_month']=valueItems[2]
        fundInfoItem['last_half_year']=valueItems[4]
        fundInfoItem['last_year']=valueItems[1]
        fundInfoItem['last_3_yesr']=valueItems[3]
        fundInfoItem['set_up']=valueItems[5]
        """
        #基金类型、规模、经理、成立日期等
        infoOfFund=response.css(".infoOfFund td")
        #基金类型
        if len(infoOfFund[0].css("::text"))>1:
            fundInfoItem['type']=infoOfFund[0].css("::text")[1].extract()
        else:
            fundInfoItem['type']=infoOfFund[0].css("::text")[0].extract().replace("基金类型：", "").split("|")[0].strip()
        fundInfoItem['scale']=infoOfFund[1].css("::text").extract()[1].split("亿")[0].replace("：","")
        if len(infoOfFund[2].css("::text").extract())>1:
           fundInfoItem['manager']=infoOfFund[2].css("::text").extract()[1]
        else:
           fundInfoItem['manager']=''
        fundInfoItem['setup_date']=infoOfFund[3].css("::text").extract()[1].split('：')[1]
        fundInfoItem['admin']=infoOfFund[4].css("a::text").extract_first()
        fundInfoItem['grade']=infoOfFund[5].css("div::attr(class)").extract_first()
        #基金状态
        staticItems=response.css("div .staticItem")[0].css(".staticCell::text").extract()
        if len(staticItems)>1:
           fundInfoItem['trade_first_status']=staticItems[0]
           fundInfoItem['trade_sencond_status']=staticItems[1]
        else:
           fundInfoItem['trade_first_status']=staticItems[0]
           fundInfoItem['trade_sencond_status']=staticItems[0] 
        yield fundInfoItem
        
        
        
        
        
        
        """
        dataItems=response.css(".dataOfFund dl")
        for dataItem in dataItems:
            dds=dataItem.css("dd")
            for dd in dds: 
                #print(dd.extract())
                ds=dd.css(".ui-num::text")
                #print(ds.extract())
                #print(ds.extract()[0])
                for d in ds:
                    print(d.extract())
        """
        """
        infoOfFund=response.css(".infoOfFund td")
        print(infoOfFund[0].css("::text").extract()[1])
        print(infoOfFund[1].css("::text").extract()[1])
        print(infoOfFund[2].css("::text").extract()[1])
        print(infoOfFund[3].css("::text").extract()[1])
        print(infoOfFund[4].css("a::text").extract_first())
        print(infoOfFund[5].css("div::attr(class)").extract_first())
        """
        """
        staticItem=response.css("div .staticItem")[0]
        staticCells=staticItem.css(".staticCell::text")
        print(staticCells[0].extract())
        print(staticCells[1].extract())
        """
        
        
        """       
        f=open("/Users/user/Desktop/python/123.txt",'w+')
        fund_daily_info=response.css("tbody tr")
        for  fund_info in fund_daily_info:
             td_infos=fund_info.css("td::text").extract()
             print(str(td_infos[0])+"\t"+str(td_infos[1]))
             f.write(str(td_infos[0])+"\t"+str(td_infos[1])+"\n")
        f.close()
        
        
        fund_list=response.css(".b>div")
        for fund in fund_list:
            print(fund.css("a::attr(href)")[0].extract())
        """