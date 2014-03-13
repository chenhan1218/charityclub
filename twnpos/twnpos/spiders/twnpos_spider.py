from scrapy.spider import Spider

class TwnposSpider(Spider):
    name = "twnpos"
    allowed_domains = ["www.twnpos.org.tw"]
    start_urls=[]
    for idx in xrange(0, 200):
        start_urls.append("http://www.twnpos.org.tw/team/team_detail.php?Key=%d" % idx)

    def parse(self, response):
        filename = 'twnpos-data/twnpos-' + str(response.url.split("=")[-1])
        open(filename, 'wb').write(response.body)
