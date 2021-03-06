#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import getopt
import requests
import time


#klasa Ticker pobiera dane z serwera i wyświetla je w konsoli
class Ticker(object):
	def __init__(self, url):
		self.url = url
		self.data = ()
	def get(self, user_timeout):
		try:
			self.data = requests.get(self.url, timeout = user_timeout).json()
		except:
			print "Błąd: Brak połączenia z serwerem !!!"
		else:	
			return self.data

#klasa Stock - nadklasa, ogólny opis giełdy, dziedziczą po niej klasy wyspecjalizowane do obsługi poszczególnych giełd
class Stock(object):
	def __init__(self, url):
		self.Ticker = Ticker(url)

#klasa Bitcurex - klasa zawierająca metody do obsługi tej giełdy
class Bitcurex(Stock):
	def __init__(self, url):
		Stock.__init__(self, url)
	
	#metody pobierająca dane z Tickera
	def get_ask(self):
		return self.Ticker.data['sell']
	
	def get_bid(self):
		return self.Ticker.data['buy']
	
	def get_high(self):
		return self.Ticker.data['high']
	
	def get_low(self):
		return self.Ticker.data['low']
	
	def get_last(self):
		return self.Ticker.data['last']
	
	def get_vwap(self):
		return self.Ticker.data['vwap']
	
	def get_volume(self):
		return self.Ticker.data['vol']
	
	def get_time(self):
		return self.Ticker.data['time']

#klasa Bitstamp - klasa zawierająca metody do obsługi tej giełdy
class Bitstamp(Stock):
	def __init__(self, url):
		Stock.__init__(self, url)
	
	#metody pobierająca dane z Tickera
	def get_ask(self):
		return self.Ticker.data['ask']
	
	def get_bid(self):
		return self.Ticker.data['bid']
	
	def get_high(self):
		return self.Ticker.data['high']
	
	def get_low(self):
		return self.Ticker.data['low']
	
	def get_last(self):
		return self.Ticker.data['last']
	
	def get_vwap(self):
		return self.Ticker.data['vwap']
	
	def get_volume(self):
		return self.Ticker.data['volume']
	
	def get_time(self):
		return self.Ticker.data['timestamp']

#klasa BTCe - klasa zawierająca metody do obsługi tej giełdy
class BTCe(Stock):
	def __init__(self, url):
		Stock.__init__(self, url)
	
	#metody pobierająca dane z Tickera
	def get_ask(self):
		return self.Ticker.data['ticker']['buy']
	
	def get_bid(self):
		return self.Ticker.data['ticker']['sell']
	
	def get_high(self):
		return self.Ticker.data['ticker']['high']
	
	def get_low(self):
		return self.Ticker.data['ticker']['low']
	
	def get_last(self):
		return self.Ticker.data['ticker']['last']
	
	def get_vwap(self):
		return self.Ticker.data['ticker']['avg']
	
	def get_volume(self):
		return self.Ticker.data['ticker']['vol_cur']
	
	def get_time(self):
		return self.Ticker.data['ticker']['server_time']

#klasa Bitcoincharts - klasa zawierająca metody do obsługi tej giełdy
class Bitcoincharts(Stock):
	def __init__(self, url):
		Stock.__init__(self, url)
		self.bitcoincharts_data = {}
		self.stock_list = []
	
	def get_all_data(self, timeout):
		self.Ticker.get(timeout)
		for i in range(len(self.Ticker.data)):
			stock_name = self.Ticker.data[i]['symbol']
			self.bitcoincharts_data[stock_name] = self.Ticker.data[i]
		return self.bitcoincharts_data
	
	def get_stock_list(self):
		self.stock_list = self.bitcoincharts_data.keys() 
		return self.stock_list.sort()
	
	#metody pobierająca dane z Tickera
	def get_ask(self, symbol):
		return self.bitcoincharts_data[symbol]['ask']
	
	def get_bid(self, symbol):
		return self.bitcoincharts_data[symbol]['bid']
	
	def get_high(self, symbol):
		return self.bitcoincharts_data[symbol]['high']
	
	def get_low(self, symbol):
		return self.bitcoincharts_data[symbol]['low']
	
	def get_last(self, symbol):
		return self.bitcoincharts_data[symbol]['close']
	
	def get_vwap(self, symbol):
		return self.bitcoincharts_data[symbol]['avg']
	
	def get_volume(self, symbol):
		return self.bitcoincharts_data[symbol]['volume']
	
	def get_time(self, symbol):
		return self.bitcoincharts_data[symbol]['time']

#testowanie
if __name__ == "__main__":
	
	#sys.stdout = open("log.txt","a")
	gielda = Bitcurex("https://pln.bitcurex.com/data/ticker.json")
	gielda2 = Bitstamp("https://www.bitstamp.net/api/ticker/")
	gielda3 = BTCe("https://btc-e.com/api/2/btc_usd/ticker")
	gielda4 = Bitcoincharts("http://api.bitcoincharts.com/v1/markets.json")
	'''
	gielda.Ticker.get(30)
	print 'Bitcurex: ',gielda.get_last(),'\n'
	
	gielda2.Ticker.get(30)
	print 'Bitstamp: ',gielda2.get_last(),'\n'
	
	gielda3.Ticker.get(30)
	print 'Btce: ',gielda3.get_last(),'\n'
	'''
	gielda4.get_all_data(30)
	#print gielda4.bitcoincharts_data['bitcurexPLN']
	print gielda4.get_bid('bitcurexPLN')

