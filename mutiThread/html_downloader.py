# coding=utf-8
import urllib2


class HtmlDownLoader(object):
    # 下载内容
    def download(self, new_url):
        if new_url is None:
            return None
        response = urllib2.urlopen(new_url)
        if response.getcode() != 200:
            return None
        return response.read()
