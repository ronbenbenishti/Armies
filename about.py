import sys

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

import about_support

def vp_start_gui():
    global val, w, root
    root = Tk()
    top = About (root)
    about_support.init(root, top)
    root.mainloop()

w = None
def create_About(root, *args, **kwargs):
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = About (w)
    about_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_About():
    global w
    w.destroy()
    w = None


class About:
    def __init__(self, top=None):
        _bgcolor = '#d9d9d9'
        _fgcolor = '#000000'
        _compcolor = '#d9d9d9'
        _ana1color = '#d9d9d9'
        _ana2color = '#d9d9d9'

        top.geometry("432x434+500+100")
        top.title("About")
        top.configure(background="#d9d9d9")



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.02, rely=0.02, relheight=0.96, relwidth=0.96)
        self.Frame1.configure(relief=GROOVE, borderwidth="2", background="#d9d9d9", width=415)

        self.Message = Message(self.Frame1)
        self.Message.place(relx=0.02, rely=0.02, relheight=0.94, relwidth=0.95)
        self.Message.configure(anchor=NW, background="#d9d9d9", foreground="#000000")
        self.Message.configure(highlightbackground="#d9d9d9", highlightcolor="black")
        self.Message.configure(text='''Armies

About, About, About, About, About, About, About. 
About, About, About, About. 
About, About, About, About, About, About. 
About, About, 
About, About, About, About, About, About. 

About, About
About, About, About.''',
                               width=396)


if __name__ == '__main__':
    vp_start_gui()



