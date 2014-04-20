# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Feb 26 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext

###########################################################################
## Class MyFrame
###########################################################################

class MyFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Bitcoin Stock Analyzer v0.1", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		mySizer = wx.FlexGridSizer( 2, 1, 0, 0 )
		mySizer.SetFlexibleDirection( wx.BOTH )
		mySizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.myPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		myPanelSizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		myPanelSizer.SetFlexibleDirection( wx.BOTH )
		myPanelSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.myNotebook = wx.Notebook( self.myPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 800,-1 ), 0 )
		self.myNotebook.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, "Arial" ) )
		
		self.newStockPanel = wx.Panel( self.myNotebook, wx.ID_ANY, wx.Point( -1,-1 ), wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		self.newStockPanel.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		newStockSizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		newStockSizer.SetFlexibleDirection( wx.BOTH )
		newStockSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		stockListboxChoices = []
		self.stockListbox = wx.ListBox( self.newStockPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,300 ), stockListboxChoices, wx.LB_ALWAYS_SB|wx.LB_HSCROLL|wx.LB_SINGLE )
		newStockSizer.Add( self.stockListbox, 0, wx.ALL, 5 )
		
		self.choiceButton = wx.Button( self.newStockPanel, wx.ID_ANY, u"choice", wx.DefaultPosition, wx.DefaultSize, 0 )
		newStockSizer.Add( self.choiceButton, 0, wx.ALL, 5 )
		
		
		self.newStockPanel.SetSizer( newStockSizer )
		self.newStockPanel.Layout()
		newStockSizer.Fit( self.newStockPanel )
		self.myNotebook.AddPage( self.newStockPanel, u"+", False )
		self.stockPanel = wx.Panel( self.myNotebook, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		self.stockPanel.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		stockSizer = wx.FlexGridSizer( 1, 3, 0, 0 )
		stockSizer.SetFlexibleDirection( wx.BOTH )
		stockSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.stockInternalPanel = wx.Panel( self.stockPanel, wx.ID_ANY, wx.Point( -1,-1 ), wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
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
		
		self.askTextCtrl = wx.TextCtrl( self.tickerPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), wx.TE_READONLY )
		self.askTextCtrl.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		tickerSizer2.Add( self.askTextCtrl, 0, wx.ALL, 5 )
		
		self.priceText = wx.StaticText( self.tickerPanel, wx.ID_ANY, u"Price", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.priceText.Wrap( -1 )
		self.priceText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		tickerSizer2.Add( self.priceText, 0, wx.ALL, 5 )
		
		self.priceTextCtrl = wx.TextCtrl( self.tickerPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), 0 )
		tickerSizer2.Add( self.priceTextCtrl, 0, wx.ALL, 5 )
		
		self.bidText = wx.StaticText( self.tickerPanel, wx.ID_ANY, u"Bid", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bidText.Wrap( -1 )
		self.bidText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		tickerSizer2.Add( self.bidText, 0, wx.ALL, 5 )
		
		self.bidTextCtrl = wx.TextCtrl( self.tickerPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), wx.TE_READONLY )
		self.bidTextCtrl.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		tickerSizer2.Add( self.bidTextCtrl, 0, wx.ALL, 5 )
		
		self.lowText = wx.StaticText( self.tickerPanel, wx.ID_ANY, u"Low price", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lowText.Wrap( -1 )
		self.lowText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		tickerSizer2.Add( self.lowText, 0, wx.ALL, 5 )
		
		self.lowTextCtrl = wx.TextCtrl( self.tickerPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), wx.TE_READONLY )
		self.lowTextCtrl.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		tickerSizer2.Add( self.lowTextCtrl, 0, wx.ALL, 5 )
		
		self.highText = wx.StaticText( self.tickerPanel, wx.ID_ANY, u"High price", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.highText.Wrap( -1 )
		self.highText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		tickerSizer2.Add( self.highText, 0, wx.ALL, 5 )
		
		self.highTextCtrl = wx.TextCtrl( self.tickerPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), wx.TE_READONLY )
		self.highTextCtrl.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		tickerSizer2.Add( self.highTextCtrl, 0, wx.ALL, 5 )
		
		self.avgText = wx.StaticText( self.tickerPanel, wx.ID_ANY, u"Average price", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.avgText.Wrap( -1 )
		self.avgText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		tickerSizer2.Add( self.avgText, 0, wx.ALL, 5 )
		
		self.avgTextCtrl = wx.TextCtrl( self.tickerPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), wx.TE_READONLY )
		self.avgTextCtrl.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		tickerSizer2.Add( self.avgTextCtrl, 0, wx.ALL, 5 )
		
		self.volumeText = wx.StaticText( self.tickerPanel, wx.ID_ANY, u"Volume", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.volumeText.Wrap( -1 )
		self.volumeText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		tickerSizer2.Add( self.volumeText, 0, wx.ALL, 5 )
		
		self.volumeTextCtrl = wx.TextCtrl( self.tickerPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 170,-1 ), wx.TE_READONLY )
		self.volumeTextCtrl.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		tickerSizer2.Add( self.volumeTextCtrl, 0, wx.ALL, 5 )
		
		
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
		self.stockNotebook.AddPage( self.tickerPanel, u"Ticker", False )
		self.alertPanel = wx.Panel( self.stockNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		alertSizer = wx.GridSizer( 0, 3, 0, 0 )
		
		self.highAlertText = wx.StaticText( self.alertPanel, wx.ID_ANY, u"High level", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.highAlertText.Wrap( -1 )
		self.highAlertText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		alertSizer.Add( self.highAlertText, 0, wx.ALL, 5 )
		
		self.highAlertTextCtrl = wx.TextCtrl( self.alertPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		alertSizer.Add( self.highAlertTextCtrl, 0, wx.ALL, 5 )
		
		self.highLevelSetButton = wx.Button( self.alertPanel, wx.ID_ANY, u"Last price as high", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		alertSizer.Add( self.highLevelSetButton, 0, wx.ALL, 5 )
		
		self.lowAlertText = wx.StaticText( self.alertPanel, wx.ID_ANY, u"Low level", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lowAlertText.Wrap( -1 )
		self.lowAlertText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		alertSizer.Add( self.lowAlertText, 0, wx.ALL, 5 )
		
		self.lowAlertTextCtrl = wx.TextCtrl( self.alertPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		alertSizer.Add( self.lowAlertTextCtrl, 0, wx.ALL, 5 )
		
		self.lowLevelSetButton = wx.Button( self.alertPanel, wx.ID_ANY, u"Last price as low", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		alertSizer.Add( self.lowLevelSetButton, 0, wx.ALL, 5 )
		
		self.remindAlertText = wx.StaticText( self.alertPanel, wx.ID_ANY, u"Remind me every [minutes]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.remindAlertText.Wrap( -1 )
		self.remindAlertText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		alertSizer.Add( self.remindAlertText, 0, wx.ALL, 5 )
		
		self.remindAlertTextCtrl = wx.TextCtrl( self.alertPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		alertSizer.Add( self.remindAlertTextCtrl, 0, wx.ALL, 5 )
		
		self.emptyPanel = wx.Panel( self.alertPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		alertSizer.Add( self.emptyPanel, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.highSoundAlertText = wx.StaticText( self.alertPanel, wx.ID_ANY, u"High level sound", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.highSoundAlertText.Wrap( -1 )
		self.highSoundAlertText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		alertSizer.Add( self.highSoundAlertText, 0, wx.ALL, 5 )
		
		highSoundAlertChoiceChoices = [ u"ComputerMagic.wav", u"Movie.wav" ]
		self.highSoundAlertChoice = wx.Choice( self.alertPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,-1 ), highSoundAlertChoiceChoices, 0 )
		self.highSoundAlertChoice.SetSelection( 0 )
		self.highSoundAlertChoice.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		alertSizer.Add( self.highSoundAlertChoice, 0, wx.ALL, 5 )
		
		self.emptyPanel2 = wx.Panel( self.alertPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		alertSizer.Add( self.emptyPanel2, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.lowSoundAlertText = wx.StaticText( self.alertPanel, wx.ID_ANY, u"Low level sound", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lowSoundAlertText.Wrap( -1 )
		self.lowSoundAlertText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		alertSizer.Add( self.lowSoundAlertText, 0, wx.ALL, 5 )
		
		lowSoundAlertChoiceChoices = [ u"Buzzer.wav", u"Siren.wav" ]
		self.lowSoundAlertChoice = wx.Choice( self.alertPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,-1 ), lowSoundAlertChoiceChoices, 0 )
		self.lowSoundAlertChoice.SetSelection( 0 )
		self.lowSoundAlertChoice.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		alertSizer.Add( self.lowSoundAlertChoice, 0, wx.ALL, 5 )
		
		self.emptyPanel3 = wx.Panel( self.alertPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		alertSizer.Add( self.emptyPanel3, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.alertPanel.SetSizer( alertSizer )
		self.alertPanel.Layout()
		alertSizer.Fit( self.alertPanel )
		self.stockNotebook.AddPage( self.alertPanel, u"Alert", True )
		
		stockInternalPanelSizer.Add( self.stockNotebook, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.stockInternalPanel.SetSizer( stockInternalPanelSizer )
		self.stockInternalPanel.Layout()
		stockInternalPanelSizer.Fit( self.stockInternalPanel )
		stockSizer.Add( self.stockInternalPanel, 1, wx.EXPAND |wx.ALL, 5 )
		
		internalSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.closeButton = wx.Button( self.stockPanel, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		internalSizer.Add( self.closeButton, 0, wx.ALL, 5 )
		
		self.stockInternalPanelEmpty = wx.Panel( self.stockPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		internalSizer.Add( self.stockInternalPanelEmpty, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.alarmToggleButton = wx.ToggleButton( self.stockPanel, wx.ID_ANY, u"Alarm", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		internalSizer.Add( self.alarmToggleButton, 0, wx.ALL, 5 )
		
		
		stockSizer.Add( internalSizer, 1, wx.EXPAND, 5 )
		
		
		self.stockPanel.SetSizer( stockSizer )
		self.stockPanel.Layout()
		stockSizer.Fit( self.stockPanel )
		self.myNotebook.AddPage( self.stockPanel, u"StockPanel", True )
		
		myPanelSizer.Add( self.myNotebook, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.myPanel.SetSizer( myPanelSizer )
		self.myPanel.Layout()
		myPanelSizer.Fit( self.myPanel )
		mySizer.Add( self.myPanel, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.infoPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		infoSizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		infoSizer.SetFlexibleDirection( wx.BOTH )
		infoSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.infoText = wx.richtext.RichTextCtrl( self.infoPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 800,70 ), wx.TE_READONLY|wx.NO_BORDER|wx.VSCROLL|wx.WANTS_CHARS )
		self.infoText.SetFont( wx.Font( 10, 70, 90, 90, False, "Arial" ) )
		self.infoText.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		
		infoSizer.Add( self.infoText, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.infoPanel.SetSizer( infoSizer )
		self.infoPanel.Layout()
		infoSizer.Fit( self.infoPanel )
		mySizer.Add( self.infoPanel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( mySizer )
		self.Layout()
		mySizer.Fit( self )
		self.timer = wx.Timer()
		self.timer.SetOwner( self, wx.ID_ANY )
		self.timer.Start( 1000 )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.choiceButton.Bind( wx.EVT_BUTTON, self.generate_stock_panel )
		self.highLevelSetButton.Bind( wx.EVT_BUTTON, self.high_level_set )
		self.lowLevelSetButton.Bind( wx.EVT_BUTTON, self.low_level_set )
		self.closeButton.Bind( wx.EVT_BUTTON, self.close_panel )
		self.alarmToggleButton.Bind( wx.EVT_TOGGLEBUTTON, self.toggle_alarm )
		self.infoText.Bind( wx.EVT_TEXT, self.autoscroll_info )
		self.Bind( wx.EVT_TIMER, self.update, id=wx.ID_ANY )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def generate_stock_panel( self, event ):
		event.Skip()
	
	def high_level_set( self, event ):
		event.Skip()
	
	def low_level_set( self, event ):
		event.Skip()
	
	def close_panel( self, event ):
		event.Skip()
	
	def toggle_alarm( self, event ):
		event.Skip()
	
	def autoscroll_info( self, event ):
		event.Skip()
	
	def update( self, event ):
		event.Skip()
	

