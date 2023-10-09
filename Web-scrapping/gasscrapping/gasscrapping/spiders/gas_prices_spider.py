import scrapy


class GasPricesSpider(scrapy.Spider):
    name = "gasPrices"

    def start_requests(self):
        urls = [
            'https://azsprice.ru/moskva?ysclid=lnj63ytfyq82170833'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')