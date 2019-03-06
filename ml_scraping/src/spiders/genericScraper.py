#Daniel Conway

import sys
import scrapy
import html2text
import re
import requests
from scrapy.crawler import CrawlerProcess
import os.path

path = '/Users/danielconway/thee-flying-chicken/ml_scraping/data/scrapingData/'

try:
    if len(sys.argv) != 2:
        print ("Please supply just one html")
        exit()
except Exception as e:
    print(e)

try:
    print("Started:\nParsing...")
    r = requests.get(sys.argv[1])

    parser = html2text.HTML2Text()
    parser.wrap_links = False
    parser.skip_internal_links = True
    parser.inline_links = True
    parser.ignore_anchors = True
    parser.ignore_images = True
    parser.ignore_emphasis = True
    parser.ignore_links = True
    text = parser.handle(r.text)
    text = text.strip(' \t\n\r')
    
    filename = sys.argv[1].replace('/', '')
    completeName = os.path.join(path, filename+".txt")
    print("Filename: %s"%(filename))
    with open(completeName,'w') as f:
        print ("Starting Writting")
        f.write(text)
        print("Completed")
    f.close()
    print("File Closed")

except Exception as e:
    print(e)
