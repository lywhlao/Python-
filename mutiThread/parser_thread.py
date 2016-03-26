# coding=utf-8
import Queue
import threading

from mutiThread import url_manager, html_parser


class ParserThread(threading.Thread):
    def __init__(self, queue, lock, urls, parser, outputer, condition):
        super(ParserThread, self).__init__()
        self.queue = queue
        self.lock = lock
        self.urls = urls
        self.parser = parser
        self.outputer = outputer
        self.condition = condition

    def run(self):
        while True:
            argus = self.queue.get()
            # 解析内容
            new_urls, new_content = self.parser.parse(argus[0], argus[1])
            # 添加url
            self.condition.acquire()
            is_add_new_urls = self.urls.add_new_urls(new_urls)
            if is_add_new_urls:
                self.condition.notify_all()
            self.condition.release()
            # 写入文件
            if new_content is None:
                continue
            self.outputer.collect_data(new_content)
            if self.outputer.get_data_length() % 50 == 0:
                self.outputer.output_html()
