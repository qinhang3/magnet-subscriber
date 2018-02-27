# coding=UTF-8

import requests
from HTMLParser import HTMLParser


class Node:
    def __init__(self):
        self.sup = ''
        self.title = ''
        self.titleHref = ''
        self.attr = ''
        self.magnet = ''

    def add_data(self, tag, data):
        data.strip()
        if len(data) == 0:
            return
        if tag == 'sup':
            self.sup = data
        if tag == 'title':
            self.title = self.title + data
        if tag == 'titleHref':
            self.titleHref = data
        if tag == 'attr':
            self.attr = self.attr + data
        if tag == 'magnet':
            self.magnet = data


class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.stack = []
        self.data = []
        self.node = Node()

    def get_attr(self, attrs, key):
        for attr in attrs:
            if attr[0] == key:
                return attr[1]
        return None

    def handle_starttag(self, tag, attrs):
        self.stack.append(tag)
        if tag == 'dl':
            self.node = Node()
        if len(self.stack) > 4 and self.stack[-1] == 'a' and self.stack[-2] == 'span' and self.stack[-3] == 'dd' and self.stack[-4] == 'dl':
            self.node.add_data('magnet', self.get_attr(attrs, 'href'))
        if len(self.stack) > 3 and self.stack[-1] == 'a' and self.stack[-2] == 'dt' and self.stack[-3] == 'dl':
            self.node.add_data('titleHref', self.get_attr(attrs, 'href'))

    def handle_endtag(self, tag):
        if tag == 'dl':
            self.data.append(self.node)
            # print('sup', self.node.sup)
            # print('title', self.node.title)
            # print('attr', self.node.attr)
            # print('titleHref', self.node.titleHref)
            # print('magnet', self.node.magnet)
            # print('---------------------')

        while self.stack[-1] != tag:
            self.stack.pop()
        self.stack.pop()

    def handle_data(self, data):
        if len(self.stack) > 0 and self.stack[-1] == 'sup':
            self.node.add_data('sup', data)
        if len(self.stack) > 3 and self.stack[-1] == 'a' and self.stack[-2] == 'dt' and self.stack[-3] == 'dl':
            self.node.add_data('title', data)
        if len(self.stack) > 4 and self.stack[-1] == 'b' and self.stack[-2] == 'a' and self.stack[-3] == 'dt' and self.stack[-4] == 'dl':
            self.node.add_data('title', data)
        if len(self.stack) > 3 and self.stack[-1] == 'span' and self.stack[-2] == 'dd' and self.stack[-3] == 'dl':
            self.node.add_data('attr', data)
        if len(self.stack) > 4 and self.stack[-1] == 'b' and self.stack[-2] == 'span' and self.stack[-3] == 'dd' and self.stack[-4] == 'dl':
            self.node.add_data('attr', data + ' | ')

    def get_nodes(self):
        return self.data


def work(url, timeout):
    r = requests.get(url, timeout=timeout)
    # r = requests.get('http://cilifanhao.org/q/snis-703/1/4/0.html', timeout=10,
    # proxies={'http': 'socks5://127.0.0.1:1080'})
    parser = MyHTMLParser()
    parser.feed(r.text)
    return parser.get_nodes()
