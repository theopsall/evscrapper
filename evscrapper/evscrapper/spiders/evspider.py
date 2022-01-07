import scrapy   
from urllib.parse import urljoin, urlparse



class EvSpider(scrapy.Spider):
    name = "ev"
    url=['https://ev-database.org/#sort:path~type~order=.rank~number~desc|range-slider-range:prev~next=0~1200|range-slider-acceleration:prev~next=2~23|range-slider-topspeed:prev~next=110~450|range-slider-battery:prev~next=10~200|range-slider-towweight:prev~next=0~2500|range-slider-fastcharge:prev~next=0~1500|paging:currentPage=0|paging:number=all']
    BASE_URL = "https://ev-database.org"
    
    def parse(self, response):
        for vehicle in response.css('div.list-item'):
        
            vehicle_url = vehicle.xpath("//div[@class='img']/a/@href").extract()
            
        yield response.follow(urljoin(self.BASE_URL, vehicle_url), callback=self.parse_vehicle) 
        
    
    def parse_vehicle(self, response):
        name = response.xpath("//header[@class='sub-header']/h1/text()").extract()
        yield name