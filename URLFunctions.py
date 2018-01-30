# URLFunctions.py
# Copyright 2011 - LiveSquare Security and Brett L. Scott - All rights reserved worldwide.

# This script is a centralized monitor of the LiveSquare Security Proactive Defense Network(tm).
# This script is CONFIDENTIAL AND PROPRIETARY.  If you are not currently employed by
# LiveSquare Security, please close this file now and make no further attempts to read this
# file's contents.



# All contents below are CONFIDENTIAL and PROPRIETARY.

import httplib, urllib, urllib2


def GetURL(sURL, sParameters):
    sScriptVer = "1.0.0"

    # Do we need to append the HTTP part?
    if sURL.find("http://") == -1:
		sURL = "http://" + sURL

    # Do we have parameters
    if sParameters == "":
        req = urllib2.Request(sURL)
        req.add_header('User-agent', 'ScottNet Neuralizer Python (' + sScriptVer + ')')
        try:
            response = urllib2.urlopen(req)
        except urllib2.URLError, e:
            if hasattr(e, 'reason'):
                print 'We failed to reach a server.'
                print 'Reason: ', e.reason
                sGetURLResponse = "URLFunctions.GetURL resulted in ERROR."
            elif hasattr(e, 'code'):
                print 'The server couldn\'t fulfill the request.'
                print 'Error code: ', e.code
                print "Retreival error"
                sGetURLResponse = "URLFunctions.GetURL resulted in ERROR."
        else:
            sGetURLResponse = response.read()
            sGetURLResponse = str(sGetURLResponse)
    else:
        # Encode the Parameters
        sParameters = sParameters.replace(" ", "+")
        req = urllib2.Request(sURL, sParameters)
        req.add_header('User-agent', 'ScottNet Neuralizer Python (' + sScriptVer + ')')
        try:
            response = urllib2.urlopen(req)
        except urllib2.URLError, e:
            if hasattr(e, 'reason'):
                print 'We failed to reach a server.'
                print 'Reason: ', e.reason
                sGetURLResponse = "URLFunctions.GetURL resulted in ERROR."
            elif hasattr(e, 'code'):
                print 'The server couldn\'t fulfill the request.'
                print 'Error code: ', e.code
                print "Retreival error"
                sGetURLResponse = "URLFunctions.GetURL resulted in ERROR."
        else:
            sGetURLResponse = response.read()
            sGetURLResponse = str(sGetURLResponse)

    return sGetURLResponse


def GetURLSSL(sURL, sParameters):
    sScriptVer = "1.0.0"

    # Do we need to append the HTTP part?
    if sURL.find("https://") == -1:
        sURL = "https://" + sURL

    # Do we have parameters
    if sParameters == "":
        req = urllib2.Request(sURL)
        req.add_header('User-agent', 'ScottNet Neuralizer Python (' + sScriptVer + ')')
        try:
            response = urllib2.urlopen(req)
        except urllib2.URLError, e:
            if hasattr(e, 'reason'):
                print 'We failed to reach a server.'
                print 'Reason: ', e.reason
            elif hasattr(e, 'code'):
                print 'The server couldn\'t fulfill the request.'
                print 'Error code: ', e.code
                print "Retreival error"
                sGetURLResponse = "URLFunctions.GetURLSSL resulted in ERROR."
        else:
            sGetURLResponse = response.read()
            sGetURLResponse = str(sGetURLResponse)
    else:
        sParameters = sParameters.replace(" ", "+")
        req = urllib2.Request(sURL, sParameters)
        req.add_header('User-agent', 'ScottNet Neuralizer Python (' + sScriptVer + ')')
        try:
            response = urllib2.urlopen(req)
        except urllib2.URLError, e:
            if hasattr(e, 'reason'):
                print 'We failed to reach a server.'
                print 'Reason: ', e.reason
            elif hasattr(e, 'code'):
                print 'The server couldn\'t fulfill the request.'
                print 'Error code: ', e.code
                print "Retreival error"
                sGetURLResponse = "URLFunctions.GetURLSSL resulted in ERROR."
        else:
            sGetURLResponse = response.read()
            sGetURLResponse = str(sGetURLResponse)

    return sGetURLResponse
