"""Provide subreddit and user class."""
from .base import BaseRSS

class subreddit(BaseRSS):

    """Generate a subreddit instance."""

    def __init__(self, rss, category = ""):
        BaseRSS.__init__(self, ("http://www.reddit.com/r/{0}/{1}").format(rss,category))


class user(BaseRSS):

    def __init__(self, rss):
        BaseRSS.__init__(self, ("http://www.reddit.com/user/{0}").format(rss))
