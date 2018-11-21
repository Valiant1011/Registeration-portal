from Tkinter import *
from os import startfile
splash=Tk()
img=PhotoImage(file='C://Users//171b080//Desktop//splash.gif')
def splash_end(event_mouse_moved):
    splash.destroy()
    os.startfile(r'Server.py')
event=Label(splash,image=img)
event.bind('<Motion>',splash_end)
event.pack()
splash.mainloop()
