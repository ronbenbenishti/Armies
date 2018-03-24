import sys,os
import armies, readme, armies_gui_support
from tkinter import filedialog, messagebox
try:
    from Tkinter import *
except ImportError:
    from tkinter import *
try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

Red = '\033[91m'
Green = '\033[92m'

def vp_start_gui():
    global val, w, root
    root = Tk()
    armies_gui_support.set_Tk_var()
    top = Armies (root)
    armies_gui_support.init(root, top)
    root.mainloop()

w = None
def create_Armies(root, *args, **kwargs):
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    armies_gui_support.set_Tk_var()
    top = Armies (w)
    armies_gui_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Armies():
    global w
    w.destroy()
    w = None


class Armies:
    def ScanFile(self):
        filename=filedialog.askopenfilename()
        armies.SingleScan(filename)

    def ScanPath(self):
        path=self.TEntryPath.get()
        armies.Scanpath(path,"")

    def UpdateLinks(self):
        numoflinks=self.TCombobox1.get()
        splitnumber=numoflinks.split(" ")
        try:
            numoflinks=int(splitnumber[1])
            armies.Linksmaker(numoflinks-1)
        except:
            print(Red+"Error: Please select links quantity")

    def QuitYN(self):
        sure= messagebox.askyesno("Armies","Are you sure do you want to quit?")
        if (sure):  #means if sure == True
            exit()

    def Update(self):
        try:
            armies.Update()
        except:
            print(Red+"Error: Links file is empty")

    def __init__(self, top=None):
        _bgcolor = '#d9d9d9'
        _fgcolor = '#000000'
        _compcolor = '#d9d9d9'
        _ana1color = '#d9d9d9'
        _ana2color = '#d9d9d9'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=[('selected', _compcolor), ('active',_ana2color)])

        top.geometry("365x414+500+100")
        top.title("Armies")
        top.configure(background="#d9d9d9")


        self.TFrameUpdate = ttk.Frame(top)
        self.TFrameUpdate.place(relx=0.05, rely=0.17, relheight=0.33, relwidth=0.89)
        self.TFrameUpdate.configure(relief=GROOVE, borderwidth="2", width=325)

        self.BtnLinksfile = ttk.Button(self.TFrameUpdate)
        self.BtnLinksfile.place(relx=0.06, rely=0.3, height=30, width=120)
        self.BtnLinksfile.configure(text="Update Links file", command=self.UpdateLinks)

        self.LabelUpdate = Label(self.TFrameUpdate)
        self.LabelUpdate.place(relx=0.03, rely=0.07, height=26, width=301)
        self.LabelUpdate.configure(background="#d9d9d9", text='''UPDATE''')

        self.BtnUpdateMD5 = ttk.Button(self.TFrameUpdate)
        self.BtnUpdateMD5.place(relx=0.06, rely=0.59, height=30, width=289)
        self.BtnUpdateMD5.configure(text='''Update MD5 DateBase''', command=self.Update)

        self.TCombobox1 = ttk.Combobox(self.TFrameUpdate)
        self.TCombobox1.place(relx=0.46, rely=0.3, relheight=0.19, relwidth=0.48)
        linkslist=[]
        for i in range(1,306):
            if i == 1:
                i=str(i)
                linkslist.append("Add %s Link" % (i))
            else:
                i=str(i)
                linkslist.append("Add %s Links" % (i))
        self.TCombobox1.configure(value=linkslist, state='readonly')

        self.TFrameScan = ttk.Frame(top)
        self.TFrameScan.place(relx=0.05, rely=0.53, relheight=0.33, relwidth=0.89)
        self.TFrameScan.configure(relief=GROOVE, width=325)

        self.LabelScan = Label(self.TFrameScan)
        self.LabelScan.place(relx=0.03, rely=0.07, height=26, width=304)
        self.LabelScan.configure(background="#d9d9d9", text="SCAN")

        self.BtnScanfile = ttk.Button(self.TFrameScan)
        self.BtnScanfile.place(relx=0.06, rely=0.59, height=30, width=288)
        self.BtnScanfile.configure(text="Scan File", command=self.ScanFile)

        self.BtnScanpath = ttk.Button(self.TFrameScan)
        self.BtnScanpath.place(relx=0.06, rely=0.3, height=30, width=108)
        self.BtnScanpath.configure(text="Scan Path", command=self.ScanPath)

        self.TEntryPath = ttk.Entry(self.TFrameScan)
        self.TEntryPath.place(relx=0.46, rely=0.3, relheight=0.19, relwidth=0.48)

        self.welcomeLabel = Label(top)
        self.welcomeLabel.place(relx=0.05, rely=0.02, height=46, width=317)
        self.welcomeLabel.configure(background="#d9d9d9", text="Welcome to Armies")

        self.menubar = Menu(top)
        top.configure(menu=self.menubar)

        self.file = Menu(top, tearoff=0)
        self.menubar.add_cascade(menu=self.file, label="File", underline=0)
        self.file.add_command(label="Open Links file", underline=5, command=lambda:os.system(("notepad lists.txt")))
        self.file.add_command(label="Open souce WebPage", underline=5, command=lambda:os.system("start https://virusshare.com/hashes.4n6"))
        self.file.add_command(label="Quit", underline=0, command=self.QuitYN)
        self.tools = Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.tools, label="Tools", underline=0)
        self.tools.add_command(label="Update links file", underline=0, command=self.UpdateLinks)
        self.tools.add_command(label="Create MD5 DB", underline=0, command=self.Update)
        self.tools.add_command( label="Scan file", underline=5, command=self.ScanFile)
        self.tools.add_command(label="Scan path", underline=5, command=self.ScanPath)
        self.help = Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.help,label="Help", underline=0)
        self.help.add_command(label="Readme", underline=0, command=lambda:os.system("readme.py"))
        self.help.add_command(label="About", underline=0, command=lambda:os.system("about.py"))


        self.BtnQuit = ttk.Button(top)
        self.BtnQuit.place(relx=0.66, rely=0.89, height=30, width=98)
        self.BtnQuit.configure(text="Quit", command=self.QuitYN)

        self.LabelVersion = Label(top)
        self.LabelVersion.place(relx=0.05, rely=0.92, height=26, width=82)
        self.LabelVersion.configure(background="#d9d9d9", text="Armies v2.0")



if __name__ == '__main__':
    vp_start_gui()



