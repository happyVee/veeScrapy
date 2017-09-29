# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from openpyxl import Workbook

class WanbangPipeline(object):

	wb = Workbook()
	ws = wb.active
	ws.append(['num','iurl'])
	count = 1

	def process_item(self, item, spider):
		line = [self.count,item['iurl']]
		self.ws.append(line)
		self.count = self.count + 1
		self.wb.save('res.xlsx')
		return item
