# -*- coding: utf-8 -*-
from .base import BaseRSS

class subreddit(BaseRSS):

    URL = "http://www.reddit.com/r/"

    def __init__(self, rss):
        BaseRSS.__init__(self, subreddit.URL+rss)


class user(BaseRSS):

    URL = "http://www.reddit.com/user/"

    def __init__(self, rss):
        BaseRSS.__init__(self, subreddit.URL+rss)
