from Tkinter import *
splash=Tk()
img=PhotoImage(file='C://Users//171b080//Desktop//splash.gif')
def splash_end(event_mouse_moved):
    splash.destroy()

    #call function
event=Label(splash,image=img)
event.bind('<Motion>',splash_end)
event.pack()
splash.mainloop()

    
    
