# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter


# class ScrapyTestPipeline:
#     def process_item(self, item, spider):
#         return item

import json

class JsonExportPipeline:
    def open_spider(self, spider):
        self.output_file = open('output.json', 'w', encoding='utf-8')
        self.output_file.write('[')

    def close_spider(self, spider):
        self.output_file.write('\n]')
        self.output_file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.output_file.write(line)
        return item
