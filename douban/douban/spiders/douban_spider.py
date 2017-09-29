#Coding = 'utf-8'
import scrapy
from scrapy import Request
from scrapy.spiders import Spider
from douban.items import DoubanItem

class doubanTopSpider(Spider):
	name = 'doubanSpider'
	headers = {
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Encoding':'gzip, deflate, sdch',
	'Accept-Language':'zh-CN,zh;q=0.8',
	'Connection':'keep-alive',
	'Upgrade-Insecure-Requests':'1',
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
	}

	def start_requests(self):
		url = 'https://movie.douban.com/top250'
		yield Request(url, headers=self.headers)

	def parse(self, response):
		item = DoubanItem()
		movies = response.xpath('//ol[@class="grid_view"]/li')
		for movie in movies:
			item['rank'] = movie.xpath(
				'.//div[@class="pic"]/em/text()').extract()[0]
			item['name'] = movie.xpath(
				'.//div[@class="hd"]/a/span[1]/text()').extract()[0]
			item['score'] = movie.xpath(
				'.//div[@class="star"]/span[@class="rating_num"]/text()'
			).extract()[0]
			yield item

		next_url = response.xpath('//span[@class="next"]/a/@href').extract()
		if next_url:
			next_url = 'https://movie.douban.com/top250' + next_url[0]
			yield Request(next_url, headers=self.headers,callback=self.parse)