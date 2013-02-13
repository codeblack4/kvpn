
#!/usr/bin/python


#: This is a gui attempt for vpnc client under Linux :#

import wx

class MyFrame(wx.Frame):
    
    def __init__(self,parent,title):
        super(MyFrame,self).__init__(parent,title=title,size=(300,100))
        self.control = wx.TextCtrl(self,style=wx.TE_MULTILINE)
        self.CreateStatusBar()


        #: set up the menu :#
        filemenu = wx.Menu()
   

        openItem = filemenu.Append(wx.ID_OPEN,"&Open","Open a file")
        filemenu.AppendSeparator()
        aboutItem = filemenu.Append(wx.ID_ABOUT,"&About","Information about kvpn")
        filemenu.AppendSeparator()
        exitItem  = filemenu.Append(wx.ID_EXIT,"&Exit","Terminate kvpn")


        #: set up edit :#
        editmenu = wx.Menu()
        prefItem = editmenu.Append(wx.ID_ABOUT,"&Preferences","Pref")

        #: Create the menubar :#
        menubar = wx.MenuBar()
        menubar.Append(filemenu,"&File") #: add the filemenu to MenuBar :# 
        menubar.Append(editmenu,"&Edit") #: add the editmenu to MenuBar :#
        self.SetMenuBar(menubar)
        self.Show(True)

        #: set the events :#
        self.Bind(wx.EVT_MENU,self.onOpen,openItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)
        self.Bind(wx.EVT_MENU,self.OnExit,exitItem)

    def onOpen(self,event):

        f = open(



    def OnAbout(self,event):
        # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.   
        msg = wx.MessageDialog(self,"A small vpnc GUI","About Kvpn",wx.OK)
        msg.ShowModal()
        msg.Destroy()

    def OnExit(self,event):
        self.Close(True)

gui = wx.App(False)
frame =MyFrame(None,'Kvpn')
gui.MainLoop()
