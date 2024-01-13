import sys
import os
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
from file import AbsolutePath


class window(QWidget):
    def __init__(self, parent = None):
       super(window, self).__init__(parent)
 
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
       self.PuskButton.move(50, 300) 
       self.PuskButton.resize(200,20) 
       self.PuskButton.clicked.connect(self.PuskClic) 
            
       

    def getDirectory(self):      
       dirlist = QFileDialog.getExistingDirectory(self,"Выбрать папку",".")
       self.TextEdit1.setText(dirlist)

    def getDirectory2(self):                                                     
       dirlist = QFileDialog.getExistingDirectory(self,"Выбрать папку",".")
       self.TextEdit2.setText(dirlist)
    
    def PuskClic(self):
       strp=self.TextEdit1.text()                                                     
       AbsolutePath(strp)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = window()
    ex.show()
    sys.exit(app.exec_())