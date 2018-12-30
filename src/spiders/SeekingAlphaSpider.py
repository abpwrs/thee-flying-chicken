#Daniel Conway

import scrapy


class SeekingAlphaSpider(scrapy.Spider):
    name = "AlphaSpider"
    allowed_domains = ["seekingalpha.com"]
    start_urls = ['https://seekingalpha.com/']


    def parse(self, response):

        links = response.xpath('//div[@class = "left_content"]/section[@class = "step_1"]/div[@class = "left_wrapper_unit"]/div[@class = "left_inside_wrapper"]/div[@class = "analysis_content"]/div[@class = "fade-out"]/div[@class = "article-elem"]/a[@class = "article_link"]/@href').extract()

        for url in links:
            abs_url = response.urljoin(url)
            yield scrapy.Request(url = abs_url, callback = self.parse_indetail)

    def parse_indetail(self, response):
        title = response.xpath('//header/div[@class = "sa-art-hd"]/h1/text()').extract()[0]
        filename = "seekingAlpha-%s.json" %title
        with open(filename,'w') as f:
            text = ''.join( response.xpath('//p/text()').extract() )
            f.write(text)
        self.log('Saved file %s'%filename)
