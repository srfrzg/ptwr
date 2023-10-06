
import tkinter as tk
from decimal import Decimal
import math
from functools import partial
from tkinter import font
from tkinter import messagebox
fixxacre=43560
fixxkanal=5445
fixxmarla=272.25
fixxkaramsing=5.5
fixxkaramdbl=30.25
window = tk.Tk()
side1ft=0.0
side1krm=0.0
totvirasat=0.0
fnt = font.Font(family="Helvetica", size=8, weight="bold")
efnt = font.Font(family="Helvetica", size=6, weight="bold")
#empty rows

emp1=tk.empty_row = tk.Label(window, padx=0, pady=0)
emp1.grid(row=6,column=1)
emp1=tk.Label(window, padx=0, pady=0)
emp1.grid(row=7,column=1)
emp1=tk.Label(window,padx=0,pady=0)
emp1.grid(row=8,column=1)
emp1=tk.Label(window,padx=0,pady=0)
emp1.grid(row=9,column=1)
emp1=tk.Label(window,padx=0,pady=0)
emp1.grid(row=10,column=1)
emp1=tk.Label(window,padx=0,pady=0)
emp1.grid(row=12,column=1)
emp1=tk.Label(window,padx=0,pady=0)
emp1.grid(row=13,column=1)
emp1=tk.Label(window,padx=0,pady=0)
emp1.grid(row=14,column=1)
emp1=tk.Label(window,padx=0,pady=0)

for i in range(6, 15):
    window.grid_rowconfigure(i, minsize=20)


emp1.grid(row=18,column=1)
emp1=tk.Label(window,padx=0,pady=0)
emp1.grid(row=19,column=1)
emp1=tk.Label(window,padx=0,pady=0)
for i in range(18, 20):
    window.grid_rowconfigure(i, minsize=20)



#empty rows end

def chk(val) :
    if(val==''):
    	return 0
    try :
    	float(val)
    except ValueError :
    	try:
    		int(val)
    	except:
    		return 1
#basic start
def resetb():
	response3 = messagebox.askyesno("Reset All Values", "Reset")
	if response3:
		print("Congratulations!")
	else:
		return
	acreget.delete("0",tk.END)
	kanalget.delete("0",tk.END)
	marlaget.delete("0",tk.END)
	footget.delete("0",tk.END)
	karamget.delete("0",tk.END)
	karamget.delete("0",tk.END)
	bighaget.delete("0",tk.END)
	bchange(1)
def bchange(event):
	global side1ft,side1krm,totvirasat
	btot=0
	err=0
	try:
		acre=float(eval(acreget.get()))*fixxacre
	except:
		acre=0.0
		err=1
	try:
		kanal=float(eval(kanalget.get()))*fixxkanal
	except:
		kanal=0.0
		err=1
	try:
		
		marla=float(eval(marlaget.get()))*fixxmarla
	except:
		marla=0.0
		err=1
		
	try:
		
		ft=float(eval(footget.get()))
	except:
		ft=0.0
		err=1
	try:
		
		karam=float(eval(karamget.get()))*fixxkaramdbl
	except:
		karam=0.0
		err=1
	try:
		
		bigha=float(eval(bighaget.get()))*21780
	except:
		bigha=0.0
		err=1
	
	btot=acre+kanal+marla+ft+karam+bigha
	foot=btot
	side1ft=btot
	side1krm=btot*fixxkaramdbl
	totvirasat=btot
	footforbkmf=btot
	footforbmf=btot
	footforbf=btot
	footforkrm=btot
	footforbigha=btot
	a=0.0
	k=0.0
	m=0.0
	if(foot>=fixxacre):
		a=foot//fixxacre
		foot=foot%fixxacre
	if(foot>=fixxkanal):
		k=foot//fixxkanal
		foot=foot%fixxkanal
	if(foot>=fixxmarla):
		m=foot//fixxmarla
		foot=foot%fixxmarla
	bakmf.config(text=f"ACRE {a}  KANAL {k}  Marla {m}  Foot {round(foot,3)}",font=fnt,width=13,anchor="w")
	a=0.0
	k=0.0
	m=0.0
	foot=footforbkmf
	if(foot>=fixxkanal):
		k=foot//fixxkanal
		foot=foot%fixxkanal
	if(foot>=fixxmarla):
		m=foot//fixxmarla
		foot=foot%fixxmarla
	bkmf.config(text=f"\tKANAL {k}  Marla {m}  Foot {round(foot,3)}",anchor="w",font=fnt,width=13)
	a=0.0
	k=0.0
	m=0.0
	foot=footforbmf
	if(foot>=fixxmarla):
		m=foot//fixxmarla
		foot=foot%fixxmarla
	bmf.config(text=f"\t\tMarla {m}  Foot {round(foot,3)}",anchor="w",font=fnt,width=13)
	a=0.0
	k=0.0
	m=0.0
	foot=footforbf
	bf.config(text=f"\t\t\tFoot {round(foot,3)}",font=efnt,width=13)
	a=0.0
	k=0.0
	m=0.0
	foot=footforkrm
	bkrm.config(text=f"\t\t\tKARAM {round(foot/fixxkaramdbl,3)}",font=efnt,width=13)
	
	a=0.0
	k=0.0
	m=0.0
	foot=footforbigha
	big=0.0
	if(foot>=21780):
		big=foot//21780
		foot=foot%21780
	if(foot>=fixxkanal):
		k=foot//fixxkanal
		foot=foot%fixxkanal
	if(foot>=fixxmarla):
		m=foot//fixxmarla
		foot=foot%fixxmarla
	bbigha.config(text=f"BIGHA {big}  KANAL {k}  Marla {m}  Foot {round(foot,3)}",anchor="w",font=efnt,width=13)
	sidechanged(event)
	virasatcal(event)

