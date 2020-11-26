# Author : Rahat Khan Tusar(RKT)
# Github : https://github.com/r3k4t

import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def window():
   app = QApplication([])
   w = QDialog()
   b1 = QPushButton(w)
   b1.setText("Ip Check")
   b1.move(50,20)
   b1.clicked.connect(b1_clicked)
   
   b2 = QPushButton(w)
   b2.setText("Exit")
   b2.move(50,50)
   b2.clicked.connect(b2_clicked)
   

   w.setGeometry(100,200,200,100)
   os.system("clear")
   print ("==================================== ")
   print ("          GUI IP Checker             ")
   print ("==================================== ")
   print (" Author : Rahat Khan Tusar(RKT)      ")
   print ("==================================== ")
   print (" Github : https://github.com/r3k4t   ")
   print ("==================================== ")
   w.setWindowTitle("GIC")


   w.show()
   sys.exit(app.exec_())
   



def b1_clicked():
   os.system("curl https://httpbin.org/ip")
   

def b2_clicked():
   sys.exit(1)



if __name__ == '__main__':
   window()
