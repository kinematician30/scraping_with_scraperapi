import scrapy
from books.items import BooksItem


class BooksSpidersSpider(scrapy.Spider):
    name = 'books_spiders'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        self.logger.info("spider started")
        all_elements = response.css("article.product_pod")
        for elements in all_elements:
            elements.css("h3 > a::attr(href)").get()

        pass

    def extract(self, parse):
        pass
