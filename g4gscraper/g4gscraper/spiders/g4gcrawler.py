# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from g4gscraper.items import G4GscraperItem


class G4GSpider(CrawlSpider):
    name = "g4gtags"
    allowed_domains = ["www.geeksforgeeks.org"]
    startingUrl = 'https://www.cdn.geeksforgeeks.org/tag/amazon/'
    start_urls = [
        startingUrl
    ]

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