import scrapy
from scrapy_splash import SplashRequest

from gazette.settings import USER_AGENT


class DfSpider(scrapy.Spider):
    name = 'facebook'
    allowed_domains = ['dodf.df.gov.br']
    start_urls = ['http://dodf.df.gov.br/listar']

    def start_requests(self):
        for url in self.start_urls:
            request = SplashRequest(url,
                                    self.parse,
                                    args={'wait': .8},
                                    headers={'User-Agent': USER_AGENT})
            yield request

    def parse(self):
        pass
