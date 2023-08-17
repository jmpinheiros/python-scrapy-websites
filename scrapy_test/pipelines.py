#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
