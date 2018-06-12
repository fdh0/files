reated on 2018-01-22 12:13:12
# Project: 51job


from pyspider.libs.base_handler import *

class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://jobs.51job.com/', callback=self.main_index, validate_cert=False, age=0)

    @config(age=10 * 24 * 60 * 60)
    def main_index(self, response):
        for each in response.doc('.e5 .lkst a').items():
            self.crawl(each.attr.href, callback=self.index_page, validate_cert=False, age=0)

    @config(priority=1)
    def index_page(self, response):
        for each in response.doc('.e .info .title a').items():
            self.crawl(each.attr.href, callback=self.detail_page, validate_cert=False, age=0,retries=3)
        for each in response.doc('.bk a').items():
            print "deep"
        self.crawl(each.attr.href, callback=self.index_page, validate_cert=False, age=0)
                
    
    @config(priority=2)
    def detail_page(self, response):
        return {
            "公司":response.doc('.cname').text(),
            "公司规模":response.doc('.ltype').text(),
            "职位":response.doc('h1').text(),
            "薪资":response.doc('.cn strong').text(),
            "描述":response.doc('.job_msg').text(),
            "地点":response.doc('.lname').text(),
        }

