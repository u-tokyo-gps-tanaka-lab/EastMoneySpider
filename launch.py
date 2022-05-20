from scrapy import cmdline
cmdline.execute('scrapy crawl EastMoneySpider -a stock_id=600000'.split())
#cmdline.execute('scrapy crawl EastMoneySpider -a stock_id=zssh000001'.split())
