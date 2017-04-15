# -*- coding: utf-8 -*-

import requests
from xml.etree import ElementTree
import re
import json


class RSSreddit(object):

    subreddit = "http://www.reddit.com/.rss"
    tree = None

    def __init__(self, url=subreddit):

        response = requests.get(url, headers={'User-agent': 'RSSreddit'})
        print(response)
        data = ElementTree.fromstring(response.content)
        RSSreddit.tree = self.recurse(data)

        # return self.dati

    def recurse(self, element):
        dati = {}
        for elem in element:
            item = self.tag_name(elem)
            print(item)
            if type(elem.text) is str:
                dati[item] = elem.text
            elif elem.attrib:
                if item in dati:
                    dati[item].append(elem.attrib)
                else:
                    dati[item] = [elem.attrib]
            else:
                if item in dati:
                    dati[item].append(self.recurse(elem))
                else:
                    dati[item] = [self.recurse(elem)]
        return dati


    def __str__(self):
        print(str(RSSreddit.tree))

    def tag_name(self, tag):
        return re.findall(r'}(\w+)', tag.tag)[0] or None
