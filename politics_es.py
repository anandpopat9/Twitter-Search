# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
import requests
from requests_oauthlib import OAuth1
from urlparse import parse_qs
import json
import time
global m
m=1
file1 = open("/Users/anandpopat/Downloads/a/politics_es.json","a")
file2 = open("/Users/anandpopat/Downloads/a/politics_es2.json","a")


REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"

CONSUMER_KEY = "aVCgyYsyFJkfspdbqLInkjzDa"
CONSUMER_SECRET = "vO2gNtNdhzbGbHvNbYqJQ0r5FDdytVZ4IP2lXiUVu4cTdoNsne"

OAUTH_TOKEN = "1157867358-2dv3Krqk7VHWFK4oTQAlJsn0XvOZ2ubFZ3MYABW"
OAUTH_TOKEN_SECRET = "vUMy3URh5vhZU1X8ja1hJ6lFFgEcxCALY1qIpxbBTTgsp"


def setup_oauth():
    """Authorize your app via identifier."""
    # Request token
    oauth = OAuth1(CONSUMER_KEY, client_secret=CONSUMER_SECRET)
    r = requests.post(url=REQUEST_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)

    resource_owner_key = credentials.get('oauth_token')[0]
    resource_owner_secret = credentials.get('oauth_token_secret')[0]

    # Authorize
    authorize_url = AUTHORIZE_URL + resource_owner_key
    print 'Please go here and authorize: ' + authorize_url

    verifier = raw_input('Please input the verifier: ')
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=resource_owner_key,
                   resource_owner_secret=resource_owner_secret,
                   verifier=verifier)

    # Finally, Obtain the Access Token
    r = requests.post(url=ACCESS_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)
    token = credentials.get('oauth_token')[0]
    secret = credentials.get('oauth_token_secret')[0]

    return token, secret


def get_oauth():
    oauth = OAuth1(CONSUMER_KEY,
                client_secret=CONSUMER_SECRET,
                resource_owner_key=OAUTH_TOKEN,
                resource_owner_secret=OAUTH_TOKEN_SECRET)
    return oauth

if __name__ == "__main__":
    if not OAUTH_TOKEN:
        token, secret = setup_oauth()
        print "OAUTH_TOKEN: " + token
        print "OAUTH_TOKEN_SECRET: " + secret
        print
    else:
        file1.write('{"anand":[')
        var = 773357768724058112-1
        oauth = get_oauth()
        r = requests.get(url="https://api.twitter.com/1.1/search/tweets.json?q=%40hillaryclinton%20OR%20%23hillaryclinton%20OR%20%23hillary%20OR%20%40realdonaldtrump%20OR%20%23trump&lang=es&count=100", auth=oauth)
        for tweet in r:
            file1.write(tweet)
        #file1.write(',')
        tweet=r.json()
        no = 1
        try:
            for a in tweet['statuses']:
                id_anand=a['id']
                #print no
                print str(id_anand)+"------"+str(no)+"-------"+str(m)
                #print ". "
                #print id_anand
                no = no + 1
                m = m + 1
                id_anand1=id_anand-1
        except IndexError:    
            print "error"
        try:
            for v in range(0,30):
               file1.write(',')
               r = requests.get(url="https://api.twitter.com/1.1/search/tweets.json?q=%40hillaryclinton%20OR%20%23hillaryclinton%20OR%20%23hillary%20OR%20%40realdonaldtrump%20OR%20%23trump&lang=es&count=100&max_id="+str(id_anand1), auth=oauth)
               for tweet in r:
                   file1.write(tweet)
               
               tweet=r.json()
               no = 1
               for a in tweet['statuses']:
                   id_anand=a['id']
                   #print m
                   print str(id_anand)+"------"+str(no)+"-------"+str(m)
                   #print ". "
                   #print id_anand
                   no = no + 1
                   m = m + 1
                   id_anand1=id_anand-1
            file2.write('{"anand":[')
            for v in range(0,30):
               file2.write(',')
               r = requests.get(url="https://api.twitter.com/1.1/search/tweets.json?q=%40hillaryclinton%20OR%20%23hillaryclinton%20OR%20%23hillary%20OR%20%40realdonaldtrump%20OR%20%23trump&lang=es&count=100&max_id="+str(id_anand1), auth=oauth)
               for tweet in r:
                   file2.write(tweet)
               
               tweet=r.json()
               no = 1
               for a in tweet['statuses']:
                   id_anand=a['id']
                   #print m
                   print str(id_anand)+"------"+str(no)+"-------"+str(m)
                   #print ". "
                   #print id_anand
                   no = no + 1
                   m = m + 1
                   id_anand1=id_anand-1
        except IndexError:
          print "error"
            