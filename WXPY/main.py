import wx
import NyobaGan as coba

class Mantab(coba.MyFrame2):
    def __init__(self,parent):
        coba.MyFrame2.__init__(self,parent)

app=wx.App()
frame=Mantab(parent=None)
frame.Show()

app.MainLoop()