lblw=8
acrelbl = tk.Label(window, text="ACRE")
acrelbl.grid(row=0, column=0)
acreget = tk.Entry(window,fg="blue",width=lblw)
acreget.grid(row=0, column=1)
kanallbl = tk.Label(window, text="KNAL")
kanallbl.grid(row=1, column=0)
kanalget = tk.Entry(window,fg="blue",width=lblw)
kanalget.grid(row=1, column=1)
marlalbl = tk.Label(window, text="MRLA")
marlalbl.grid(row=2, column=0)
marlaget = tk.Entry(window,fg="blue",width=lblw)
marlaget.grid(row=2, column=1)
footlbl = tk.Label(window, text="FOOT")
footlbl.grid(row=3, column=0)
footget = tk.Entry(window,fg="blue",width=lblw)
footget.grid(row=3, column=1)
karamlbl = tk.Label(window, text="KRAM")
karamlbl.grid(row=4, column=0)
karamget = tk.Entry(window,fg="blue",width=lblw)
karamget.grid(row=4, column=1)
bighalbl = tk.Label(window, text="BIGHA")
bighalbl.grid(row=5, column=0)
bighaget = tk.Entry(window,fg="blue",width=lblw)
bighaget.grid(row=5, column=1)
acreget.bind('<KeyRelease>',bchange )
kanalget.bind('<KeyRelease>',bchange )
marlaget.bind('<KeyRelease>',bchange )
footget.bind('<KeyRelease>',bchange )
karamget.bind('<KeyRelease>',bchange )
bighaget.bind('<KeyRelease>',bchange )
basicbtn = tk.Button(window, text="RESET",bg="red",fg="white",command=resetb)
basicbtn.grid(row=2, column=3)
window.attributes('-fullscreen', True)  # make the window full screen
bakmf = tk.Label(window, text='', font=fnt,bg="black",fg="white")
bakmf.place(x=0, y=450, relwidth=1, height=50)  # position the label at the top of the window and make it full width
bkmf = tk.Label(window, text='', font=fnt,bg="black",fg="white")
bkmf.place(x=0, y=510, relwidth=1, height=50)  # position the label at the top of the window and make it full width
bmf = tk.Label(window, text='', font=fnt,bg="black",fg="white")
bmf.place(x=0, y=570, relwidth=1, height=50) # position the label at the top of the window and make it full width
bf = tk.Label(window, text='', font=fnt,bg="black",fg="white")
bf.place(x=0, y=630, relwidth=1, height=50)# position the label at the top of the window and make it full width
bkrm= tk.Label(window, text="", font=fnt,bg="black",fg="white")
bkrm.place(x=0, y=690, relwidth=1, height=50) # position the label at the top of the window and make it full width
bbigha= tk.Label(window, text="", font=efnt,bg="black",fg="white")
bbigha.place(x=0, y=750, relwidth=1, height=50) # position the label at the top of the window and make it full width
#basic end


#side1 start


lblw=8
sidefnt = font.Font(family="Helvetica", size=6, weight="bold")
s1footer = tk.Label(window, text='', font=sidefnt,bg="blue",anchor="w",fg="white")
s1footer.place(x=20, y=940, relwidth=1, height=50)  # position the label at the top of the window and make it full width
def sideclick():
	sidechanged(1)
def sidechanged(event):
	global sdie1krm,side1ft
	s1=0.0
	s2=0.0
	s2=side1ft
	err=0
	err=chk(s1sideget.get())
	if err==1:
		s1=0.0
	else:
		try:
			s1=float(s1sideget.get())
		except:
			s1=0.0
	def zero():
		s1footer.config(text=f"{0} ft * {0} ft   ===   {0} krm* {(0)*0} krm")
	if(s1==0.0 or s2==0.0 or s1==0 or s2==0 or s1>s2):
		zero()
		return
	if(radio_var.get()==1):
		try:
			s1footer.config(text=f"{round(s1,2)} ft* {round(s2/s1,2)} ft   ===   {round(s1/fixxkaramsing,2)} krm * {round((s2/s1)/fixxkaramsing,2)} krm")
		except:
			zero()
	if(radio_var.get()==2):
		try:
			s2=s2/fixxkaramdbl
		except:
			zero()
			return
		try:
			s1footer.config(text=f"( {round(s1,2)} krm* {round(s2/s1,2)} krm ) ===( {round(s1*fixxkaramsing,2)} ft * {round((s2/s1)*fixxkaramsing,2)} ft )")
		except:
			zero()
radio_var=tk.IntVar(value=1)
s1sidelbl = tk.Label(window, text="SIDE 1)",bg="blue",fg="white")
s1sidelbl.grid(row=17, column=0)
s1sideget = tk.Entry(window,fg="white",bg="blue",width=lblw)
s1sideget.grid(row=17, column=1)
s1sideget.bind('<KeyRelease>',sidechanged )
rb1 = tk.Radiobutton(window, text="FOT",font=('Arial', 10),variable=radio_var, value=1, command=sideclick)
rb1.grid(row=17, column=2)
rb2 = tk.Radiobutton(window, text="KRM",font=('Arial', 10), variable=radio_var, value=2,command=sideclick)
rb2.grid(row=17, column=3)
window.attributes('-fullscreen', True)  # make the window full screen
#side1 end


