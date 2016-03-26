# coding=utf-8
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    # 1.添加url
    def add_new_url(self, new_url):
        if new_url is None:
            return
        # 既不在新url 也不在访问过的url集合中
        if new_url not in self.new_urls and new_url not in self.old_urls:
            self.new_urls.add(new_url)
        pass

    # 2.添加url集合
    def add_new_urls(self, new_urls):
        if new_urls is None or len(new_urls) == 0:
            return False
        for url in new_urls:
            self.add_new_url(url)
        return True

    # 3.是否有新的url
    def has_new_url(self):
        return len(self.new_urls) != 0

    # 4.获得新的url
    def get_new_url(self):
        url = self.new_urls.pop()
        self.old_urls.add(url)
        return url

    def get_new_url_set(self):
        return self.new_urls
