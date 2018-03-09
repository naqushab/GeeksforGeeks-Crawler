import scrapy
from scrapy.crawler import CrawlerProcess

from g4gscraper.spiders.g4gcrawler import G4GSpider

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'FEED_FORMAT': 'json',
    'FEED_URI': 'data.json'
})

process.crawl(G4GSpider)
process.start() # the script will block here until the crawling is finished