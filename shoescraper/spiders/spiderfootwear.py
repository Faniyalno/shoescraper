import scrapy
from shoescraper.items import FtwearItem


class SpiderfootwearSpider(scrapy.Spider):
    name = "spiderfootwear"
    allowed_domains = ["pyoppfledge.com"]
    start_urls = ["https://pyoppfledge.com/collections/barefoot-shoes"]

    def parse(self, response):
        footwears = response.css('div.product-item')
        for footwear in footwears:
            relative_url = footwear.css('h4 a').attrib['href']
            footwear_url = 'https://pyoppfledge.com' + relative_url
            yield response.follow(footwear_url, callback=self.parse_footwear)

        next_element = response.css('a.pagination__touch::attr(title)').get().split(' ')[0].lower()
        if next_element == 'next':
            next_page = response.css('li.pagination__item a.link::attr(href)').get().split('&')[0]
            if next_page is not None:
                next_page_url = 'https://pyoppfledge.com' + next_page
            yield response.follow(next_page_url, callback=self.parse)

    def parse_footwear(self, response):
        # I am Unable to make scrapy interact with the web to make filter that tells which size available works
        # is_available = response.css('button.btn > span:nth-child(1)::text').get().lower().strip()
        # if is_available == "add to cart":
        #     available_size = [response.css('button.fs-body-base::attr(aria-label)').get()]

        list_option_rectangle = response.css('select.pf-input::attr(name)').get()

        def desc_checker(response):
            has_span = response.css('div.product-single__description span::text').get()
            has_p = response.css('div.product-single__description p::text').get()
            generic_page = response.css('div.product-single__description::text').get()

            if has_span is not None:
                ftwear_item['description'] = response.css('div.product-single__description span::text').getall()
            elif has_p is not None:
                ftwear_item['description'] = response.css('div.product-single__description p::text').getall()
            elif generic_page is not None:
                ftwear_item['description'] = response.css('div.product-single__description::text').getall()

        ftwear_item = FtwearItem()
        ftwear_item['name'] = response.css('h1.product-single__title::text').get(),
        ftwear_item['price'] = response.css('span.money::text').get(),
        if list_option_rectangle == 'options[Ukuran]':
            ftwear_item['size_lists'] = response.css('select.pf-input option::text').getall(),
        else: 
            ftwear_item['size_lists'] = response.css('button.fs-body-base::attr(aria-label)').getall(),
        ftwear_item['vendor'] = response.css('div.product__vendor a::text').get(),
        desc_checker(response)

        ftwear_item['url'] = response.url,

        yield ftwear_item
