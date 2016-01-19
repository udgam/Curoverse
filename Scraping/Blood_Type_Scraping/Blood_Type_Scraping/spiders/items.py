import scrapy
class BloodTypeItem(scrapy.Item):
	Sample = scrapy.Field()
	Bloodtype = scrapy.Field()