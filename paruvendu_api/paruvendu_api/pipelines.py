# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class JsonWriterPipeline:
    def open_spider(self, url_harvester):
        self.file = open('C:/Users/thiba/Desktop/SIMPLON_PARUVENDU_API/paruvendu_api/paruvendu_api/outputs/harvest.json', 'w', encoding='utf-8')

    def close_spider(self, url_harvester):
        self.file.close()

    def process_item(self, url_harvester_item, url_harvester):
        line = json.dumps(ItemAdapter(url_harvester_item).asdict(), ensure_ascii=False) + "\n"
        self.file.write(line)
        return url_harvester_item
