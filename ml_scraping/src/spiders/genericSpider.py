#Daniel Conway

import sys
import scrapy
import html2text
import re
from scrapy.crawler import CrawlerProcess

try:
    if len(sys.argv) != 2:
        print ("Please supply just one html")
        exit()
except Exception as e:
    print(e)

try:
    url1 = sys.argv[-1]

    class genericSpider(scrapy.Spider):
        name = "genericSpider"
        # allowed_domains = ["seekingalpha.com"]
        # start_urls = [str(url1)]
        def parse(self, response):
            abs_url = response.urljoin(url1)
            yield scrapy.Request(url = abs_url, callback = self.parse_indetail)

        def parse_indetail(self, response, rehtml = False):
            html = response
            parser = html2text.HTML2Text()
            parser.wrap_links = False
            parser.skip_internal_links = True
            parser.inline_links = True
            parser.ignore_anchors = True
            parser.ignore_images = True
            parser.ignore_emphasis = True
            parser.ignore_links = True
            text = parser.handle(html)
            text = text.strip(' \t\n\r')
            if rehtml:
                text = text.replace('\n', '<br/>')
                text = text.replace('\\', '')
            filename = str(url1)
            with open('../ml_scraping/data/scrapingData/' + filename,'w') as f:
                f.write(text)
                self.log('Saved file %s'%filename)
except Exception as e:
    print(e)

if __name__ == "__main__":
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(genericSpider)
    process.start() # the script will block here until the crawling is finished