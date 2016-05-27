#!/usr/local/bin/python

import wx


class MyFrame(wx.Frame):
    global_count = 0
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title = title, size = (800, 500))
        self.initFrame()


    def initFrame(self):
        self.Mylayout()
        self.Mycreatepacket()
        
        self.Centre()
        self.Show(True)

        # bind events
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.TimerHandler)

        #self.timer.Start(10)
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.my_button)
        self.Bind(wx.EVT_PAINT, self.Mydraw)
        self.timer1=1
        self.tmp=0

    def Mylayout(self):
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.my_button = wx.Button(self, label = 'start')
        self.vbox.Add(self.my_button, flag = wx.ALL, border = 4)
        self.SetSizer(self.vbox)
        self.my_static_text = wx.StaticText(self, label = "input time", pos = (135, 10))
        self.my_static_text = wx.StaticText(self, label = "count down", pos = (470, 10))
        self.my_spinctrl = wx.SpinCtrl(self, value = '0', pos = (550, 10))
        self.my_spinctrl.SetRange(0, 20)
        self.my_spinctrl2 = wx.SpinCtrl(self, value = '0', pos = (200, 10))
        self.my_spinctrl2.SetRange(0, 20)
        #self.rtt=self.my_spinctrl2.GetValue()


    def OnClick(self, event):
        self.timer.Start(40)
        self.rtt = self.my_spinctrl2.GetValue()
        self.timer1=int(self.rtt)
        # pass

    def TimerHandler(self, event):
        MyFrame.global_count = MyFrame.global_count + 1
        self.tmp=self.tmp+1
        if self.tmp>5:
            self.tmp=0
        if self.timer1>0:
            self.timer1=self.timer1-self.tmp/5
        else:
            self.timer1=self.rtt
        self.my_spinctrl.SetValue(self.timer1)
        self.send()
        for i in range(len(self.flying_packet1)):
            if self.flying_packet1[i].direction == "down" and self.flying_packet1[i].y == 50:
                self.flying_packet1[i].start_time =MyFrame.global_count

            if MyFrame.global_count - self.flying_packet1[i].start_time > self.rtt:
                self.send()
        self.Refresh()

    def Mycreatepacket(self):
        self.packet_num = 15
        self.winsize=5
        self.top_packet = [MyPacket("top","blue","null",i*50+20, 50) for i in range(self.packet_num)]
        self.bottom_packet = [MyPacket("bottom", "white","null", i*50+20, 350) for i in range(self.packet_num)]
        self.flying_packet1 = [MyPacket("middle", "blue","down", i*50+20, 50-i*30) for i in range(self.winsize)]
        self.top1_packet = [MyPacket("top","yellow","null",k*50+20,50) for k in range(5)]
        self.bottom1_packet = [MyPacket("bottom", "dark blue", "null", k*50+20, 350) for k in range(5)]
        self.slider_window = SliderWindow(15,45)
    
    def Mydraw(self, event):
        dc = wx.PaintDC(self)

        dc.SetPen(wx.Pen('#4c4c4c', 1, wx.SOLID))
        dc.DrawRectangle(self.slider_window.x, self.slider_window.y, 250, 50)
        
        dc.SetBrush(wx.Brush("#F9F900", wx.SOLID))
        for i in range(5):
            dc.SetPen(wx.Pen('#4c4c4c', 1, wx.SOLID))
            dc.DrawRectangle(self.top1_packet[i].x, self.top1_packet[i].y, 20, 40)

        dc.SetBrush(wx.Brush("#000080", wx.SOLID))
        for i in range(5):
            dc.SetPen(wx.Pen('#4c4c4c', 1, wx.SOLID))
            dc.DrawRectangle(self.bottom1_packet[i].x, self.bottom1_packet[i].y, 20, 40)


        for i in range(self.packet_num):
            if self.top_packet[i].color == "blue":
                dc.SetBrush(wx.Brush("#46A3FF", wx.SOLID))
                dc.SetPen(wx.Pen('#4c4c4c', 1, wx.SOLID))
                dc.DrawRectangle(self.top_packet[i].x, self.top_packet[i].y, 20, 40)

            if self.top_packet[i].color == "yellow":
                dc.SetBrush(wx.Brush("#F9F900", wx.SOLID))
                dc.SetPen(wx.Pen('#4c4c4c', 1, wx.SOLID))
                dc.DrawRectangle(self.top_packet[i].x, self.top_packet[i].y, 20, 40)
        
        for i in range(self.packet_num):
            if self.bottom_packet[i].color == "white":
                dc.SetBrush(wx.Brush("#FCFCFC", wx.SOLID)) 
                dc.SetPen(wx.Pen('#4c4c4c', 1, wx.SOLID))
                dc.DrawRectangle(self.bottom_packet[i].x, self.bottom_packet[i].y, 20, 40)
            if self.bottom_packet[i].color ==  "dark blue":
                dc.SetBrush(wx.Brush("#000080", wx.SOLID))
                dc.SetPen(wx.Pen('#4c4c4c', 1, wx.SOLID))
                dc.DrawRectangle(self.bottom_packet[i].x, self.bottom_packet[i].y, 20, 40)
        

        for i in range(self.winsize):
            if self.flying_packet1[i].y>=50:
                if self.flying_packet1[i].color == "blue":
                    dc.SetBrush(wx.Brush("#46A3FF", wx.SOLID))
                    dc.SetPen(wx.Pen('#4c4c4c', 1, wx.SOLID))
                    dc.DrawRectangle(self.flying_packet1[i].x, self.flying_packet1[i].y, 20, 40)
                if self.flying_packet1[i].color == "green":
                    dc.SetBrush(wx.Brush("#8cEA00", wx.SOLID))
                    dc.SetPen(wx.Pen('#4c4c4c', 1, wx.SOLID))
                    dc.DrawRectangle(self.flying_packet1[i].x, self.flying_packet1[i].y, 20, 40)
 
    def send(self):
         
        for i in range(len(self.flying_packet1)):
            
            if self.flying_packet1[i].direction == "down":
                self.flying_packet1[i].y = self.flying_packet1[i].y +1
                
                if self.flying_packet1[i].y == 350:
                    #print k 
                    self.flying_packet1[i].color = "green"
                    self.bottom_packet[i].color = "dark blue"
                    
                    self.flying_packet1[i].direction = "up"
            if self.flying_packet1[i].direction == "up":
                
                self.flying_packet1[i].y  = self.flying_packet1[i].y - 1
                if self.flying_packet1[i].y == 50:
                                self.timer1=self.rtt
                                self.tmp=0
                                self.my_spinctrl.SetValue(self.rtt)
                                self.top_packet[i].color = "yellow"                                
                                self.slider_window.x = self.slider_window.x + 50
                                self.flying_packet1[i].x = self.flying_packet1[i].x + 250
                                self.flying_packet1[i].y = 50
                                self.flying_packet1[i].direction = "down"
                                self.flying_packet1[i].color = "blue"

                                self.top_packet[i] = self.top_packet[i+5] 
                                self.bottom_packet[i] = self.bottom_packet[i+5]
                                if self.flying_packet1[i].x >= 520:
                                    self.top_packet[i] = self.top_packet[i+10]
                                    self.bottom_packet[i] = self.bottom_packet[i+10]
                                
                                if self.slider_window.x >= 765 and self.flying_packet1[i].x >= 770:
                                    self.flying_packet1 = [MyPacket("middle", "blue","down", i*50+20, 50-i*30) for i in range(self.winsize)]
                                    self.slider_window.x = 15
                                    self.slider_window.y = 45
                                    self.top_packet = [MyPacket("top","blue","null",i*50+20, 50) for i in range(self.packet_num)]
                                    self.bottom_packet = [MyPacket("bottom", "white","null", i*50+20, 350) for i in range(self.packet_num)]
    
class MyPacket(object):
    def __init__(self, state, color, direction,x,y ):
        self.state = state
        self.color = color
        self.direction = direction
        self.x = x
        self.y = y
        self.timer =20
        self.start_time = 0

class SliderWindow(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

app = wx.App()
MyFrame(None, title = "GO Back N")
app.MainLoop()