#virasat start
virname=tk.Label(window,text="VIRST", padx=0, pady=0)
virname.grid(row=20,column=0)
virp1= tk.Entry(window,fg="blue",width=7)
virp1.grid(row=25, column=0)
virp1lbl= tk.Label(window, text='', font=sidefnt,bg="orange",anchor="w",fg="white")
virp1lbl.place(x=200, y=1090, relwidth=1, height=50)  # position the label at the top of the window and make it full width

virp2= tk.Entry(window,fg="blue",width=7)
virp2.grid(row=26, column=0)
virp2lbl= tk.Label(window, text='', font=sidefnt,bg="orange",anchor="w",fg="white")
virp2lbl.place(x=200, y=1150, relwidth=1, height=50)  # position the label at the top of the window and make it full width

virp3= tk.Entry(window,fg="blue",width=7)
virp3.grid(row=27, column=0)
virp3lbl= tk.Label(window, text='', font=sidefnt,bg="orange",anchor="w",fg="white")
virp3lbl.place(x=200, y=1210, relwidth=1, height=50)  # position the label at the top of the window and make it full width

virp4= tk.Entry(window,fg="blue",width=7)
virp4.grid(row=28, column=0)
virp4lbl= tk.Label(window, text='', font=sidefnt,bg="orange",anchor="w",fg="white")
virp4lbl.place(x=200, y=1270, relwidth=1, height=50)  # position the label at the top of the window and make it full width

virp5= tk.Entry(window,fg="blue",width=7)
virp5.grid(row=29, column=0)
virp5lbl= tk.Label(window, text='', font=sidefnt,bg="orange",anchor="w",fg="white")
virp5lbl.place(x=200, y=1330, relwidth=1, height=50)  # position the label at the top of the window and make it full width
global msg1,msg2,msg3,msg4,msg5,msg6

