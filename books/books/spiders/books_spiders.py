import scrapy


class BooksSpidersSpider(scrapy.Spider):
    name = 'books_spiders'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        pass
