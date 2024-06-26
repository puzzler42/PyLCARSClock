from tkinter import *
from tkinter import ttk
from tkinter import font
import time
import calendar
from datetime import datetime
import os, sys
#import PIL
from PIL import Image

def quit(*args):
	root.destroy()

def show_time():
	txt.set(time.strftime("%I:%M"))
	txt2.set(time.strftime("%S"))
	txt3.set(time.strftime("%I:%M %p")[-2:])
	root.after(1000, show_time)
	root.after(1000, upd_cal)
		
def upd_cal():
	dt_cur = datetime.now()
	txtC.set(calendar.TextCalendar(firstweekday = 6).formatmonth(dt_cur.year, dt_cur.month).split('\n', 2)[2])
	txtMY.set(dt_cur.strftime("%B")+" "+dt_cur.strftime("%Y"))
	txtWD.set(dt_cur.strftime("%A"))
	txtD.set(dt_cur.strftime("%m/%d"))

def img_mult(sw, sh):
    h = sh/1080
    ofs = 0
    if sh*16/9 > sw:
        ofs = sh*16/9-sw
    r = (h, ofs)
    return r

    

root = Tk()
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.attributes("-fullscreen", True)
root.configure(background='black')
root.bind("<Escape>", quit)
root.bind("x", quit)
root.after(1000, show_time)
root.after(1000, upd_cal)
root.config(cursor="none")
mlt, ofs = img_mult(screen_width, screen_height)
app_mlt = False
if mlt == 1 and ofs <= 480:
    bg = PhotoImage(file = "LCARS_UI.png") 
else:
    app_mlt = True
if ofs > 480:
    mlt = max(mlt, screen_width/1440)
    app_mlt = True
if app_mlt:
    if os.path.isfile("LCARS_UI-"+str(mlt)[0:16]+".png"):
        bg = PhotoImage(file = "LCARS_UI-"+str(mlt)[0:16]+".png")
    else:
        im = Image.open("LCARS_UI.png")
        im = im.resize(((1440*mlt), (1080*mlt)), Image.Resampling.LANCZOS)
        im.save("LCARS_UI-"+str(mlt)[0:16]+".png","PNG")
        bg = PhotoImage(file = "LCARS_UI-"+str(mlt)[0:16]+".png")
    
lcars_tan = '#F8CC99'
lcars_orange = '#FF9A00'
lcars_blue = '#9C9AFF'
lcars_pink = "#CE9ACE"

fnt = font.Font(family='LCARS', size=int(320*mlt), weight='normal')
fnt2 = font.Font(family='LCARS', size=int(128*mlt), weight='normal')
fnt3 = font.Font(family='LCARS_Mono', size=int(18*mlt), weight='normal')
fnt4 = font.Font(family='LCARS', size=int(32*mlt), weight='normal')
fnt5 = font.Font(family='LCARS', size=int(90*mlt), weight='normal')
txt = StringVar()
txt.set(time.strftime("%I:%M"))
txt2 = StringVar()
txt2.set(time.strftime("%S"))
txt3 = StringVar()
txt3.set(time.strftime("%I:%M %p")[-2:])
txtC = StringVar()
txtMY = StringVar()
txtWD = StringVar()
txtD = StringVar()
upd_cal()

ui_lbl = ttk.Label(root, image=bg, background="black")
ui_lbl.place(relx=0.5, rely=0.5, anchor=CENTER)
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground=lcars_tan, background="black")
lbl.place(relx=0.41, rely=0.55, anchor=CENTER)
s_lbl = ttk.Label(root, textvariable=txt2, font=fnt2, foreground=lcars_orange, background="black")
s_lbl.place(relx=0.65, rely=0.48, anchor=CENTER)
p_lbl = ttk.Label(root, textvariable=txt3, font=fnt2, foreground=lcars_tan, background="black")
p_lbl.place(relx=0.65, rely=0.63, anchor=CENTER)
c_lbl = ttk.Label(root, textvariable=txtC, font=fnt3, foreground=lcars_blue, background="black")
c_lbl.place(relx=0.28, rely=0.16, anchor=CENTER)
my_lbl = ttk.Label(root, textvariable=txtMY, font=fnt4, foreground=lcars_pink, background="black")
my_lbl.place(relx=0.32, rely=0.035, anchor=E)
wd_lbl = ttk.Label(root, textvariable=txtWD, font=fnt5, foreground=lcars_orange, background="black")
wd_lbl.place(relx=0.6, rely=0.055, anchor=E)
d_lbl = ttk.Label(root, textvariable=txtD, font=fnt5, foreground=lcars_tan, background="black")
d_lbl.place(relx=0.6, rely=0.18, anchor=E)


root.mainloop()
