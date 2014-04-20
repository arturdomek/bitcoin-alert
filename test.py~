#! /usr/bin/env python
# -*- coding: utf-8 -*-

#importing wx files
import wx

#import the newly created GUI file
import gui

from Stock import *
from Analysis import *

import time
import datetime
import sys
from StringIO import StringIO

#inherit from the MainFrame created in wxFowmBuilder and create CalcFrame
class BitcoinApp(gui.MyFrame):
	#constructor
	def __init__(self,parent):
		#initialize parent class
		gui.MyFrame.__init__(self,parent) 
		
		self.timer_counter_ticker = 0
		self.timer_counter_alert = 0
		self.timer_counter_log = 0
		self.update_flag = 0
		self.handler_flag = 0
		self.new_panel_counter = 0
		self.Bitcurex = Bitcurex("https://pln.bitcurex.com/data/ticker.json")
		self.Bitstamp = Bitstamp("https://www.bitstamp.net/api/ticker/")
		self.BTCe = BTCe("https://btc-e.com/api/2/btc_usd/ticker")
		self.Bitcoincharts = Bitcoincharts("http://api.bitcoincharts.com/v1/markets.json")
		self.update_gui()
		
	#funkcja aktualizująca gui
	def update_gui(self):
		self.update_ticker()
		self.update_alert()

	#funckja aktualizujaca ticker
	def update_ticker(self):
		self.Bitcurex.Ticker.get(5)
		self.Bitstamp.Ticker.get(5)
		self.BTCe.Ticker.get(5)
		self.Bitcoincharts.get_all_data(5)
		if self.update_flag == 0:
			self.update_flag = 1
			self.Bitcoincharts.get_stock_list()
			self.generate_stock_list()
		#kod aktualizujacy wartosci z tickera
		if self.new_panel_counter > 0:
			#print "update ticker"
			for key in self.stockPanel.keys(): 
				symbol = self.Bitcoincharts.stock_list[self.stockPanel[key].stockID]
				try:
					ask = self.Bitcoincharts.get_ask(symbol)
					bid = self.Bitcoincharts.get_bid(symbol)
					high = self.Bitcoincharts.get_high(symbol)
					low = self.Bitcoincharts.get_low(symbol)
					last = self.Bitcoincharts.get_last(symbol)
					vwap = self.Bitcoincharts.get_vwap(symbol)
					volume = self.Bitcoincharts.get_volume(symbol)
					#time = self.Bitcoincharts.get_time(symbol)
					#uchwyty zakladki ticker
					self.askTextCtrl[key].SetValue(str(ask))
					self.bidTextCtrl[key].SetValue(str(bid))
					self.lowTextCtrl[key].SetValue(str(low))
					self.highTextCtrl[key].SetValue(str(high))
					self.priceTextCtrl[key].SetValue(str(last))
					self.avgTextCtrl[key].SetValue(str(vwap))
					self.volumeTextCtrl[key].SetValue(str(volume))
				except:
					print "Błąd: Nie udało się wyświetlić danych !!!"
	
				
	#funkcja aktualizująca alarmy
	def update_alert(self):
		if self.new_panel_counter > 0:
			#print "update alert"
			for key in self.stockPanel.keys():	 
				if self.stockPanel[key].alarmState == True:
					try:
						symbol = self.Bitcoincharts.stock_list[self.stockPanel[key].stockID]
						high = self.highAlertTextCtrl[key].GetValue()
						low = self.lowAlertTextCtrl[key].GetValue()
						last = self.Bitcoincharts.get_last(symbol)
						print self.stockPanel[key].Analysis.Indicators.Price_level.get_rmd(last, float(low), float(high))
					except:
						print "Błąd: Niepowodzenie w ustawieniu alarmu !!!"
			
	#funckja obsługująca wybór giełdy 
	def generate_stock_list(self):
		self.stockListbox.Set(self.Bitcoincharts.stock_list)
	
	#funkcja aktualizująca ogólnego przeznaczenia włączana co przerwanie timera
	def update(self, event):
		self.timer_counter_ticker += 1
		self.timer_counter_log += 1
		self.timer_counter_alert += 1
		
		if self.timer_counter_ticker >= 10:
			self.timer_counter_ticker = 0
			self.update_gui()
		
		if self.timer_counter_log >= 1:
			self.timer_counter_log = 0
			self.update_log()
		
		
	#funkcja aktualizująca logi włączana co przerwanie timera
	def update_log(self):
		#print datetime.datetime.now()
		#self.infoText.AppendText(log_string.getvalue())
		#print "update log"
		pass
	
	#funkcja autoscrolujaca info
	def autoscroll_info(self, event):
		self.infoText.ScrollIntoView(self.infoText.GetCaretPosition(), wx.WXK_PAGEDOWN)
	
	#funkcja ustawiajaca aktualny kurs jako poziom wysoki alarmu
	def high_level_set(self, event):
		button = event.GetEventObject()
		panel_id = button.ID
		symbol = self.Bitcoincharts.stock_list[self.stockPanel[panel_id].stockID]
		try:	
			last = self.Bitcoincharts.get_last(symbol)
			self.highAlertTextCtrl[panel_id].SetValue(str(last))
		except:
			print "Błąd: Nie udało się ustawić wysokiego poziomu alarmu"
			
	#funkcja ustawiajaca aktualny kurs jako poziom niski alarmu
	def low_level_set(self, event):
		button = event.GetEventObject()
		panel_id = button.ID
		symbol = self.Bitcoincharts.stock_list[self.stockPanel[panel_id].stockID]
		try:	
			last = self.Bitcoincharts.get_last(symbol)
			self.lowAlertTextCtrl[panel_id].SetValue(str(last))
		except:
			print "Błąd: Nie udało się ustawić niskiego poziomu alarmu"
	
	#funkcja zamykajaca panel
	def close_panel(self, event):
		button = event.GetEventObject()
		panel_id = button.ID
		self.stockPanel[panel_id].Destroy()
		self.stockPanel.pop(panel_id)
		self.askTextCtrl.pop(panel_id)
		self.bidTextCtrl.pop(panel_id)
		self.lowTextCtrl.pop(panel_id)
		self.highTextCtrl.pop(panel_id)
		self.priceTextCtrl.pop(panel_id)
		self.avgTextCtrl.pop(panel_id)
		self.volumeTextCtrl.pop(panel_id)
		self.highAlertTextCtrl.pop(panel_id)
		self.lowAlertTextCtrl.pop(panel_id)
		self.highLevelSetButton.pop(panel_id)
		self.lowLevelSetButton.pop(panel_id)
		self.remindAlertTextCtrl.pop(panel_id)
		self.highSoundAlertChoice.pop(panel_id)
		self.lowSoundAlertChoice.pop(panel_id)
		self.closeButton.pop(panel_id)
		self.alarmToggleButton.pop(panel_id)
		
	#funkcja wlaczajaca lub wylaczajaca alarm
	def toggle_alarm(self, event):
		button = event.GetEventObject()
		panel_id = button.ID
		self.stockPanel[panel_id].alarmState = button.GetValue()
	
	#funkcja powodująca generowanie nowej zakładki
	def generate_stock_panel(self, event):
		self.new_panel_counter += 1
		if self.stockListbox.GetSelections() != ():
			stock_select = self.stockListbox.GetSelections()[0]
			i = self.new_panel_counter
			#stworzenie słownika przechowującego uchwyty do kontrolek zakładki
			if self.handler_flag == 0:
				self.handler_flag = 1
				#uchwyty zakladki ticker
				self.stockPanel = {}
				self.askTextCtrl = {}
				self.bidTextCtrl = {}
				self.lowTextCtrl = {}
				self.highTextCtrl = {}
				self.priceTextCtrl = {}
				self.avgTextCtrl = {}
				self.volumeTextCtrl = {}
				#uchwyty zakladki alert
				self.highAlertTextCtrl = {}
				self.lowAlertTextCtrl = {}
				self.highLevelSetButton = {}
				self.lowLevelSetButton = {}
				self.remindAlertTextCtrl = {}
				self.highSoundAlertChoice = {}
				self.lowSoundAlertChoice = {}
				self.closeButton = {}
				self.alarmToggleButton = {}
			###tworzenie nowej zakładki
			self.stockPanel[i] = wx.Panel( self.myNotebook, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
			self.stockPanel[i].SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
			stockSizer = wx.FlexGridSizer( 1, 3, 0, 0 )
			stockSizer.SetFlexibleDirection( wx.BOTH )
			stockSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
			self.stockInternalPanel = wx.Panel( self.stockPanel[i], wx.ID_ANY, wx.Point( -1,-1 ), wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
			stockInternalPanelSizer = wx.FlexGridSizer( 0, 2, 0, 0 )
			stockInternalPanelSizer.SetFlexibleDirection( wx.BOTH )
			stockInternalPanelSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
			self.stockNotebook = wx.Notebook( self.stockInternalPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 680,-1 ), 0 )
			self.stockNotebook.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
			self.tickerPanel = wx.Panel( self.stockNotebook, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
			tickerSizer = wx.FlexGridSizer( 0, 2, 0, 0 )
			tickerSizer.SetFlexibleDirection( wx.BOTH )
			tickerSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
			tickerSizer2 = wx.GridSizer( 7, 2, 0, 0 )
		
			self.askText = wx.StaticText( self.tickerPanel, wx.ID_ANY, u"Ask", wx.DefaultPosition, wx.DefaultSize, 0 )
			self.askText.Wrap( -1 )
			self.askText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
			tickerSizer2.Add( self.askText, 0, wx.ALL, 5 )
		
			self.askTextCtrl[i] = wx.TextCtrl( self.tickerPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), wx.TE_READONLY )
			self.askTextCtrl[i].SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
			tickerSizer2.Add( self.askTextCtrl[i], 0, wx.ALL, 5 )
		
			self.priceText = wx.StaticText( self.tickerPanel, wx.ID_ANY, u"Price", wx.DefaultPosition, wx.DefaultSize, 0 )
			self.priceText.Wrap( -1 )
			self.priceText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
			tickerSizer2.Add( self.priceText, 0, wx.ALL, 5 )
		
			self.priceTextCtrl[i] = wx.TextCtrl( self.tickerPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
			tickerSizer2.Add( self.priceTextCtrl[i], 0, wx.ALL, 5 )
		
			self.bidText = wx.StaticText( self.tickerPanel, wx.ID_ANY, u"Bid", wx.DefaultPosition, wx.DefaultSize, 0 )
			self.bidText.Wrap( -1 )
			self.bidText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
			tickerSizer2.Add( self.bidText, 0, wx.ALL, 5 )
		
			self.bidTextCtrl[i] = wx.TextCtrl( self.tickerPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), wx.TE_READONLY )
			self.bidTextCtrl[i].SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
			tickerSizer2.Add( self.bidTextCtrl[i], 0, wx.ALL, 5 )
		
			self.lowText = wx.StaticText( self.tickerPanel, wx.ID_ANY, u"Low price", wx.DefaultPosition, wx.DefaultSize, 0 )
			self.lowText.Wrap( -1 )
			self.lowText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
			tickerSizer2.Add( self.lowText, 0, wx.ALL, 5 )
		
			self.lowTextCtrl[i] = wx.TextCtrl( self.tickerPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), wx.TE_READONLY )
			self.lowTextCtrl[i].SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
			tickerSizer2.Add( self.lowTextCtrl[i], 0, wx.ALL, 5 )
		
			self.highText = wx.StaticText( self.tickerPanel, wx.ID_ANY, u"High price", wx.DefaultPosition, wx.DefaultSize, 0 )
			self.highText.Wrap( -1 )
			self.highText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
			tickerSizer2.Add( self.highText, 0, wx.ALL, 5 )
		
			self.highTextCtrl[i] = wx.TextCtrl( self.tickerPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), wx.TE_READONLY )
			self.highTextCtrl[i].SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
			tickerSizer2.Add( self.highTextCtrl[i], 0, wx.ALL, 5 )
		
			self.avgText = wx.StaticText( self.tickerPanel, wx.ID_ANY, u"Average price", wx.DefaultPosition, wx.DefaultSize, 0 )
			self.avgText.Wrap( -1 )
			self.avgText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
			tickerSizer2.Add( self.avgText, 0, wx.ALL, 5 )
		
			self.avgTextCtrl[i] = wx.TextCtrl( self.tickerPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), wx.TE_READONLY )
			self.avgTextCtrl[i].SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
			tickerSizer2.Add( self.avgTextCtrl[i], 0, wx.ALL, 5 )
		
			self.volumeText = wx.StaticText( self.tickerPanel, wx.ID_ANY, u"Volume", wx.DefaultPosition, wx.DefaultSize, 0 )
			self.volumeText.Wrap( -1 )
			self.volumeText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
			tickerSizer2.Add( self.volumeText, 0, wx.ALL, 5 )
		
			self.volumeTextCtrl[i] = wx.TextCtrl( self.tickerPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), wx.TE_READONLY )
			self.volumeTextCtrl[i].SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
			tickerSizer2.Add( self.volumeTextCtrl[i], 0, wx.ALL, 5 )
		
		
			tickerSizer.Add( tickerSizer2, 1, wx.EXPAND, 5 )
		
			tickerSizer3 = wx.BoxSizer( wx.VERTICAL )
		
			self.chartPanel = wx.Panel( self.tickerPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), wx.TAB_TRAVERSAL )
			self.chartPanel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )
		
			chartSizer = wx.BoxSizer( wx.VERTICAL )
		
			self.chartBitmap = wx.StaticBitmap( self.chartPanel, wx.ID_ANY, wx.Bitmap( u"chart.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 290,245 ), 0 )
			chartSizer.Add( self.chartBitmap, 0, wx.ALL, 5 )
		
		
			self.chartPanel.SetSizer( chartSizer )
			self.chartPanel.Layout()
			tickerSizer3.Add( self.chartPanel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
			tickerSizer.Add( tickerSizer3, 1, wx.EXPAND, 5 )
		
		
			self.tickerPanel.SetSizer( tickerSizer )
			self.tickerPanel.Layout()
			tickerSizer.Fit( self.tickerPanel )
			self.stockNotebook.AddPage( self.tickerPanel, u"Ticker", True )
			self.alertPanel = wx.Panel( self.stockNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
			alertSizer = wx.GridSizer( 0, 3, 0, 0 )
		
			self.highAlertText = wx.StaticText( self.alertPanel, wx.ID_ANY, u"High level", wx.DefaultPosition, wx.DefaultSize, 0 )
			self.highAlertText.Wrap( -1 )
			self.highAlertText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
			alertSizer.Add( self.highAlertText, 0, wx.ALL, 5 )
		
			self.highAlertTextCtrl[i] = wx.TextCtrl( self.alertPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
			alertSizer.Add( self.highAlertTextCtrl[i], 0, wx.ALL, 5 )
		
			self.highLevelSetButton[i] = wx.Button( self.alertPanel, wx.ID_ANY, u"Last price as high", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
			alertSizer.Add( self.highLevelSetButton[i], 0, wx.ALL, 5 )
		
			self.lowAlertText = wx.StaticText( self.alertPanel, wx.ID_ANY, u"Low level", wx.DefaultPosition, wx.DefaultSize, 0 )
			self.lowAlertText.Wrap( -1 )
			self.lowAlertText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
			alertSizer.Add( self.lowAlertText, 0, wx.ALL, 5 )
		
			self.lowAlertTextCtrl[i] = wx.TextCtrl( self.alertPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
			alertSizer.Add( self.lowAlertTextCtrl[i], 0, wx.ALL, 5 )
		
			self.lowLevelSetButton[i] = wx.Button( self.alertPanel, wx.ID_ANY, u"Last price as low", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
			alertSizer.Add( self.lowLevelSetButton[i], 0, wx.ALL, 5 )
		
			self.remindAlertText = wx.StaticText( self.alertPanel, wx.ID_ANY, u"Remind me every [minutes]", wx.DefaultPosition, wx.DefaultSize, 0 )
			self.remindAlertText.Wrap( -1 )
			self.remindAlertText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
			alertSizer.Add( self.remindAlertText, 0, wx.ALL, 5 )
		
			self.remindAlertTextCtrl[i] = wx.TextCtrl( self.alertPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
			alertSizer.Add( self.remindAlertTextCtrl[i], 0, wx.ALL, 5 )
		
			self.emptyPanel = wx.Panel( self.alertPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
			alertSizer.Add( self.emptyPanel, 1, wx.EXPAND |wx.ALL, 5 )
		
			self.highSoundAlertText = wx.StaticText( self.alertPanel, wx.ID_ANY, u"High level sound", wx.DefaultPosition, wx.DefaultSize, 0 )
			self.highSoundAlertText.Wrap( -1 )
			self.highSoundAlertText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
			alertSizer.Add( self.highSoundAlertText, 0, wx.ALL, 5 )
		
			highSoundAlertChoices = [ u"ComputerMagic.wav", u"Movie.wav" ]
			self.highSoundAlertChoice[i] = wx.Choice( self.alertPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,-1 ), highSoundAlertChoices, 0 )
			self.highSoundAlertChoice[i].SetSelection( 0 )
			self.highSoundAlertChoice[i].SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
			alertSizer.Add( self.highSoundAlertChoice[i], 0, wx.ALL, 5 )
		
			self.emptyPanel2 = wx.Panel( self.alertPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
			alertSizer.Add( self.emptyPanel2, 1, wx.EXPAND |wx.ALL, 5 )
		
			self.lowSoundAlertText = wx.StaticText( self.alertPanel, wx.ID_ANY, u"Low level sound", wx.DefaultPosition, wx.DefaultSize, 0 )
			self.lowSoundAlertText.Wrap( -1 )
			self.lowSoundAlertText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
			alertSizer.Add( self.lowSoundAlertText, 0, wx.ALL, 5 )
		
			lowSoundAlertChoices = [ u"Buzzer.wav", u"Siren.wav" ]
			self.lowSoundAlertChoice[i] = wx.Choice( self.alertPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,-1 ), lowSoundAlertChoices, 0 )
			self.lowSoundAlertChoice[i].SetSelection( 0 )
			self.lowSoundAlertChoice[i].SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
			alertSizer.Add( self.lowSoundAlertChoice[i], 0, wx.ALL, 5 )
		
			self.emptyPanel3 = wx.Panel( self.alertPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
			alertSizer.Add( self.emptyPanel3, 1, wx.EXPAND |wx.ALL, 5 )
		
		
			self.alertPanel.SetSizer( alertSizer )
			self.alertPanel.Layout()
			alertSizer.Fit( self.alertPanel )
			self.stockNotebook.AddPage( self.alertPanel, u"Alert", False )
		
			stockInternalPanelSizer.Add( self.stockNotebook, 1, wx.EXPAND |wx.ALL, 5 )
		
		
			self.stockInternalPanel.SetSizer( stockInternalPanelSizer )
			self.stockInternalPanel.Layout()
			stockInternalPanelSizer.Fit( self.stockInternalPanel )
			stockSizer.Add( self.stockInternalPanel, 1, wx.EXPAND |wx.ALL, 5 )
		
			internalSizer = wx.BoxSizer( wx.VERTICAL )
		
			self.closeButton[i] = wx.Button( self.stockPanel[i], wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
			internalSizer.Add( self.closeButton[i], 0, wx.ALL, 5 )
		
			self.stockInternalPanelEmpty = wx.Panel( self.stockPanel[i], wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
			internalSizer.Add( self.stockInternalPanelEmpty, 1, wx.EXPAND |wx.ALL, 5 )
		
			self.alarmToggleButton[i] = wx.ToggleButton( self.stockPanel[i], wx.ID_ANY, u"Alarm", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
			internalSizer.Add( self.alarmToggleButton[i], 0, wx.ALL, 5 )
		
		
			stockSizer.Add( internalSizer, 1, wx.EXPAND, 5 )
		
		
			self.stockPanel[i].SetSizer( stockSizer )
			self.stockPanel[i].Layout()
			stockSizer.Fit( self.stockPanel[i] )
			self.myNotebook.AddPage( self.stockPanel[i], self.Bitcoincharts.stock_list[stock_select], True )
			
			#stworzenie nowych atrybutów dla panelu
			self.stockPanel[i].stockID = stock_select
			self.stockPanel[i].alarmState = False
			self.stockPanel[i].Analysis = Analysis()
			#dodawanie identyfikatorów paneli do przycisków
			self.highLevelSetButton[i].ID = i
			self.lowLevelSetButton[i].ID = i
			self.closeButton[i].ID = i
			self.alarmToggleButton[i].ID = i
			#bindowanie eventów
			self.highLevelSetButton[i].Bind( wx.EVT_BUTTON, self.high_level_set )
			self.lowLevelSetButton[i].Bind( wx.EVT_BUTTON, self.low_level_set )
			self.closeButton[i].Bind( wx.EVT_BUTTON, self.close_panel )
			self.alarmToggleButton[i].Bind( wx.EVT_TOGGLEBUTTON, self.toggle_alarm )
			
			#pobranie danych z tickera
			self.update_ticker()
			
#przekierowanie standardowego wyjścia do pliku
#sys.stdout = open("log.txt","a")
'''
old_stdout = sys.stdout
log_string = StringIO()
sys.stdout = log_string
'''
#mandatory in wx, create an app, False stands for not deteriction stdin/stdout
#refer manual for details
app = wx.App(False)
 
#create an object of CalcFrame
frame = BitcoinApp(None)
#show the frame
frame.Show(True)

#start the applications
app.MainLoop()


