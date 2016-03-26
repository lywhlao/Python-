# coding=utf-8
import re
import urlparse

from  bs4 import BeautifulSoup


class HtmlParser(object):
    # 1.解析数据
    # 2.解析Url
    def parse(self, new_url, html_content):
        if new_url is None or html_content is None:
            return
        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(new_url, soup)
        new_data = self._get_new_data(new_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        url_set = set()
        # 查找链接
        links = soup.find_all('a', href=re.compile(r"/view/\d+\.htm"))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            url_set.add(new_full_url)
        return url_set

        # 标题 <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        # 内容<div class="lemma-summary" label-module="lemmaSummary">

    def _get_new_data(self, new_url, soup):
        res_data = {}
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        summay_node = soup.find('div', class_='lemma-summary')
        if summay_node is not None:
            res_data['title'] = title_node.get_text()
            res_data['summary'] = summay_node.get_text()
            res_data['url'] = new_url
        return res_data
