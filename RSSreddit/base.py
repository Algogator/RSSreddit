from .util import getXML, recurseXML

class BaseRSS(object):

    def __init__(self, rss):
        # print(rss)
        self.xml = getXML(rss+"/.rss")
        self.json = recurseXML(self.xml)
