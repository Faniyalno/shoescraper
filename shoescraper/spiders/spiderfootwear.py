import scrapy


class SpiderfootwearSpider(scrapy.Spider):
    name = "spiderfootwear"
    allowed_domains = ["pyoppfledge.com"]
    start_urls = ["https://pyoppfledge.com/collections/barefoot-shoes"]

    def parse(self, response):
        footwears = response.css('div.product-item')
        for footwear in footwears:
            yield{
                'Name' : footwear.css('h4 a::text').get(),
                'price' : footwear.css('span.money::text').get(),
                'url' : footwear.css('h4 a::attr(href)').get(),
            }