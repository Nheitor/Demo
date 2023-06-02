from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QThread, Signal, Slot)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QSizePolicy,
    QWidget)

from Ui_Main import Ui_MainWindow
from Ui_Element import Ui_ElMatr
from time import sleep
from threading import Thread
import math, sys


class ThreadApp(QThread):
    any_signal = Signal()

    def __init__(self, index = 0):
        QThread.__init__(self)
        self.index = index
        self.is_running = True

    def run(self):
        print("start thread", self.index)
        self.any_signal.emit()
    def stop(self):
        print("stop thread", self.index)
        self.terminate()

class ElMatrix(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self)
        self.ui = Ui_ElMatr()
        self.ui.setupUi(self)
        self.setParent(parent)        

    def changeValue(self, v):
        self.ui.cell_p.setText(f"{v}")
    def setPos(self, x, y):
        self.setGeometry(QRect(x, y, 50, 50))
    def selected(self, color):
        self.ui.cell_p.setStyleSheet(f"background-color : {color}")
    def unselected(self):
        self.ui.cell_p.setStyleSheet(u"")

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Set up
        self.dx = [0, 1, 0, -1]
        self.dy = [1, 0, -1, 0]

        self.cellM = []

        self.spacex = (570 - columns * 50) // 2
        self.spacey = (570 - rows * 50) // 2

        self.ui.start_stop_btn.setDisabled(True)
        self.ui.warning_w.setHidden(True)
        self.ui.matrix_w.show()
        self.ui.create_btn.clicked.connect(self.create_event)
        self.ui.start_stop_btn.clicked.connect(self.start_event)
        self.a = 100
        self.thread = {}

    def create_event(self):
        self.setupMatrix()
        self.ui.start_stop_btn.setEnabled(True)

    def setupMatrix(self):
        self.ui.create_btn.setDisabled(True)
        for i in range(rows):
            for j in range(columns):
                cell = ElMatrix(self.ui.matrix_w)
                cell.setPos(50 * j + self.spacex, 50 * i + self.spacey)
                cell.changeValue(a[i][j])
                cell.show()
                self.cellM.append([])
                self.cellM[i].append(cell)

    def start_event(self):
        self.ui.create_btn.setDisabled(True)

        self.ui.start_stop_btn.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.ui.start_stop_btn.setStyleSheet(u"#start_stop_btn{    \n"
"   border : 2px solid;\n"
"   border-radius : 15px;\n"
"   height : 30px;\n"
"   background-color : rgb(90, 203, 255)\n"
"}\n"
"#start_stop_btn:hover{\n"
"   background-color : rgb(70, 255, 153) \n"
"}\n"
"")
        self.thread["_mt"] = ThreadApp(1)
        self.thread["_mt"].start()

        self.thread["_mt"].any_signal.connect(lambda : self.bfs(0, 0, -1 , -1))

        self.ui.start_stop_btn.clicked.disconnect()
        self.ui.start_stop_btn.clicked.connect(self.stop_event)

    def stop_event(self):
        self.thread["_mt"].stop()

        self.ui.start_stop_btn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.ui.start_stop_btn.setStyleSheet(u"#start_stop_btn{    \n"
"   border : 2px solid;\n"
"   border-radius : 15px;\n"
"   height : 30px;\n"
"   background-color : rgb(70, 255, 153)\n"
"}\n"
"#start_stop_btn:hover{\n"
"   background-color : rgb(90, 203, 255)\n"
"}\n"
"")
        self.ui.start_stop_btn.clicked.disconnect()
        self.ui.start_stop_btn.clicked.connect(self.start_event)
        self.ui.create_btn.setEnabled(True)
        print(self.a)

    # BFS Tìm kiếm thể lực tối thiểu từ [0][0] đến [rows][columns] #
    def bfs(self, x, y, ox, oy):
        self.a = 200
        self.cellM[x][y].selected("#2c53ff")
        sleep(0.6)
        
        for i in range(4):
            
            x1 = self.dx[i] + x
            y1 = self.dy[i] + y
            
            if (x1 == ox) and (y1 == oy):
                continue
            
            if (x1 >= 0) and (x1 < rows) and (y1 >= 0) and (y1 < columns):

                self.cellM[x1][y1].selected("#7dafff")
                sleep(0.6)
                

                temp = d[x][y] + abs(a[x][y] - a[x1][y1])
                if temp < d[x1][y1]:
                    d[x1][y1] = temp
                    
                    self.cellM[x1][y1].changeValue(temp)
                    sleep(0.6)
                    
                    if x1 + y1 != rows + columns - 2:
                        
                        self.cellM[x][y].unselected()
                        
                        self.bfs(x1, y1, x, y)
                        
                        self.cellM[x][y].selected("#2c53ff")
                        sleep(0.6)
                
                self.cellM[x1][y1].unselected()


        self.cellM[x][y].unselected()
if __name__ == "__main__":
    a, d, visited = [], [], []
    h = input().split()
    rows = int(h[0])
    columns = int(h[1])
    for i in range(rows):
        t = input().split()
        a.append([])
        d.append([])
        visited.append([])
        for j in range(columns):
            a[i].append(int(t[j]))
            d[i].append(math.inf)
            visited[i].append(False)
    d[0][0] = 0
    app = QApplication(sys.argv)
    root = MainWindow()
    root.show()
    sys.exit(app.exec())

