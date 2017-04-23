"""Provide subreddit and user class."""
from .base import BaseRSS

class subreddit(BaseRSS):

    """Generate a subreddit instance."""

    def __init__(self, rss):
        BaseRSS.__init__(self, ("http://www.reddit.com/r/{0}/").format(rss))

    def hot(self):
        return self.make_request("hot")

    def top(self, arg):
        return self.make_request("top")

    def controversial(self, arg):
        return self.make_request("controversial")

    def new(self, arg):
        return self.make_request("new")

    def gilded(self, arg):
        return self.make_request("gilded")

class user(BaseRSS):

    def __init__(self, rss):
        BaseRSS.__init__(self, ("http://www.reddit.com/user/{0}").format(rss))
