import scrapy
class HeightWeightItem(scrapy.Item):
	Sample = scrapy.Field()
	Height = scrapy.Field()
	Weight = scrapy.Field()