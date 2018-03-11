# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from g4gscraper.items import G4GscraperItem


class G4GSpider(CrawlSpider):
    name = "g4gtagcrawler"
    allowed_domains = ["www.geeksforgeeks.org"]
    start_urls = []
    tag = None

    def __init__(self, tag='amazon', *args, **kwargs):
        super(G4GSpider, self).__init__(*args, **kwargs)
        self.tag = str(tag).lower()
        baseURL = 'https://www.geeksforgeeks.org/tag/' + self.tag
        print(baseURL)
        self.start_urls.append(baseURL)
    
    def parse(self, response):
        item_links = response.css('.entry-title a::attr(href)').extract()

        for a in item_links:
            yield scrapy.Request(a, callback=self.parse_detail_page)
        
        for a in response.css('.nextpostslink'):
            yield response.follow(a, callback=self.parse)

    def parse_detail_page(self, response):
        title = response.css('.entry-title').extract()[0].strip()
        content = response.css('.entry-content').extract()[0]

        item = G4GscraperItem()
        item['title'] = title
        item['content'] = content
        yield item