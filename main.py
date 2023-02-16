import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.uic import *
import sys
import os
#print(dir(PyQt5.QtWidgets.QFileDialog))
# getOpenFileName   getSaveFileName
from editor import *
FORM  = Ui_MainWindow
#FORM ,_ = loadUiType('editor.ui')
class APP(QMainWindow,FORM):
    def __init__(self,parent=None):
        super(APP, self).__init__(parent)
        QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.update()

    def update(self):
        self.actionopen_file_2.triggered.connect(self.newfile)
        self.actionsave.triggered.connect(self.savefile)


    def newfile(self):
        
        file=QFileDialog.getOpenFileName(self,"open file",".","All Files (*.txt)")
        print(file[0])
        self.setWindowTitle(str(file[0]))
        with open(file[0],"r") as f:
            r=f.read()
            self.textEdit.setPlainText(str(r))
            f.close()



    def savefile(self):
        path=str(self.windowTitle())
        pextpath=path.replace("/","//")
        text=str(self.textEdit.toPlainText())
        comm=f"del {pextpath}"
        os.system(comm)



    def saveasfile(self):
        pass
    def openfile(self):
        pass
    def newWindow(self):
        pass
    def copy(self):
        pass
    def cut(self):
        pass
    def paste(self):
        pass
    def clear(self):
        pass
    def redo(self):
        pass
    def undo(self):
        pass
    def search(self):
        pass
    def find(self):
        pass
    def findof(self):
        pass
    def replace(self):
        pass
    def zoomin(self):
        pass
    def zoomout(self):
        pass
    def defiult(self):
        pass
    def black(self):
        pass
    def white(self):
        pass
    def red(self):
        pass
    def blue(self):
        pass
    def green(self):
        pass
    def costumcolor(self):
        pass
    def darkmode(self):
        pass
    def whitemode(self):
        pass
    def highlightmode(self):
        pass
    def redmode(self):
        pass
    def bluemode(self):
        pass


if __name__ == '__main__':

    app=QApplication(sys.argv)
    win=APP()
    win.show()
    sys.exit(app.exec_())






