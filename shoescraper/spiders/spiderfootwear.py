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

        next_page = response.css('li.pagination__item a.link::attr(href)').get().split('&')[0]
        if next_page is not None:
            next_page_url = 'https://pyoppfledge.com' + next_page
        yield response.follow(next_page_url, callback=self.parse)