import os
from tkinter import *

root=Tk()

root.title('Manage Computer-All in One Place')
root.config(background='skyblue')

titleimage=PhotoImage(file='title.png')

titlelabel=Label(root,text='Computer manager',font=('Sans Serif',25,'bold'),image=titleimage,compound=LEFT)
titlelabel.grid()

frame=Frame(root,bd=8,relief=SUNKEN,bg='white')
frame.grid(row=1)

taskimage=PhotoImage(file='task.png')
Button(frame,text="Task Manager",font=('Sans Serif',15,'bold'),image=taskimage,compound=LEFT,fg='green',
bg='white',cursor='hand2',bd=0,command=lambda:os.system('taskmgr')).grid(padx=10,pady=10,sticky='w')

controlpanelimage=PhotoImage(file='controlpanel.png')
Button(frame,text="Control Panel",font=('Sans Serif',15,'bold'),image=controlpanelimage,compound=LEFT,fg='red',
bg='white',cursor='hand2',bd=0,command=lambda:os.system('control')).grid(row=0,column=1,padx=10,pady=10,sticky='w')

datetimeimage=PhotoImage(file='datetime.png')
Button(frame,text="Date and Time",font=('Sans Serif',15,'bold'),fg='green',image=datetimeimage,compound=LEFT,cursor='hand2',
bg='white',bd=0,command=lambda:os.system('timedate.cpl')).grid(padx=10,pady=10,sticky='w')

networkimg=PhotoImage(file='network.png')
Button(frame,text="Network Config",font=('Sans Serif',15,'bold'),fg='blue',image=networkimg,compound=LEFT,cursor='hand2',
bg='white',bd=0,command=lambda:os.system('ncpa.cpl')).grid(row=1,column=1,padx=10,pady=10,sticky='w')

devmgmtimg=PhotoImage(file='device.png')
Button(frame,text="Device management",font=('Sans Serif',15,'bold'),fg='blue',image=devmgmtimg,compound=LEFT,cursor='hand2',
bg='white',bd=0,command=lambda:os.system('devmgmt.msc')).grid(padx=10,pady=10,sticky='w')

mouseimg=PhotoImage(file='mouse.png')
Button(frame,text="Mouse Setting",font=('Sans Serif',15,'bold'),fg='blue',image=mouseimg,compound=LEFT,cursor='hand2',
bg='white',bd=0,command=lambda:os.system('main.cpl')).grid(row=2,column=1,padx=10,pady=10,sticky='w')

uninstallimg=PhotoImage(file='remove.png')
Button(frame,text="Uninstall App",font=('Sans Serif',15,'bold'),fg='blue',image=uninstallimg,compound=LEFT,cursor='hand2',
bg='white',bd=0,command=lambda:os.system('appwiz.cpl')).grid(padx=10,pady=10,sticky='w')

serviceimg=PhotoImage(file='services.png')
Button(frame,text="System Service",font=('Sans Serif',15,'bold'),fg='yellow',image=serviceimg,compound=LEFT,cursor='hand2',
bg='white',bd=0,command=os.system('services.msc')).grid(row=3,column=1,padx=10,pady=10,sticky='w')

updateimg=PhotoImage(file='update.png')
Button(frame,text="Windows Update",font=('Sans Serif',15,'bold'),fg='black',image=updateimg,compound=LEFT,cursor='hand2',
bg='white',bd=0,command=os.system('control update')).grid(padx=10,pady=10,sticky='w')

sysimg=PhotoImage(file='properties.png')
Button(frame,text="System Properties",font=('Sans Serif',15,'bold'),fg='purple',image=sysimg,compound=LEFT,cursor='hand2',
bg='white',bd=0).grid(row=4,column=1,padx=10,pady=10,sticky='w')

root.mainloop()
