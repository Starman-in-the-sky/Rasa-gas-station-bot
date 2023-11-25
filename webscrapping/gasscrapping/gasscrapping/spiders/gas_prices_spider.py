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
        for gasStation in response.css('div.card'):
            yield {
                'station-name': gasStation.css('p.my-0.font-weight-normal small.text-muted::text').get(),
                'price_100': gasStation.css('li span.badge.bg-light.text-dark.product_name:contains("Аи-100") + span.text-::text').get(),
                'price_92': gasStation.css('li span.badge.bg-light.text-dark.product_name:contains("Аи-92") + span.text-::text').get(),
                'price_95': gasStation.css('li span.badge.bg-primary.product_name:contains("Аи-95") + span.text-::text').get(),
                'price_spbt': gasStation.css('li span.badge.bg-light.text-dark.product_name:contains("Газ СПБТ") + span.text-::text').get(),
                'price_dt': gasStation.css('li span.badge.bg-light.text-dark.product_name:contains("ДТ") + span.text-::text').get(),
                'price_metan': gasStation.css('li span.badge.bg-light.text-dark.product_name:contains("Метан") + span.text-::text').get(),
                'price_premium_92': gasStation.css('li span.badge.bg-light.text-dark.product_name:contains("Премиум 92") + span.text-::text').get(),
                'price_premium_95': gasStation.css('li span.badge.bg-light.text-dark.product_name:contains("Премиум 95") + span.text-::text').get(),
                'price_premium_dt': gasStation.css('li span.badge.bg-light.text-dark.product_name:contains("Премиум ДТ") + span.text-::text').get(),
                'address': gasStation.css('p.card-title.pricing-card-title small.text-muted::text').get()
            }