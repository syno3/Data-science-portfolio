## initializing terminal color variables
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

try:
    import scrapy
    import logging
    import pytest
    import re
    from loguru import logger
    from scrapy.spiders import CrawlSpider, Rule
    from scrapy.linkextractors import LinkExtractor
    import time
except ImportError:
    print(FAIL+'please run python.exe pip install -r requirements.txt')
logo = FAIL+'''
 ██████╗██████╗  █████╗ ██╗    ██╗██╗     ██╗███╗   ██╗ ██████╗ ███████╗██████╗ ██╗██████╗ ███████╗██████╗ ███████╗
██╔════╝██╔══██╗██╔══██╗██║    ██║██║     ██║████╗  ██║██╔════╝ ██╔════╝██╔══██╗██║██╔══██╗██╔════╝██╔══██╗██╔════╝
██║     ██████╔╝███████║██║ █╗ ██║██║     ██║██╔██╗ ██║██║  ███╗███████╗██████╔╝██║██║  ██║█████╗  ██████╔╝███████╗
██║     ██╔══██╗██╔══██║██║███╗██║██║     ██║██║╚██╗██║██║   ██║╚════██║██╔═══╝ ██║██║  ██║██╔══╝  ██╔══██╗╚════██║
╚██████╗██║  ██║██║  ██║╚███╔███╔╝███████╗██║██║ ╚████║╚██████╔╝███████║██║     ██║██████╔╝███████╗██║  ██║███████║
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝
                                                                                                        
''' 

print(logo)
time.sleep(3)
#getting the links from the user via the terminal
website_name = input(OKGREEN+'please enter the name of the website \n : \t')
user_website = input(OKGREEN+'Please enter a website youd like to parse\n :\t')
#checking wether the input given is an actual url
regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

if (re.match(regex, user_website) is not None) == True:
## Creating the crawler and catch errors
    #logging.warning('The script should be working')
    class WikipediaSpider(CrawlSpider):
        name = str(website_name)
        allowed_domains = [str(user_website)]
        start_urls = [str(user_website)]
        rules = [Rule(LinkExtractor(allow=r'/((?!:).)*$'), callback='parse_info', follow=True)]

        def parse_info(self, response):
            return {
                'url': response.url
            }

else:
    logging.warning('Please provide a valid url')
