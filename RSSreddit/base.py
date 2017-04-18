from .util import getXML, recurseXML

class BaseRSS(object):

    def __init__(self, rss):
        # print(rss+"/.rss")
        self.xml = getXML(rss+"/.rss")
        if self.xml:
            self.json = recurseXML(self.xml)
