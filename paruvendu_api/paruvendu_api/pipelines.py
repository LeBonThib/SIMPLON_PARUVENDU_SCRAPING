# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class JsonWriterPipeline:
    """ def open_spider(self, spider):
        if spider.name == "url_harvester":
            self.file = open('./paruvendu_api/outputs/url_harvest.json', 'w', encoding='utf-8')
        if spider.name == "data_harvester":
            self.file = open('./paruvendu_api/outputs/data_harvest.json', 'w', encoding='utf-8')
            # self.file.write('{"data":[')

    def close_spider(self, spider):
        if spider.name == "url_harvester":
            self.file.close()
        if spider.name == "data_harvester":
            # self.file.write(']}')
            self.file.close() """

    def process_item(self, spider_item, spider):
        """ if spider.name == "url_harvester":
            line = json.dumps(ItemAdapter(spider_item).asdict(), ensure_ascii=False) + "\n"
            self.file.write(line)
            return spider_item
        if spider.name == "data_harvester":
            # line = json.dumps(ItemAdapter(spider_item).asdict(), ensure_ascii=False) + ",\n"
            # self.file.write(line)
            # return spider_item
            exporter = self._exporter_for_item(spider_item)
            exporter.export_item(spider_item) """
        return spider_item