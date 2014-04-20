#! /usr/bin/env python
# -*- coding: utf-8 -*-



#klasa Analysis - zawiera instancje różnych metod analizy technicznej
class Analysis(object):
	def __init__(self):
		self.Indicators = Indicators() 	#instancja klasy zawierająca wskaźniki analizy technicznej
		self.Forms = Forms() 						#instancja klasy zawierająca formacje analizy technicznej

#klasa Indicators - wskaźniki analizy technicznej
class Indicators(object):
	def __init__(self):
		self.Price_level = Price_level() #testuje zdefiniowany przez użytkownika poziom ceny
		self.Avg_level = Avg_level() 		#sprawdza czy cena nie przekroczyła wartości średniej z 24h

##poszczególne implementacje wskaźników analizy technicznej
class Price_level(object):
	u"""Wskaźnik testujący poziom cen zdefiniowany przez użytkownika"""
	def __init__(self):
		self.rmd = 'noworking'						#rekomendacja
	
	def get_rmd(self, price, lower_bound, upper_bound):
		u"""
		Funkcja przyjmuje argumenty:
		price - cena aktualna
		lower_bound - dolne ograniczenie ceny
		upper_bound - górne ograniczenie ceny
		"""
		#sprawdzenie poprawności poziomów cen
		if upper_bound >= lower_bound:
			if price > upper_bound:
				self.rmd = 'sell'
			elif price < lower_bound:
				self.rmd = 'buy'
			else:
				self.rmd = 'hold'
		else:
			print "Błąd: Niepoprawne wartości poziomów cen w Price_level !!!"
			self.rmd = 'noworking'
		return self.rmd

class Avg_level(object):
	u"""Wskaźnik sprawdzający czy cena nie przekroczyła wartości średniej z 24h"""
	def __init__(self):
		self.rmd = 'noworking'						#rekomendacja
	
	def get_rmd(self, price, avg_price, coeff):
		u"""
		Funkcja przyjmuje argumenty:
		price - cena aktualna
		avg_price - średnia cena z 24h
		coeff - współczynnik odchylenia od średniej np. 0.05 to 5% odchylenia od średniej
		"""
		#sprawdzenie poprawności współczynnika coeff
		if 0 <= coeff <= 1:
			if price > (avg_price*(1+coeff)):
				self.rmd = 'sell'
			elif price < (avg_price*(1-coeff)):
				self.rmd = 'buy'
			else:
				self.rmd = 'hold'
		else:
			print "Błąd: Niepoprawna wartość współczynnika coeff w Avg_level !!!"
			self.rmd = 'noworking'
		return self.rmd


#klasa Forms - formacje analizy technicznej
class Forms(object):
	def __init__(self):
		pass

##poszczególne implementacje formacji analizy techniczej





#testowanie
if __name__ == "__main__":
	
	analiza = Analysis()
	print analiza.Indicators.Price_level.get_rmd(1600,1300,1500)
	print analiza.Indicators.Avg_level.get_rmd(1200,1300,0.05)
	
	
	
	
	


