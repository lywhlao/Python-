# coding=utf-8
import Queue
import threading

from mutiThread import url_manager, html_downloader


class DownLoadThread(threading.Thread):
    def __init__(self, queue, lock, urls, downloader, condition):
        super(DownLoadThread, self).__init__()
        self.queue = queue
        self.lock = lock
        self.urls = urls
        self.stopFlag = False
        self.downloader = downloader
        self.condition = condition
        self.count = 0

    def run(self):
        # 判断是否还有新的url
        while self.get_new_url_state() and not self.stopFlag:
            try:
                self.condition.acquire()
                new_url = self.urls.get_new_url()
                print "count=%s" % self.count, " new url: ", new_url
                self.count += 1
                self.condition.release()
                # 下载数据
                html_content = self.downloader.download(new_url)
                # 存放数据
                self.queue.put([new_url, html_content])
            except:
                print("craw faild")

    def set_stop_flag(self, stop_flag):
        self.stopFlag = stop_flag

    # 是否有新的url
    def get_new_url_state(self):
        self.condition.acquire()
        value = self.urls.has_new_url()
        if not value:
            self.condition.wait()
        self.condition.release()
        value = self.urls.has_new_url()
        return value
