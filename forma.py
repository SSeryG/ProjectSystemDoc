import sys
import os
from tkinter import *

import tkinter.filedialog as fd
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
from file import FileClass
#import errorbox
import threading


class App(Tk):
   def __init__(self):  
      self.file=FileClass()
      super().__init__()        
      self.title('SD')
      self.minsize(319,349)
      self.maxsize(321,351)
      self.geometry('320x350')  
      self.labelinputpath=Label(self,font='Arial 10',text="Папка с документами")
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

      self.labeltransferpath=Label(self,font='Arial 10',text="Папка перемещения документов")
      self.labeltransferpath.place(x = 40,y = 120)

      self.entrytransferpath=Entry(self,font='Arial 10')
      self.entrytransferpath.place(x = 40,y = 140,width=200,height=15)
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
         text="Проход по папкам",
         command=threading.Thread(target=self.ClicPusk).start
      )
      self.pusk.place(x=40,y=200,width=235,height=20)

      self.createfile=Button(
         self,
         text="Создание папок",
         command=threading.Thread(target=self.ClicCreate).start
      )
      self.createfile.place(x=40,y=240,width=235,height=20)
         
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
     # try:         
      self.file.AbsolutePath(path)
      #except:         
         #errorbox.InputEntry(path)


   def ClicCreate(self):
      path=self.entrytransferpath.get()
      #try:         
      self.file.CreateDirectory(path)
      #except:
         #errorbox.TransferEntry(path)

if __name__=="__main__":
   app=App()
   app.mainloop()



'''
class window(QWidget):   
   def __init__(self, parent = None):
      self.file=FileClass()
      super(window, self).__init__(parent)
      window.msg = QMessageBox()       
      self.resize(350,350)
      self.setWindowTitle("СД")
  
          
      self.label1=QLabel(self)
      self.label1.setFont(QFont('Arial',8))
      self.label1.setText('Папка с документами')      
      self.label1.move(50,125)


      self.TextEdit1 = QLineEdit(self)
      self.TextEdit1.setFont(QFont('Arial',8))      
      self.TextEdit1.move(40, 140)
      self.TextEdit1.resize(200,20)


      self.openDirButton = QPushButton(self)
      self.openDirButton.setIcon(QIcon('icondir.svg'))      
      self.openDirButton.move(240, 140) 
      self.openDirButton.resize(20,20) 
      self.openDirButton.clicked.connect(self.getDirectory)


      self.label2=QLabel(self)
      self.label2.setFont(QFont('Arial',8))
      self.label2.setText('Папка назначения')
      self.label2.move(50,175)


      self.TextEdit2 = QLineEdit(self)
      self.TextEdit2.setFont(QFont('Arial',8))
      self.TextEdit2.move(40, 190)
      self.TextEdit2.resize(200,20)

      self.openDirButton2 = QPushButton(self)
      self.openDirButton2.setIcon(QIcon('icondir.svg'))
      self.openDirButton2.move(240, 190) 
      self.openDirButton2.resize(20,20)
      self.openDirButton2.clicked.connect(self.getDirectory2)


      self.PuskButton = QPushButton(self)
       #self.PuskButton.setIcon()
      self.PuskButton.move(50, 220) 
      self.PuskButton.resize(200,20) 
      self.PuskButton.clicked.connect(self.PuskClic) 
       
      self.CreateButton = QPushButton(self)
       #self.PuskButton.setIcon()
      self.CreateButton.move(50, 250) 
      self.CreateButton.resize(200,20) 
      self.CreateButton.clicked.connect(self.CreateClic) 
      
   def getDirectory(self):           
      dirlist = QFileDialog.getExistingDirectory(self,"Выбрать папку",".")
      self.TextEdit1.setText(dirlist)
      

   def getDirectory2(self):                                                     
      dirlist = QFileDialog.getExistingDirectory(self,"Выбрать папку",".")
      self.TextEdit2.setText(dirlist)
    
   def PuskClic(self):#запуск обхода папок
      #try:
         strp=self.TextEdit1.text()                                                              
         self.file.AbsolutePath(strp)
      #except:         
       #  window.msg.setIcon(QMessageBox.Information) 
  
         # setting message for Message Box 
        # window.msg.setText("Information ") 
      
      # setting Message box window title 
         #window.msg.setWindowTitle("Information MessageBox") 
      
      # declaring buttons on Message Box 
         #window.msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel) 
      
      # start the app 
         #retval = window.msg.exec_() 

   def CreateClic(self):#создание папок
      strp=self.TextEdit2.text()                                                           
      self.file.CreateDirectory(strp)

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = window()
   ex.show()
   sys.exit(app.exec_())
'''