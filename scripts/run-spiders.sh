#!/bin/sh
# Author: AlexPowers
# Sun Dec 30 13:13:00 CST 2018
# All scripts should be run from the project root
for spider_script in ./src/spiders/*.py; do
scrapy runspider ${spider_script}
done
