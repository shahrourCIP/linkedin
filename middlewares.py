from scrapy import signals
from itemadapter import is_item, ItemAdapter


class BasicScraperSpiderMiddleware:

    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        return None

    def process_spider_output(self, response, result, spider):
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        pass

    def process_start_requests(self, start_requests, spider):

        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class QuotesJsScraperDownloaderMiddleware:

    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        return None

    def process_response(self, request, response, spider):
        return response

    def process_exception(self, request, exception, spider):
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

class shahrour:
    def uniorschools(self, uni:str, des:str, GPA:float):
        rqq = shahrour().uniorschools()
        pass
    pass

class all_info:
    def user(username:str):
        '''
        ---> username: linkedin: ->linkedin.com/{username}
        '''
        pass
    def edu(user:str):
        """
        ---> education: linkedin: -> linkedin.com/username/details/{education}
        """
        pass
    def experience():
        '''
        experience: linkedin.com/{username}/details/{experience}/
        '''
        pass
    pass