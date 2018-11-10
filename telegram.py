#!-*- conding: utf8 -*-
import telepot
import util as ut
import time
import urllib as req
from bs4 import BeautifulSoup as bs

bot = telepot.Bot("481230590:AAHr0Eq8FIhtt1PkX1AKoTRGOi_8G6yb7ac")


def recebendoMsg(msg):
	id = msg['from']['id']
	print(msg)
	bot.sendMessage(id,ut.response(msg))

bot.message_loop(recebendoMsg)
ut.getNoticiaTop()
while(True):
	#pass
	time.sleep(1) 