def virasatcal(event):
	global totvirasat
	totall=0.0
	totall=totvirasat
	virerr=0
	global msg1,msg2,msg3,msg4,msg5,msg6
	msg1=msg2=msg3=msg4=msg5=msg=0
	def virkmf(inp,str):
		
		knlflg=0
		mrlflg=0
		yy=float(inp)
		kn=0
		mr=0
		if(yy>=fixxkanal):
			knlflg=1
			kn=(yy//fixxkanal)
			yy=yy%fixxkanal
		if(yy>=fixxmarla):
			mrlflg=1
			mr=yy//fixxmarla
			yy=yy%fixxmarla
		if(knlflg==0):
			kn=0
		if (mrlflg==0):
			mr=0
		if(yy==0.0):
			yy=0
		if(str=="e1"):
			virp1lbl.config(text=f"\tKANAL {kn}  Marla {mr}  Foot {yy}",anchor="w",font=efnt)
		if(str=="e2"):
			virp2lbl.config(text=f"\tKANAL {kn}  Marla {mr}  Foot {yy}",anchor="w",font=efnt)
		if(str=="e3"):
			virp3lbl.config(text=f"\tKANAL {kn}  Marla {mr}  Foot {yy}",anchor="w",font=efnt)
		if(str=="e4"):
			virp4lbl.config(text=f"\tKANAL {kn}  Marla {mr}  Foot {yy}",anchor="w",font=efnt)
		if(str=="e5"):
			virp5lbl.config(text=f"\tKANAL {kn}  Marla {mr}  Foot {yy}",anchor="w",font=efnt)
		if(inp==0 and str=="e1"):
			virp1lbl.config(text=f"\tKANAL {0}  Marla {0}  Foot {0}",anchor="w",font=efnt)
		if(inp==0 and str=="e2"):
			virp2lbl.config(text=f"\tKANAL {0}  Marla {0}  Foot {0}",anchor="w",font=efnt)
			
		if(inp==0 and str=="e3"):
			virp3lbl.config(text=f"\tKANAL {0}  Marla {0}  Foot {0}",anchor="w",font=efnt)
		
		if(inp==0 and str=="e4"):
			virp4lbl.config(text=f"\tKANAL {0}  Marla {0}  Foot {0}",anchor="w",font=efnt)
			
		if(inp==0 and str=="e5"):
			virp5lbl.config(text=f"\tKANAL {0}  Marla {0}  Foot {0}",anchor="w",font=efnt)
		
	try:
		msg1=totall*float(eval(virp1.get()))
		virkmf(totall*float(eval(virp1.get())),"e1")
	except:
		msg1=0
		virkmf(0,"e1")
	try:
		msg2=totall*float(eval(virp2.get()))
		virkmf(totall*float(eval(virp2.get())),"e2")
	except:
		msg2=0
		virkmf(0,"e2")
	try:
		msg3=totall*float(eval(virp3.get()))
		virkmf(totall*float(eval(virp3.get())),"e3")
	except:
		virkmf(0,"e3")
	try:
		msg4=totall*float(eval(virp4.get()))
		virkmf(totall*float(eval(virp4.get())),"e4")
	except:
		msg4=0
		virkmf(0,"e4")
	try:
		msg5=totall*float(eval(virp5.get()))
		virkmf(totall*float(eval(virp5.get())),"e5")
	except:
		msg5=0
		virkmf(0,"e5")
		


def clk1(event):
    # Create a new window
    newwindow = tk.Toplevel(window)
    newwindow.title("VIRASAT HISSA-1")
    newwindow.geometry("900x500+{}+{}".format(window.winfo_x()+30, window.winfo_screenheight() - 700))
    clkakmf = tk.Label(newwindow, text='', font=fnt,bg="orange",fg="white")
    clkakmf.place(x=20, y=60, relwidth=1, height=50)  # position the label at the top of the window and make it full widt
    clkkmf = tk.Label(newwindow, text='', font=fnt,bg="orange",fg="white")
    clkkmf.place(x=20, y=120, relwidth=1, height=50) 
    clkmf = tk.Label(newwindow, text='', font=fnt,bg="orange",fg="white")
    clkmf.place(x=20, y=180, relwidth=1, height=50)
    clkf = tk.Label(newwindow, text='', font=fnt,bg="orange",fg="white")
    clkf.place(x=20, y=240, relwidth=1, height=50)  
    clkkrm= tk.Label(newwindow, text='', font=fnt,bg="orange",fg="white")
    clkkrm.place(x=20, y=300, relwidth=1, height=50) 
    clkbigha= tk.Label(newwindow, text='', font=fnt,bg="orange",fg="white")
    clkbigha.place(x=20, y=360, relwidth=1, height=50) 
    foot=msg1
    footforbkmf=foot
    footforbmf=foot
    footforbf=foot
    footforkrm=foot
    footforbigha=foot
    a=0.0
    k=0.0
    m=0.0
    if(foot>=fixxacre):
    	a=foot//fixxacre
    	foot=foot%fixxacre
    if(foot>=fixxkanal):
    	k=foot//fixxkanal
    	foot=foot%fixxkanal
    if(foot>=fixxmarla):
    	m=foot//fixxmarla
    	foot=foot%fixxmarla
    clkakmf.config(text=f"ACRE {a}  KANAL {k}  Marla {m}  Foot {round(foot,3)}",font=efnt,width=13,anchor="w")
    a=0.0
    k=0.0
    m=0.0
    foot=footforbkmf
    if(foot>=fixxkanal):
    	k=foot//fixxkanal
    	foot=foot%fixxkanal
    if(foot>=fixxmarla):
    	m=foot//fixxmarla
    	foot=foot%fixxmarla
    clkkmf.config(text=f"\tKANAL {k}  Marla {m}  Foot {round(foot,3)}",anchor="w",font=efnt,width=13)
    a=0.0
    k=0.0
    m=0.0
    foot=footforbmf
    if(foot>=fixxmarla):
    	m=foot//fixxmarla
    	foot=foot%fixxmarla
    clkmf.config(text=f"\t\tMarla {m}  Foot {round(foot,3)}",anchor="w",font=efnt,width=13)
    a=0.0
    k=0.0
    m=0.0
    foot=footforbf
    clkf.config(text=f"\t\t\tFoot {round(foot,3)}",font=efnt,width=13)
    a=0.0
    k=0.0
    m=0.0
    foot=footforkrm
    clkkrm.config(text=f"\t\t\tKARAM {round(foot/fixxkaramdbl)}",font=efnt,width=13)
    a=0.0
    k=0.0
    m=0.0
    foot=footforbigha
    big=0.0
    if(foot>=21780):
    	big=foot//21780
    	foot=foot%21780
    if(foot>=fixxkanal):
    	k=foot//fixxkanal
    	foot=foot%fixxkanal
    if(foot>=fixxmarla):
    	m=foot//fixxmarla
    	foot=foot%fixxmarla
    clkbigha.config(text=f"BIGHA {big}  KANAL {k}  Marla {m}  Foot {round(foot,3)}",anchor="w",font=efnt,width=13)
def clk2(event):
    # Create a new window
    newwindow = tk.Toplevel(window)
    newwindow.title("VIRASAT HISSA-2")
    newwindow.geometry("900x500+{}+{}".format(window.winfo_x()+30, window.winfo_screenheight() - 700))
    clkakmf = tk.Label(newwindow, text='', font=fnt,bg="orange",fg="white")
    clkakmf.place(x=20, y=60, relwidth=1, height=50)  # position the label at the top of the window and make it full widt
    clkkmf = tk.Label(newwindow, text='', font=fnt,bg="orange",fg="white")
    clkkmf.place(x=20, y=120, relwidth=1, height=50) 
    clkmf = tk.Label(newwindow, text='', font=fnt,bg="orange",fg="white")
    clkmf.place(x=20, y=180, relwidth=1, height=50)
    clkf = tk.Label(newwindow, text='', font=fnt,bg="orange",fg="white")
    clkf.place(x=20, y=240, relwidth=1, height=50)  
    clkkrm= tk.Label(newwindow, text='', font=fnt,bg="orange",fg="white")
    clkkrm.place(x=20, y=300, relwidth=1, height=50) 
    clkbigha= tk.Label(newwindow, text='', font=fnt,bg="orange",fg="white")
    clkbigha.place(x=20, y=360, relwidth=1, height=50) 
    foot=msg2
    footforbkmf=foot
    footforbmf=foot
    footforbf=foot
    footforkrm=foot
    footforbigha=foot
    a=0.0
    k=0.0
    m=0.0
    if(foot>=fixxacre):
    	a=foot//fixxacre
    	foot=foot%fixxacre
    if(foot>=fixxkanal):
    	k=foot//fixxkanal
    	foot=foot%fixxkanal
    if(foot>=fixxmarla):
    	m=foot//fixxmarla
    	foot=foot%fixxmarla
    clkakmf.config(text=f"ACRE {a}  KANAL {k}  Marla {m}  Foot {round(foot,3)}",font=efnt,width=13,anchor="w")
    a=0.0
    k=0.0
    m=0.0
    foot=footforbkmf
    if(foot>=fixxkanal):
    	k=foot//fixxkanal
    	foot=foot%fixxkanal
    if(foot>=fixxmarla):
    	m=foot//fixxmarla
    	foot=foot%fixxmarla
    clkkmf.config(text=f"\tKANAL {k}  Marla {m}  Foot {round(foot,3)}",anchor="w",font=efnt,width=13)
    a=0.0
    k=0.0
    m=0.0
    foot=footforbmf
    if(foot>=fixxmarla):
    	m=foot//fixxmarla
    	foot=foot%fixxmarla
    clkmf.config(text=f"\t\tMarla {m}  Foot {round(foot,3)}",anchor="w",font=efnt,width=13)
    a=0.0
    k=0.0
    m=0.0
    foot=footforbf
    clkf.config(text=f"\t\t\tFoot {round(foot,3)}",font=efnt,width=13)
    a=0.0
    k=0.0
    m=0.0
    foot=footforkrm
    clkkrm.config(text=f"\t\t\tKARAM {round(foot/fixxkaramdbl)}",font=efnt,width=13)
    a=0.0
    k=0.0
    m=0.0
    foot=footforbigha
    big=0.0
    if(foot>=21780):
    	big=foot//21780
    	foot=foot%21780
    if(foot>=fixxkanal):
    	k=foot//fixxkanal
    	foot=foot%fixxkanal
    if(foot>=fixxmarla):
    	m=foot//fixxmarla
    	foot=foot%fixxmarla
    clkbigha.config(text=f"BIGHA {big}  KANAL {k}  Marla {m}  Foot {round(foot,3)}",anchor="w",font=efnt,width=13)
def clk3(event):
    # Create a new window
    newwindow = tk.Toplevel(window)
    newwindow.title("VIRASAT HISSA-3")
    newwindow.geometry("900x500+{}+{}".format(window.winfo_x()+30, window.winfo_screenheight() - 700))
    clkakmf = tk.Label(newwindow, text='', font=fnt,bg="orange",fg="white")
    clkakmf.place(x=20, y=60, relwidth=1, height=50)  # position the label at the top of the window and make it full widt
    clkkmf = tk.Label(newwindow, text='', font=fnt,bg="orange",fg="white")
    clkkmf.place(x=20, y=120, relwidth=1, height=50) 
    clkmf = tk.Label(newwindow, text='', font=fnt,bg="orange",fg="white")
    clkmf.place(x=20, y=180, relwidth=1, height=50)
    clkf = tk.Label(newwindow, text='', font=fnt,bg="orange",fg="white")
    clkf.place(x=20, y=240, relwidth=1, height=50)  
    clkkrm= tk.Label(newwindow, text='', font=fnt,bg="orange",fg="white")
    clkkrm.place(x=20, y=300, relwidth=1, height=50) 
    clkbigha= tk.Label(newwindow, text='', font=fnt,bg="orange",fg="white")
    clkbigha.place(x=20, y=360, relwidth=1, height=50) 
    foot=msg3
    footforbkmf=foot
    footforbmf=foot
    footforbf=foot
    footforkrm=foot
    footforbigha=foot
    a=0.0
    k=0.0
    m=0.0
    if(foot>=fixxacre):
    	a=foot//fixxacre
    	foot=foot%fixxacre
    if(foot>=fixxkanal):
    	k=foot//fixxkanal
    	foot=foot%fixxkanal
    if(foot>=fixxmarla):
    	m=foot//fixxmarla
    	foot=foot%fixxmarla
    clkakmf.config(text=f"ACRE {a}  KANAL {k}  Marla {m}  Foot {round(foot,3)}",font=efnt,width=13,anchor="w")
    a=0.0
    k=0.0
    m=0.0
    foot=footforbkmf
    if(foot>=fixxkanal):
    	k=foot//fixxkanal
    	foot=foot%fixxkanal
    if(foot>=fixxmarla):
    	m=foot//fixxmarla
    	foot=foot%fixxmarla
    clkkmf.config(text=f"\tKANAL {k}  Marla {m}  Foot {round(foot,3)}",anchor="w",font=efnt,width=13)
    a=0.0
    k=0.0
    m=0.0
    foot=footforbmf
    if(foot>=fixxmarla):
    	m=foot//fixxmarla
    	foot=foot%fixxmarla
    clkmf.config(text=f"\t\tMarla {m}  Foot {round(foot,3)}",anchor="w",font=efnt,width=13)
    a=0.0
    k=0.0
    m=0.0
    foot=footforbf
    bf.config(text=f"\t\t\tFoot {round(foot,3)}",font=efnt,width=13)
    a=0.0
    k=0.0
    m=0.0
    foot=footforkrm
    clkkrm.config(text=f"\t\t\tKARAM {round(foot/fixxkaramdbl)}",font=efnt,width=13)
    a=0.0
    k=0.0
    m=0.0
    foot=footforbigha
    big=0.0
    if(foot>=21780):
    	big=foot//21780
    	foot=foot%21780
    if(foot>=fixxkanal):
    	k=foot//fixxkanal
    	foot=foot%fixxkanal
    if(foot>=fixxmarla):
    	m=foot//fixxmarla
    	foot=foot%fixxmarla
    clkbigha.config(text=f"BIGHA {big}  KANAL {k}  Marla {m}  Foot {round(foot,3)}",anchor="w",font=efnt,width=13)
def clk4(event):
    # Create a new window
    newwindow = tk.Toplevel(window)
    newwindow.title("VIRASAT HISSA-4")
    newwindow.geometry("900x500+{}+{}".format(window.winfo_x()+30, window.winfo_screenheight() - 700))
    clkakmf = tk.Label(newwindow, text='', font=fnt,bg="orange",fg="white")
    clkakmf.place(x=20, y=60, relwidth=1, height=50)  # position the label at the top of the window and make it full widt
    clkkmf = tk.Label(newwindow, text='', font=fnt,bg="orange",fg="white")
    clkkmf.place(x=20, y=120, relwidth=1, height=50) 
    clkmf = tk.Label(newwindow, text='', font=fnt,bg="orange",fg="white")
    clkmf.place(x=20, y=180, relwidth=1, height=50)
    clkf = tk.Label(newwindow, text='', font=fnt,bg="orange",fg="white")
    clkf.place(x=20, y=240, relwidth=1, height=50)  
    clkkrm= tk.Label(newwindow, text='', font=fnt,bg="orange",fg="white")
    clkkrm.place(x=20, y=300, relwidth=1, height=50) 
    clkbigha= tk.Label(newwindow, text='', font=fnt,bg="orange",fg="white")
    clkbigha.place(x=20, y=360, relwidth=1, height=50) 
    foot=msg4
    footforbkmf=foot
    footforbmf=foot
    footforbf=foot
    footforkrm=foot
    footforbigha=foot
    a=0.0
    k=0.0
    m=0.0
    if(foot>=fixxacre):
    	a=foot//fixxacre
    	foot=foot%fixxacre
    if(foot>=fixxkanal):
    	k=foot//fixxkanal
    	foot=foot%fixxkanal
    if(foot>=fixxmarla):
    	m=foot//fixxmarla
    	foot=foot%fixxmarla
    clkakmf.config(text=f"ACRE {a}  KANAL {k}  Marla {m}  Foot {round(foot,3)}",font=efnt,width=13,anchor="w")
    a=0.0
    k=0.0
    m=0.0
    foot=footforbkmf
    if(foot>=fixxkanal):
    	k=foot//fixxkanal
    	foot=foot%fixxkanal
    if(foot>=fixxmarla):
    	m=foot//fixxmarla
    	foot=foot%fixxmarla
    clkkmf.config(text=f"\tKANAL {k}  Marla {m}  Foot {round(foot,3)}",anchor="w",font=efnt,width=13)
    a=0.0
    k=0.0
    m=0.0
    foot=footforbmf
    if(foot>=fixxmarla):
    	m=foot//fixxmarla
    	foot=foot%fixxmarla
    clkmf.config(text=f"\t\tMarla {m}  Foot {round(foot,3)}",anchor="w",font=efnt,width=13)
    a=0.0
    k=0.0
    m=0.0
    foot=footforbf
    bf.config(text=f"\t\t\tFoot {round(foot,3)}",font=efnt,width=13)
    a=0.0
    k=0.0
    m=0.0
    foot=footforkrm
    clkkrm.config(text=f"\t\t\tKARAM {round(foot/fixxkaramdbl)}",font=efnt,width=13)
    a=0.0
    k=0.0
    m=0.0
    foot=footforbigha
    big=0.0
    if(foot>=21780):
    	big=foot//21780
    	foot=foot%21780
    if(foot>=fixxkanal):
    	k=foot//fixxkanal
    	foot=foot%fixxkanal
    if(foot>=fixxmarla):
    	m=foot//fixxmarla
    	foot=foot%fixxmarla
    clkbigha.config(text=f"BIGHA {big}  KANAL {k}  Marla {m}  Foot {round(foot,3)}",anchor="w",font=efnt,width=13)
def clk5(event):
    # Create a new window
    newwindow = tk.Toplevel(window)
    newwindow.title("VIRASAT HISSA-5")
    newwindow.geometry("900x500+{}+{}".format(window.winfo_x()+30, window.winfo_screenheight() - 700))
    clkakmf = tk.Label(newwindow, text='', font=fnt,bg="orange",fg="white")
    clkakmf.place(x=20, y=60, relwidth=1, height=50)  # position the label at the top of the window and make it full widt
    clkkmf = tk.Label(newwindow, text='', font=fnt,bg="orange",fg="white")
    clkkmf.place(x=20, y=120, relwidth=1, height=50) 
    clkmf = tk.Label(newwindow, text='', font=fnt,bg="orange",fg="white")
    clkmf.place(x=20, y=180, relwidth=1, height=50)
    clkf = tk.Label(newwindow, text='', font=fnt,bg="orange",fg="white")
    clkf.place(x=20, y=240, relwidth=1, height=50)  
    clkkrm= tk.Label(newwindow, text='', font=fnt,bg="orange",fg="white")
    clkkrm.place(x=20, y=300, relwidth=1, height=50) 
    clkbigha= tk.Label(newwindow, text='', font=fnt,bg="orange",fg="white")
    clkbigha.place(x=20, y=360, relwidth=1, height=50) 
    foot=msg5
    footforbkmf=foot
    footforbmf=foot
    footforbf=foot
    footforkrm=foot
    footforbigha=foot
    a=0.0
    k=0.0
    m=0.0
    if(foot>=fixxacre):
    	a=foot//fixxacre
    	foot=foot%fixxacre
    if(foot>=fixxkanal):
    	k=foot//fixxkanal
    	foot=foot%fixxkanal
    if(foot>=fixxmarla):
    	m=foot//fixxmarla
    	foot=foot%fixxmarla
    clkakmf.config(text=f"ACRE {a}  KANAL {k}  Marla {m}  Foot {round(foot,3)}",font=efnt,width=13,anchor="w")
    a=0.0
    k=0.0
    m=0.0
    foot=footforbkmf
    if(foot>=fixxkanal):
    	k=foot//fixxkanal
    	foot=foot%fixxkanal
    if(foot>=fixxmarla):
    	m=foot//fixxmarla
    	foot=foot%fixxmarla
    clkkmf.config(text=f"\tKANAL {k}  Marla {m}  Foot {round(foot,3)}",anchor="w",font=efnt,width=13)
    a=0.0
    k=0.0
    m=0.0
    foot=footforbmf
    if(foot>=fixxmarla):
    	m=foot//fixxmarla
    	foot=foot%fixxmarla
    clkmf.config(text=f"\t\tMarla {m}  Foot {round(foot,3)}",anchor="w",font=efnt,width=13)
    a=0.0
    k=0.0
    m=0.0
    foot=footforbf
    bf.config(text=f"\t\t\tFoot {round(foot,3)}",font=efnt,width=13)
    a=0.0
    k=0.0
    m=0.0
    foot=footforkrm
    clkkrm.config(text=f"\t\t\tKARAM {round(foot/fixxkaramdbl)}",font=efnt,width=13)
    a=0.0
    k=0.0
    m=0.0
    foot=footforbigha
    big=0.0#
    if(foot>=21780):
    	big=foot//21780
    	foot=foot%21780
    if(foot>=fixxkanal):
    	k=foot//fixxkanal
    	foot=foot%fixxkanal
    if(foot>=fixxmarla):
    	m=foot//fixxmarla
    	foot=foot%fixxmarla
    clkbigha.config(text=f"BIGHA {big}  KANAL {k}  Marla {m}  Foot {round(foot,3)}",anchor="w",font=efnt,width=13)
	
    #new wind end
    
    
virp1lbl.bind("<Double-Button-1>", clk1)
virp2lbl.bind("<Double-Button-1>", clk2)
virp3lbl.bind("<Double-Button-1>", clk3)
virp4lbl.bind("<Double-Button-1>", clk4)
virp5lbl.bind("<Double-Button-1>", clk5)
virp1.bind('<KeyRelease>',virasatcal )
virp2.bind('<KeyRelease>',virasatcal )
virp3.bind('<KeyRelease>',virasatcal )
virp4.bind('<KeyRelease>',virasatcal )
virp5.bind('<KeyRelease>',virasatcal )
virasatcal(1)#critical


#virasat end
#negative start
neglbl = tk.Label(window, text='NEGATIVE')
neglbl.grid(row=30, column=0)
neghdlbl = tk.Label(window, text="ACRE")
neghdlbl.grid(row=31, column=0)
neghdlbl = tk.Label(window, text="KANAL")
neghdlbl.grid(row=31, column=1)
neghdlbl = tk.Label(window, text="MARLA")
neghdlbl.grid(row=31, column=2)
neghdlbl = tk.Label(window, text="FOOT")
neghdlbl.grid(row=31, column=3)
neghdlbl = tk.Label(window, text="BIGHA")
neghdlbl.grid(row=31, column=4)
negacre1= tk.Entry(window,fg="blue",width=7)
negacre1.grid(row=32, column=0)
negkanal1= tk.Entry(window,fg="blue",width=7)
negkanal1.grid(row=32, column=1)
negmarla1= tk.Entry(window,fg="blue",width=7)
negmarla1.grid(row=32, column=2)
negfoot1= tk.Entry(window,fg="blue",width=7)
negfoot1.grid(row=32, column=3)
negbigha1= tk.Entry(window,fg="blue",width=7)
negbigha1.grid(row=32, column=4)
negacre2= tk.Entry(window,fg="blue",width=7)
negacre2.grid(row=33, column=0)
negkanal2= tk.Entry(window,fg="blue",width=7)
negkanal2.grid(row=33, column=1)
negmarla2= tk.Entry(window,fg="blue",width=7)
negmarla2.grid(row=33, column=2)
negfoot2= tk.Entry(window,fg="blue",width=7)
negfoot2.grid(row=33, column=3)
negbigha2= tk.Entry(window,fg="blue",width=7)
negbigha2.grid(row=33, column=4)
negacre3= tk.Entry(window,fg="blue",width=7)
negacre3.grid(row=34, column=0)
negkanal3= tk.Entry(window,fg="blue",width=7)
negkanal3.grid(row=34, column=1)
negmarla3= tk.Entry(window,fg="blue",width=7)
negmarla3.grid(row=34, column=2)
negfoot3= tk.Entry(window,fg="blue",width=7)
negfoot3.grid(row=34, column=3)
negbigha3= tk.Entry(window,fg="blue",width=7)
negbigha3.grid(row=34, column=4)
def negreset():
	response4 = messagebox.askyesno("Reset All Values", "Reset")
	if response4:
		print("Congratulations!")
	else:
		return
	negacre1.delete("0",tk.END)
	negacre2.delete("0",tk.END)
	negacre3.delete("0",tk.END)
	negkanal1.delete("0",tk.END)
	negkanal2.delete("0",tk.END)
	negkanal3.delete("0",tk.END)
	negmarla1.delete("0",tk.END)
	negmarla2.delete("0",tk.END)
	negmarla3.delete("0",tk.END)
	negfoot1.delete("0",tk.END)
	negfoot2.delete("0",tk.END)
	negfoot3.delete("0",tk.END)
	negbigha1.delete("0",tk.END)
	negbigha2.delete("0",tk.END)
	negbigha3.delete("0",tk.END)
negbtnreset = tk.Button(window, text="RESET",bg="red",fg="white",command=negreset)
negbtnreset.grid(row=35, column=3)
def negcal():
	btot=0
	err=0
	acre=kanal=marla=foot=bigha=0
	try:
		acre=float(eval(negacre1.get()))*fixxacre
	except:
		acre=0.0
		err=1
	try:
		kanal=float(eval(negkanal1.get()))*fixxkanal
	except:
		kanal=0.0
		err=1
	try:
		
		marla=float(eval(negmarla1.get()))*fixxmarla
	except:
		marla=0.0
		err=1
		
	try:
		
		ft=float(eval(negfoot1.get()))
	except:
		ft=0.0
		err=1
	try:
		
		bigha=float(eval(negbigha1.get()))*21780
	except:
		bigha=0.0
		err=1
	
	totly=acre+kanal+marla+ft+bigha
	acre=kanal=marla=foot=bigha=0
	try:
		acre=float(eval(negacre2.get()))*fixxacre
	except:
		acre=0.0
		err=1
	try:
		kanal=float(eval(negkanal2.get()))*fixxkanal
	except:
		kanal=0.0
		err=1
	try:
		
		marla=float(eval(negmarla2.get()))*fixxmarla
	except:
		marla=0.0
		err=1
		
	try:
		
		ft=float(eval(negfoot2.get()))
	except:
		ft=0.0
		err=1
	try:
		
		bigha=float(eval(negbigha2.get()))*21780
	except:
		bigha=0.0
		err=1
	min1=acre+kanal+marla+ft+bigha
	try:
		acre=float(eval(negacre3.get()))*fixxacre
	except:
		acre=0.0
		err=1
	try:
		kanal=float(eval(negkanal3.get()))*fixxkanal
	except:
		kanal=0.0
		err=1
	try:
		
		marla=float(eval(negmarla3.get()))*fixxmarla
	except:
		marla=0.0
		err=1
		
	try:
		
		ft=float(eval(negfoot3.get()))
	except:
		ft=0.0
		err=1
	try:
		
		bigha=float(eval(negbigha3.get()))*21780
	except:
		bigha=0.0
		err=1
	
	min2=acre+kanal+marla+ft+bigha
	acre=kanal=marla=foot=bigha=0
	foot=totly-min1-min2
	newwindow = tk.Toplevel(window)
	newwindow.title("VIRASAT HISSA-5")
	newwindow.geometry("900x500+{}+{}".format(window.winfo_x()+30, window.winfo_screenheight() - 700))
	clkakmf = tk.Label(newwindow, text='', font=fnt,bg="orange",fg="white")
	clkakmf.place(x=20, y=60, relwidth=1, height=50)  # position the label at the top of the window and make it full widt
	clkkmf = tk.Label(newwindow, text='', font=fnt,bg="orange",fg="white")
	clkkmf.place(x=20, y=120, relwidth=1, height=50) 
	clkmf = tk.Label(newwindow, text='', font=fnt,bg="orange",fg="white")
	clkmf.place(x=20, y=180, relwidth=1, height=50)
	clkf = tk.Label(newwindow, text='', font=fnt,bg="orange",fg="white")
	clkf.place(x=20, y=240, relwidth=1, height=50)  
	clkkrm= tk.Label(newwindow, text='', font=fnt,bg="orange",fg="white")
	clkkrm.place(x=20, y=300, relwidth=1, height=50) 
	clkbigha= tk.Label(newwindow, text='', font=fnt,bg="orange",fg="white")
	clkbigha.place(x=20, y=360, relwidth=1, height=50) 
	footforbkmf=foot
	footforbmf=foot
	footforbf=foot
	footforkrm=foot
	footforbigha=foot
	a=k=m=0.0
	if(foot>=fixxacre):
	   a=foot//fixxacre
	   foot=foot%fixxacre
	if(foot>=fixxkanal):
	   k=foot//fixxkanal
	   foot=foot%fixxkanal
	if(foot>=fixxmarla):
	   m=foot//fixxmarla
	   foot=foot%fixxmarla
	clkakmf.config(text=f"ACRE {a}  KANAL {k}  Marla {m}  Foot {round(foot,3)}",font=efnt,width=13,anchor="w")
    
negbtncal= tk.Button(window, text="CALC",bg="green",fg="white",command=negcal)
negbtncal.grid(row=35, column=1)
#negative end
window.mainloop()