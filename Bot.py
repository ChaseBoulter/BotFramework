import URLFunctions
import os
import sys
import time


class Bot(object):

    def __init__(self, botType, dbURL, ccURL):
        self._bot_type = botType
        self._db_url = dbURL
        self._cc_url = ccURL

    @staticmethod
    def sleep():
            print "No work found...sleeping for 10 seconds..."
            time.sleep(10)

    def getTarget(self):
        return URLFunctions.GetURL("http://", self._cc_url)
