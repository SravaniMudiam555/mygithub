import os.path
from os import path

import tkinter as tk
from tkinter.messagebox import *
import os
import shutil

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 700,  relief = 'raised', bg="pink")
canvas1.pack()

label1 = tk.Label(root, text='Master Files ')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='enter Environment name')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

label3 = tk.Label(root, text='Enter the Desination Path')
label3.config(font=('helvetica', 10))
canvas1.create_window(200, 200, window=label3)

label4 = tk.Label(root, text='enter jira number')
label4.config(font=('helvetica', 10))
canvas1.create_window(200, 300, window=label4)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

entry2 = tk.Entry (root) 
canvas1.create_window(200, 240, window=entry2)

entry3 = tk.Entry (root) 
canvas1.create_window(200, 340, window=entry3)

def getPath ():
    
    region = entry1.get()
    x      = entry2.get()
    y      = entry3.get()
    isExist = os.path.exists(x)
    path   = x.replace("\\","/")
     
    if region == 'DC0R'or 'dc0r':
        to_find =y 
        #directory = os.listdir(region)
        Region = 'C:\Accounts\SRR\jiras'
        directory = os.listdir(Region)
        #Regio = '//dmdqatfsx.fsg.amer.csc.com/test1/DAPWIN/SRR/DC0R/Mstrres/FSIUSER'
        #print(regio)
        #file1 = open(Regio, "r")
        #readfile = file1.read()
        #if string1 in readfile:*/
        for fname in directory: # change directory as needed
            if y in fname:
                f = open(fname,'r')
                def showinfo3():
                    showinfo("PopUp","jira found")
                showinfo3()
            else:
                 
                    showinfo("PopUp","jira not found")
                
               
        
        file1.close() 
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
   
    
    
button1 = tk.Button(text='Enter', command=getPath, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 480, window=button1)

root.mainloop()