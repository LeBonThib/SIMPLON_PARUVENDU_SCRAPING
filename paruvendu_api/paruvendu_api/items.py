# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class URLHarvesterItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    status = scrapy.Field()

class DataHarvesterItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    status = scrapy.Field()
    location = scrapy.Field()
    version = scrapy.Field()
    price = scrapy.Field()
    year = scrapy.Field()
    mileage = scrapy.Field()
    fuel_type = scrapy.Field()
    emission = scrapy.Field()
    fuel_usage = scrapy.Field()
    transmission = scrapy.Field()
    door_nb = scrapy.Field()
    seat_nb = scrapy.Field()
    technical_power = scrapy.Field()
    actual_power = scrapy.Field()
    body_colour = scrapy.Field()
    body_type = scrapy.Field()
    warranty = scrapy.Field()
    control = scrapy.Field()
