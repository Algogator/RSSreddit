from .util import getXML, recurseXML

class BaseRSS(object):
    # URL = "http://www.reddit.com"
    def __init__(self, rss):
        self.URL = rss

    def make_request(self, arg):
        self.xml = getXML(self.URL+arg+"/.rss")
        if self.xml:
            return recurseXML(self.xml)

    def comments(self):
        return self.make_request("comments")
