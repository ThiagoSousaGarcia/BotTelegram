from datetime import datetime
import urllib as req
from bs4 import BeautifulSoup as bs

def getNoticiaTop():
	url = "http://legiaodosherois.uol.com.br/"
	site = req.urlopen(url).read()
	html = bs(site,"html.parser")
	valor = html.select("div.title-content h2 a ")[0]['href']
	
	
	return valor
	#return valor.get("value")


def response(msg):
	text = msg['text']
	now = datetime.now()
	if(text == '/start'):
		if(now.hour < 12):
			return "Bom dia, "+msg['from']['first_name']+"!"
		elif(now.hour < 18):
			return "Boa tarde, "+msg['from']['first_name']+"!"
		else:
			return "Boa noite, "+msg['from']['first_name']+"!"
	elif (text == "noticia nerd"):
		noticia = getNoticiaTop()
		mensagem = "A noticia nerd mais recente eh :  {}".format(noticia)
		return mensagem
	else:
		return eval(text)