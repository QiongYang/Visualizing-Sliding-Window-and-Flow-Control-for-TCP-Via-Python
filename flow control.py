#!/usr/local/bin/python

import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title = title, size = (800, 400))
        self.initFrame()

    def initFrame(self):
        self.buffer_size = 2048
        self.file_size = 4096
        self.file_block = 2048
        self.count1 =0
        self.count2 =0
        self.count3 =2048
        self.count4 = 0
        self.count5 =0
        self.count6 = 2048
        self.count7 = 2048
        self.count8 =2048
        self.count9 = 2048
        self.count10 = 0
        #self.flag = 0
        self.Mylayout()
        self.Centre(True)
        self.Bind(wx.EVT_IDLE, self.OnIdle)
        self.Show(True)

    def Mylayout(self):
        
        self.my_static_text1 = wx.StaticText(self, label = "sender buffer", pos = (10, 10))
        self.my_static_text3 = wx.StaticText(self, label = "sender application", pos = (10, 120))
        self.my_static_text2 = wx.StaticText(self, label = "receiver buffer", pos = (500, 10))
        self.my_static_text4 = wx.StaticText(self, label = "receiver application", pos = (500, 120))

        self.my_static_text5 = wx.StaticText(self, label = "sender buffer", pos = (10, 10))
        self.my_static_text6 = wx.StaticText(self, label = "sender application", pos = (10, 120))
        self.my_static_text7 = wx.StaticText(self, label = "receiver buffer", pos = (500, 10))
        self.my_static_text8 = wx.StaticText(self, label = "receiver application", pos = (500, 120))

        self.my_static_text9 = wx.StaticText(self, label = "sender buffer", pos = (10, 10))
        self.my_static_text10 = wx.StaticText(self, label = "sender application", pos = (10, 120))
        self.my_static_text11 = wx.StaticText(self, label = "receiver buffer", pos = (500, 10))
        self.my_static_text12 = wx.StaticText(self, label = "receiver application", pos = (500, 120))

        
        self.my_gauge1 = wx.Gauge(self, range=self.buffer_size, size=(200, 20), pos = (50, 10))
        self.my_gauge1.SetValue(0)

        self.my_gauge2 = wx.Gauge(self, range=self.file_size, size=(200, 20), pos = (50, 60))
        self.my_gauge2.SetValue(0)

        self.my_gauge3 = wx.Gauge(self, range=self.buffer_size, size=(200, 20), pos = (580, 10))
        self.my_gauge3.SetValue(0)

        self.my_gauge4 = wx.Gauge(self, range=self.file_size, size=(200, 20), pos = (580, 60))
        self.my_gauge4.SetValue(0)
           
        self.my_gauge5 = wx.Gauge(self, range=self.buffer_size, size=(200, 20), pos = (50, 10))
        self.my_gauge5.SetValue(0)

        self.my_gauge6 = wx.Gauge(self, range=self.buffer_size, size=(200, 20), pos = (50, 10))
        self.my_gauge6.SetValue(0)

        self.my_gauge7 = wx.Gauge(self, range=self.buffer_size, size=(200, 20), pos = (50, 10))
        self.my_gauge7.SetValue(0)

        self.my_gauge8 = wx.Gauge(self, range=self.buffer_size, size=(200, 20), pos = (50, 10))
        self.my_gauge8.SetValue(0)

        self.my_gauge9 = wx.Gauge(self, range=self.buffer_size, size=(200, 20), pos = (50, 10))
        self.my_gauge9.SetValue(0)

        self.my_gauge10 = wx.Gauge(self, range=self.file_size, size=(200, 20), pos = (50, 10))
        self.my_gauge10.SetValue(0)

        self.my_gauge11 = wx.Gauge(self, range=self.buffer_size, size=(200, 20), pos = (50, 10))
        self.my_gauge11.SetValue(0)

        self.my_gauge12 = wx.Gauge(self, range=self.file_size, size=(200, 20), pos = (50, 10))
        self.my_gauge12.SetValue(0)

        self.hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.vbox1 = wx.BoxSizer(wx.VERTICAL)
        self.vbox2 = wx.BoxSizer(wx.VERTICAL)
        self.vbox3 = wx.BoxSizer(wx.VERTICAL)
        self.vbox4 = wx.BoxSizer(wx.VERTICAL)

        self.vbox1.Add(self.my_static_text1, flag = wx.ALL, border = 4)
        self.vbox1.Add(self.my_static_text5, flag = wx.ALL, border = 4)
        self.vbox1.Add(self.my_static_text9, flag = wx.ALL, border = 4)
        self.vbox1.Add(self.my_static_text3, flag = wx.ALL, border = 4)
        self.vbox1.Add(self.my_static_text6, flag = wx.ALL, border = 4)
        self.vbox1.Add(self.my_static_text10, flag = wx.ALL, border = 4)
        #self.vbox1.Add(self.my_button, flag = wx.ALL, border = 4)

        self.vbox2.Add(self.my_gauge1, flag = wx.ALL, border = 4)
        self.vbox2.Add(self.my_gauge5, flag = wx.ALL, border = 4)
        self.vbox2.Add(self.my_gauge7, flag = wx.ALL, border = 4)
        self.vbox2.Add(self.my_gauge2, flag = wx.ALL, border = 4)
        self.vbox2.Add(self.my_gauge6, flag = wx.ALL, border = 4)
        self.vbox2.Add(self.my_gauge8, flag = wx.ALL, border = 4)

        
        self.vbox3.Add(self.my_static_text2, flag = wx.ALL, border = 4)
        self.vbox3.Add(self.my_static_text7, flag = wx.ALL, border = 4)
        self.vbox3.Add(self.my_static_text11, flag = wx.ALL, border = 4)

        self.vbox3.Add(self.my_static_text4, flag = wx.ALL, border = 4)
        self.vbox3.Add(self.my_static_text8, flag = wx.ALL, border = 4)
        self.vbox3.Add(self.my_static_text12, flag = wx.ALL, border = 4)
        
        self.vbox4.Add(self.my_gauge3, flag = wx.ALL, border = 4)
        self.vbox4.Add(self.my_gauge9, flag = wx.ALL, border = 4)
        self.vbox4.Add(self.my_gauge11, flag = wx.ALL, border = 4)
        self.vbox4.Add(self.my_gauge4, flag = wx.ALL, border = 4)
        self.vbox4.Add(self.my_gauge10, flag = wx.ALL, border = 4)
        
        self.vbox4.Add(self.my_gauge12, flag = wx.ALL, border = 4)


        self.hbox.Add(self.vbox1, flag = wx.ALL, border = 4)
        self.hbox.Add(self.vbox2, flag = wx.ALL, border = 4)
        self.hbox.Add(self.vbox3, flag = wx.ALL, border = 4)
        self.hbox.Add(self.vbox4, flag = wx.ALL, border = 4)

        self.SetSizer(self.hbox)
    def OnIdle(self, event):
        self.count1 = self.count1 +20
        if self.count1 >= self.buffer_size:
            self.count1 = self.buffer_size    
        self.my_gauge1.SetValue(self.count1)
        self.my_gauge2.SetValue(self.count1)
        if self.my_gauge2.GetValue() == self.buffer_size:
            self.count2 = self.count2 + 20
            if self.count2 >= self.buffer_size:
                self.count2 = self.buffer_size
            self.my_gauge3.SetValue(self.count2)
            self.count3 = self.count3 - 20 
            if self.count3 <= 8:
                self.count3 = 0
            self.my_gauge1.SetValue(self.count3)
            self.my_gauge2.SetValue(self.count3)
            
        if self.my_gauge1.GetValue() == 0 and self.my_gauge3.GetValue() == self.buffer_size:
            self.count4 = self.count4 + 20
            if self.count4 >= self.buffer_size:
                self.count4 = self.buffer_size
            self.my_gauge5.SetValue(self.count4)
            self.my_gauge3.SetValue(0)
            #self.my_gauge9.SetValue(2048)
        if self.my_gauge5.GetValue() == 2048:
            self.count5 = self.count5 + 20
            if self.count5 >= self.buffer_size:
                self.count5 = 0
            #self.my_gauge9.SetValue(0)
            self.my_gauge10.SetValue(self.file_block)
        if self.my_gauge10.GetValue() == 2048:
            self.my_gauge7.SetValue(2048)
            self.my_gauge5.SetValue(0)
            self.count6 = self.count6 - 20
            if self.count6 <= 8:
                self.count6 =0
            self.my_gauge7.SetValue(self.count6)
            self.my_gauge9.SetValue(self.buffer_size)
            self.count7 = self.count7 - 20
            if self.count7 <= 8:
                self.count7 = 0
                self.my_gauge9.SetValue(self.count7)
            self.my_gauge7.SetValue(2048)
            self.count9 = self.count9 - 20
            if self.count9 <= 8:
                self.count9 = 0
            self.my_gauge7.SetValue(self.count9)
            self.count10 = self.count10 + 20 
            if self.count10 >= 2048:
                self.count10 = 2048
            self.my_gauge11.SetValue(self.count10)
        if self.my_gauge10.GetValue() == 2048 and self.my_gauge11.GetValue() == 2048:
            self.my_gauge10.SetValue(0)
            self.my_gauge11.SetValue(0)
            self.my_gauge12.SetValue(self.file_size)

app = wx.App()
MyFrame(None, title = "flow control")
app.MainLoop()