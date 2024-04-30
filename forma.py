import os
from tkinter import *

import tkinter.filedialog as fd

from file import FileClass
import errorbox
from threading import Thread
import time
import asyncio


class App(Tk):
   def __init__(self):  
      self.file=FileClass()
      super().__init__()        
      self.title('Систематизация файлов')
      self.minsize(319,349)
      self.maxsize(321,351)
      self.geometry('320x350')  
      self.labelinputpath=Label(self,font='Arial 9',text="Выберите файлы")
      self.labelinputpath.place(x = 40,y = 70)

      self.entryinputpath=Entry(self,font='Arial 10')
      self.entryinputpath.place(x = 40,y = 90,width=200,height=15)
      self.entryinputpath.insert(0,"C:/Dekstop/dir")

      self.photodelete=PhotoImage(file="icon/icondelete.png")
      self.photodir=PhotoImage(file="icon/icondir.png")
      self.deleteinputbtn=Button(
         self,
         image =self.photodelete,
         command=self.ClicDelEntryInput
      )
      self.deleteinputbtn.place(x=245,y=90,width=15,height=15)

      self.diropeninputbtn=Button(
         self,
         image=self.photodir,
         command=self.ClicOpenDirInpat
      )
      self.diropeninputbtn.place(x=260,y=90,width=15,height=15)

      self.labeltransferpath=Label(self,font='Arial 9',text="Папка для систематизированных файлов")
      self.labeltransferpath.place(x = 40,y = 120)

      self.entrytransferpath=Entry(self,font='Arial 10')
      self.entrytransferpath.place(x = 40,y = 140 ,width=200,height=15)
      self.entrytransferpath.insert(0,"C:/Dekstop/dir")

      self.deletetransferbtn=Button(
         self,
         image =self.photodelete,
         activeforeground = "Gray",
         command=self.ClicDelEntryTransfer
      )
      self.deletetransferbtn.place(x=245,y=140,width=15,height=15) 

      self.diropentransferbtn=Button(
         self,
         image=self.photodir,
         command=self.ClicOpenDirTransfer
      )
      self.diropentransferbtn.place(x=260,y=140,width=15,height=15)

      self.pusk=Button(
         self,
         text="Загрузка и обработка файлов",
         command=self.ClicPusk
      )
      self.pusk.place(x=40,y=200,width=235,height=20)

      self.createfile=Button(
         self,
         text="Систематизация файлов",
         command=self.ClicCreate
      )
      self.createfile.place(x=40,y=240,width=235,height=20)
      
      self.clean=Button(
         self,
         text="очистить кэш",
         command=self.CleanData
      )
      self.clean.place(x=40,y=40,width=100,height=20)
         
  


   def CleanData(self):
      if errorbox.Info():
         try:
            os.remove("data/data.csv")
         except:
            errorbox.ErrorData()

   
   def ClicDelEntryInput(self):
      self.entryinputpath.delete(0,END)

   def ClicDelEntryTransfer(self):
      self.entrytransferpath.delete(0,END)

   def ClicOpenDirInpat(self):
      self.directory = fd.askdirectory(title="Выбрать папку", initialdir="/")
      self.entryinputpath.delete(0,END)
      self.entryinputpath.insert(0,self.directory)

   def ClicOpenDirTransfer(self):
      self.directory = fd.askdirectory(title="Выбрать папку", initialdir="/")
      self.entrytransferpath.delete(0,END)
      self.entrytransferpath.insert(0,self.directory)

   def ClicPusk(self):
      path=self.entryinputpath.get()
      #try:         
      asyncio.run(self.file.AbsolutePath(path))
      
      #thread.start()
      #self.file.AbsolutePath(path)
      #self.pusk.config(relief=RAISED)
      #self.title("(Загружает файлы...)")

      #time.sleep(5)  # Имитация длительной операции
      #if thread.is_alive:
      #   self.title("Систематизация файлов")
      #   self.pusk.config(relief=SUNKEN)
      #except:         
        # errorbox.ErrorPath(path)


   def ClicCreate(self):

      path=self.entrytransferpath.get()
      #try:         
      asyncio.run(self.file.CreateDirectory(path))
      
      ##self.file.AbsolutePath(path)
      #self.pusk.config(relief=RAISED)
      #self.title("(Систематизирует файлы...)")

      #time.sleep(5)  # Имитация длительной операции
      #if thread.is_alive:
       #  self.title("Систематизация файлов")
        # self.pusk.config(relief=SUNKEN)
      
      #except:         
      #errorbox.ErrorPath(path)

if __name__=="__main__":
   app=App()
   app.mainloop()