# -*- coding: utf-8 -*-
from __future__ import absolute_import
from flask import Flask
app = Flask(__name__)
import urllib2, urllib, urlparse
import os,sys
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
LAT = os.environ.get("LINE_ACCESS_TOKEN")

@app.route('/shoshu')
def notify_shoshu():
#    post_line(u"消臭力")
    msg = "消臭力ボタンが押されました"
    play_google(msg=msg)

@app.route('/furugura')
def notify_furugura():
    #post_line(u"フルグラ")
    msg = "フルグラボタンが押されました"
    play_google("192.168.1.5", msg=msg)

@app.route('/nescafe')
def notify_nescafe():
    #post_line(u"フルグラ")
    msg = "ネスカフェが押されました"
    play_google(msg=msg)


def play_google(gh_ip="192.168.1.4", msg=None):
    """google homeに喋らせる
    @param gh_ip:google homeのipアドレス (default:google home mini)
    @param meg:喋らせる内容
    """
    os.system("node ~/Develop/g_h_hack/google-home-notifier/speak.js "+gh_ip+" "+msg) 

def post_line(message):
    url = u"https://notify-api.line.me/api/notify"
    message += u"買ってこい"
    params = {u"message":message.encode('utf-8')}
    params = urllib.urlencode(params)
    req = urllib2.Request(url)
    AT = "******************"
    #req.add_header(u"Authorization",u"Bearer "+os.environ[u"LINE_ACCESS_TOKEN"])
    req.add_header(u"Authorization",u"Bearer "+LAT)
    req.add_data(params)

    res = urllib2.urlopen(req)
    r = res.read()
    print(r)

if __name__ == '__main__':
    app.run()
