# coding=utf-8
import Queue
import threading

from mutiThread import url_manager, html_downloader, html_parser, html_output, down_load_thread, parser_thread

root_url = "http://baike.baidu.com/link?url=bmnlVcU6lZo5EbyvNbeEU-2SRq" \
           "lP0f_gqp1RucW2aO5ap3au4WiwT5CFl8tzzctXA_1XbDu1v-6gzh6QuALJAK"

# 初始化参数
urls = url_manager.UrlManager()
downloader = html_downloader.HtmlDownLoader()
parser = html_parser.HtmlParser()
outputer = html_output.HtmlOuter()
queue = Queue.Queue(2)
lock = threading.RLock()
condition = threading.Condition()

urls.add_new_url(root_url)
# 开启线程
work_down_load_thread = down_load_thread.DownLoadThread(queue, lock, urls, downloader, condition)
work_parser_thread = parser_thread.ParserThread(queue, lock, urls, parser, outputer, condition)
# 启动线程
work_down_load_thread.start()
work_parser_thread.start()
