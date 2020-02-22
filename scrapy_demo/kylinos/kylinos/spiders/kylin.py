# -*- coding: utf-8 -*-
import scrapy
from kylinos.items import KylinosItem

class KylinSpider(scrapy.Spider):
    name = 'kylin'
    # http://www.kylinos.cn/job_list.aspx?category_id=256
    # http://www.kylinos.cn/job_list.aspx?category_id=256&page=1
    allowed_domains = ['www.kylinos.cn']
    start_urls = ['http://www.kylinos.cn/job_list.aspx?category_id=256']

    def parse(self, response):
        item = KylinosItem()
        # print(response.body.decode('utf-8'))
        next_url = response.xpath("//div[@class='digg']/a[last()]/@href").extract()[0]
        print(next_url)
        for content in response.xpath("//ul[@class='n-list']/li"):
            position = content.xpath("h2/text()").extract()[0]
            datas = content.xpath("div/p//text()").extract()
            keys =["招聘人数","工作地点","岗位","任职要求"]
            if self._split_item(datas,keys) != False:
                num,location,duty,request1 = self._split_item(datas,keys)
            else:
                continue
            item["position"] = position
            item['num'] = num
            item['location'] = location
            item['duty'] = duty
            item['request'] = request1
            # print("position:",position)
            # print("num:",num)
            # print("location:",location)
            # print("duty:",duty)
            # print("request:",request1)
            yield item
        yield scrapy.Request("http://www.kylinos.cn" + next_url, callback=self.parse)

    @staticmethod
    def _split_item(datas,keys):
        # data = "".join(x for x in datas if x not in ['\r\n\t', '\r\n'])
        data = [x for x in datas if x not in ['\r\n\t', '\r\n']]
        index = list()
        k = 0
        for i in range(len(data)):
            if keys[k] in data[i]:
                index.append(i)
                k += 1
            if k >= len(keys):
                break
        if len(index) == len(keys):
            num = data[index[0]:index[1]][1]
            location = data[index[1]:index[2]][0].split("：")[1]
            duty = data[index[2]:index[3]][1:]
            duty = ''.join(duty)
            request1 = data[index[3]:][1:]
            request1 = ''.join(request1)
            return num, location, duty, request1
        else:
            print(data)
            return False