import scrapy
from items import HeightWeightItem

arrayedIds = open('ids.txt', 'r')

known_hu_ids = arrayedIds.read().split(',')

class HeightWeightSpider(scrapy.Spider):
    name = "heightweight"
    allowed_domains = ["my.pgp-hms.org"]
    start_urls = ["https://my.pgp-hms.org/profile/%s" % (huid) for huid in known_hu_ids]
    def parse(self, response):
        item = HeightWeightItem()
        assert response.status == 200, "Bad response"
        item['Sample'] = response.url.split('/')[-1]
        for sel in response.xpath('//table[@class="demographics"]/tr'):
            if sel.xpath('th/text()').extract() == ['Height']:
                height_list = sel.xpath('td/text()').extract()
                if len(height_list) > 0:
                    assert len(height_list) == 1, "height? %s" % (height_list)
                    item['Height'] = height_list[0]
            if sel.xpath('th/text()').extract() == ['Weight']:
                weight_list = sel.xpath('td/text()').extract()
                if len(weight_list) > 0:
                    assert len(weight_list) == 1, "weight? %s" % (weight_list)
                    item['Weight'] = weight_list[0]
        yield item