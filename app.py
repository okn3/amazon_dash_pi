# -*- coding: utf-8 -*-
from __future__ import absolute_import
from flask import Flask
app = Flask(__name__)
import urllib2, urllib, urlparse
import os,sys


@app.route('/shoshu')
def notify_shoshu():
#    post_line(u"消臭力")
    os.system("open 'https://www.youtube.com/watch?v=s39_de-2dpQ'") # 消臭力のYoutubeを再生
    os.system("node /Users/okuno/Desktop/@worklog/20180107_google_home_hack/google-home-notifier/main2.js 消臭力") #googlehomeで喋らせる

@app.route('/furugura')
def notify_furugura():
    post_line(u"フルグラ")

@app.route('/')
def hello_world():
    return "hello from flask"

def post_line(message):
    url = u"https://notify-api.line.me/api/notify"
    message += u"買ってこい"
    params = {u"message":message.encode('utf-8')}
    params = urllib.urlencode(params)
    req = urllib2.Request(url)
    AT = "******************"
    #req.add_header(u"Authorization",u"Bearer "+os.environ[u"LINE_ACCESS_TOKEN"])
    req.add_header(u"Authorization",u"Bearer "+AT)
    req.add_data(params)

    res = urllib2.urlopen(req)
    r = res.read()
    print(r)

if __name__ == '__main__':
    app.run()
