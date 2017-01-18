#!/usr/bin/env pythonw
import numpy as np
import matplotlib.pylpot as plt
#from numpy import arange, sin, pi
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure

import wx
import os
class MyFrame(wx.Frame):
        """We simply derive a new class of frame"""
        def __init__(self, parent, title):
            wx.Frame.__init__(self, parent, title=title, size=(1000,700))
            self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
            self.CreateStatusBar() #A statusbar at the bottom of the window
            
            # setting up the menu.
            filemenu= wx.Menu()
            
            # wx.ID_ABOUT and wx.ID_EXIT are standard IDs provided by wxWidgets
            menuAbout = filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
            filemenu.AppendSeparator()
            menuOpen = filemenu.Append(wx.ID_OPEN, "&Open"," Opens a selected file from memory")
            filemenu.Append(wx.ID_CLOSE, "&Close"," Closes an already opened file")
            filemenu.Append(wx.ID_SAVEAS, "&Save as"," Save your current file as")
            menuExit = filemenu.Append(wx.ID_EXIT, "&Exit"," Terminate the program")
            
            #adding a plot window
            self.figure = Figure()
            self.axes = self.figure.add_subplot(111)
           
            self.canvas = FigureCanvas(self, -1, self.figure)

            self.sizer = wx.BoxSizer(wx.HORIZONTAL)
            self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP )
            self.SetSizer(self.sizer)
            
            

            # Creating the menubar
            menuBar = wx.MenuBar()
            menuBar.Append(filemenu, "&File") # adding the "filename" to the...
            self.SetMenuBar(menuBar) # Adding the MenuBar for the Frame contentt
            self.Show(True)
            
            
            #set events:
            self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
            self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
            self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
            self.Show(True)
            
            #buttons to control data
            
            self.sizer2 = wx.BoxSizer(wx.VERTICAL)
            self.buttons = []
            btn_name=["Plot","Mean","Mod","Median","CDF"]
            for i in range(0, 5):
                self.buttons.append(wx.Button(self, -1, btn_name[i]))
                self.sizer2.Add(self.buttons[i], 1, wx.EXPAND)

            # Use some sizers to see layout options
            self.sizer = wx.BoxSizer(wx.HORIZONTAL)
            self.sizer.Add(self.control, 5, wx.EXPAND)
            self.sizer.Add(self.canvas, 1, wx.EXPAND)            
            self.sizer.Add(self.sizer2, 1, wx.EXPAND)

            #Layout sizers
            self.SetSizer(self.sizer)
            self.SetAutoLayout(1)
            #self.sizer.Fit(self)
            self.Show()
            
            
        #definition of functions:
        
        def OnAbout(self,e):
            # A message dialog box with an OK button, wx.OK is a standard ID
            dlg = wx.MessageDialog( self, "Sorry, there is nothing much to do here at this point. But there are some attempts to show how it will look at the end. \nLet's start with small steps",
                                   "About this application", wx.OK)
            dlg.ShowModal() #show it
            dlg.Destroy() # destroy it when finished
        
        def OnExit(self,e):
            self.Close(True) # close the frame
            
        def OnOpen(self,e):  #Open a file
            """Open a file"""
            self.dirname = ''
            dlg = wx.FileDialog(self, "Choose a text file", self.dirname, "", "*.txt", wx.OPEN)
            if dlg.ShowModal() == wx.ID_OK:
                self.filename = dlg.GetFilename()
                self.dirname = dlg.GetDirectory()
                filepath=os.path.join(self.dirname, self.filename)
                f = open(os.path.join(self.dirname, self.filename), 'r')
                self.data = np.loadtxt(filepath)
                print self.data
                self.control.SetValue(f.read())
                f.close()
            dlg.Destroy()

class App(wx.App):
    def OnInit(self):
        'Create the main window and insert the custom frame'
        frame = CanvasFrame()
        frame.Show(True)
        return True

app = wx.App(False)
frame = MyFrame(None, 'Practice App')
app.MainLoop()