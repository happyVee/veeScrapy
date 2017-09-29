#Coding = 'utf-8'
import scrapy
from scrapy import Request
from scrapy.spiders import Spider
from wanbang.items import WanbangItem

class wanbangSpider(Spider):
	name = 'wanbangSpider'
	headers = {
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Encoding':'gzip, deflate, sdch',
	'Accept-Language':'zh-CN,zh;q=0.8',
	'Connection':'keep-alive',
	'Upgrade-Insecure-Requests':'1',
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
	}


	def start_requests(self):
		url = 'http://zhengzhou.wbtrans.com/index.asp?ty=130'
		yield Request(url, headers=self.headers)

	def parse(self, response):
		item = WanbangItem()
		tuanitem = response.xpath('//div[@class="lister"]/div[@class="tuanitem"]')
		for tuan in tuanitem:
			item['iurl'] = 'http://zhengzhou.wbtrans.com/' + tuan.xpath(
				'.//div[@class="tuanitem-meta-title"]/a/@href').extract()[0]
			yield item
'''
		next_url = response.xpath('//div[@id="pagation"]/a[@title="下一页"]/@href').extract()
		if next_url:
			next_url = 'http://zhengzhou.wbtrans.com/' + next_url[0]
			yield Request(next_url, headers=self.headers,callback=self.parse)
			'''