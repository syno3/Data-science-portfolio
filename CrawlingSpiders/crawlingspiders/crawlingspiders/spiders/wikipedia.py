import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class WikipediaSpider(CrawlSpider):
    name = 'eserver'
    allowed_domains = ['https://eserver.kabarak.ac.ke/']
    start_urls = ['https://eserver.kabarak.ac.ke/']
    rules = [Rule(LinkExtractor(allow=r'/((?!:).)*$'), callback='parse_info', follow=True)]

    def parse_info(self, response):
        return {
            'url': response.url
        }


