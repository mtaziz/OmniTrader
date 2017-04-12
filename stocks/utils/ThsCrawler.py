import scrapy



class ThsCrawler():

    def parse(self,response):
        print("world")

    def send(self):
        print("hello")
        yield scrapy.Request(url='http://stockpage.10jqka.com.cn/600340/', callback=self.parse)
        return


crawler = ThsCrawler()
print("before")
crawler.send()

print("after")