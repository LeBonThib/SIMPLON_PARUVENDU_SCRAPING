# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class URLHarvesterItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    status = scrapy.Field()
    brand = scrapy.Field()

class CarHarvesterItem(scrapy.Item):
    # define the fields for your item here like:
    version = scrapy.Field()
    price = scrapy.Field()
    year = scrapy.Field()
    kms = scrapy.Field()
    fuel = scrapy.Field()
    emission = scrapy.Field()
    consommation = scrapy.Field()
    transmission = scrapy.Field()
    door_nb = scrapy.Field()
    power = scrapy.Field()
    seat_nb = scrapy.Field()