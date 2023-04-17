import tkinter as tk
from tkinter.messagebox import *
import os
import shutil

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised', bg="pink")
canvas1.pack()

label1 = tk.Label(root, text='Master Files ')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='rEnvironment')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

label3 = tk.Label(root, text='Enter the Desination Path')
label3.config(font=('helvetica', 10))
canvas1.create_window(200, 200, window=label3)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

entry2 = tk.Entry (root) 
canvas1.create_window(200, 240, window=entry2)

def getPath ():
    
    region = entry1.get()
    x      = entry2.get()
    isExist = os.path.exists(x)
    path   = x.replace("\\","/")


    if region == 'DC0R'or 'dc0r':
        Region = '//dmdqatfsx.fsg.amer.csc.com/test1/DAPWIN/SRR/DC0R/Mstrres/DEFLIB'
    elif region == 'QC0R'or 'qc0r':
        Region = '//dmdqatfsx.fsg.amer.csc.com/test1/DAPWIN/SRR/QC0R/Mstrres/DEFLIB'
    elif region == 'QC0A'or 'dc0a':
        Region = '//dmdqatfsx.fsg.amer.csc.com/test1/DAPWIN/SRR/QC0A/Mstrres/DEFLIB'
    elif region == 'XC0R'or 'xc0r':
        Region = '//dmdqatfsx.fsg.amer.csc.com/test1/DAPWIN/SRR/XC0R/Mstrres/DEFLIB'
    elif region == 'STAGE'or 'STAGE':
        Region = '//dmdqatfsx.fsg.amer.csc.com/Stage1/DAPWIN/SRR/Mstrres/DEFLIB'
    elif region == 'PROD'or 'PROD':
        Region = '//dmdprdfs.fsg.amer.csc.com/prod3/DAPWIN/SRR/Mstrres/DEFLIB'
    elif region == 'DC0RAGCY':
        Region = '//dmdqatfsx.fsg.amer.csc.com/test1/DAPWIN/SRR/DC0RAGCY/DEFLIB'
    elif region == 'QC0RAGCY':
        Region = '//dmdqatfsx.fsg.amer.csc.com/test1/DAPWIN/SRR/QC0RAGCY/DEFLIB'
    elif region == 'QC0AAGCY':
        Region = '//dmdqatfsx.fsg.amer.csc.com/test1/DAPWIN/SRR/QC0AAGCY/DEFLIB'
    elif region == 'STAGEAGCY':
        Region = '//dmdqatfsx.fsg.amer.csc.com/Stage1/DAPWIN/SRR/AGCY/DEFLIB'
    elif region == 'PRODAGCY':
        Region = '//dmdprdfs.fsg.amer.csc.com/prod3/DAPWIN/SRR/AGCY/DEFLIB'
    else:
        Region = ' '
   
    if Region!=' ' and isExist == True:

        shutil.copy(Region + '/lbylog.dbf',path)
        shutil.copy(Region + '/lbylog.mdx',path)
        shutil.copy(Region + '/MASTER.dbf',path)
        shutil.copy(Region + '/MASTER.LBY',path)
        shutil.copy(Region + '/MASTER.mdx',path)
    else:
        def showinfo2():
            showinfo("PopUp","Enter Valid Environment and Path")
        showinfo2()

    def showinfo1():
        showinfo("PopUp","Done")
    showinfo1()
    
button1 = tk.Button(text='Enter', command=getPath, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 280, window=button1)

root.mainloop()