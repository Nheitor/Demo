# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_MainXwuGZH.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QMainWindow, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
        MainWindow.setStyleSheet(u"#centralwidget{\n"
"	background-color : #fff\n"
"}\n"
"#main_w{\n"
"	border-right : 2px solid;\n"
"}\n"
"#warning{\n"
"	border : none;\n"
"	color : rgb(255, 0, 0);\n"
"}\n"
"#rc_box, #matrix_box{\n"
"	border : 2px solid;\n"
"	border-radius : 10px;\n"
"	background-color : palette(base);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.start_w = QWidget(self.centralwidget)
        self.start_w.setObjectName(u"start_w")
        self.start_w.setStyleSheet(u"QGroupBox{\n"
"	\n"
"}")
        self.verticalLayout = QVBoxLayout(self.start_w)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.input_w = QWidget(self.start_w)
        self.input_w.setObjectName(u"input_w")
        self.verticalLayout_3 = QVBoxLayout(self.input_w)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 5, 0, 0)
        self.groupBox = QGroupBox(self.input_w)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"JetBrains Mono"])
        font.setPointSize(10)
        font.setBold(True)
        self.groupBox.setFont(font)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.rc_box = QTextEdit(self.groupBox)
        self.rc_box.setObjectName(u"rc_box")
        self.rc_box.setMaximumSize(QSize(180, 100))
        self.rc_box.setFont(font)
        self.rc_box.setLineWrapMode(QTextEdit.NoWrap)

        self.horizontalLayout_2.addWidget(self.rc_box)


        self.verticalLayout_3.addWidget(self.groupBox, 0, Qt.AlignTop)

        self.groupBox_2 = QGroupBox(self.input_w)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setFont(font)
        self.horizontalLayout = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.matrix_box = QTextEdit(self.groupBox_2)
        self.matrix_box.setObjectName(u"matrix_box")
        self.matrix_box.setFont(font)
        self.matrix_box.setLineWrapMode(QTextEdit.NoWrap)

        self.horizontalLayout.addWidget(self.matrix_box)


        self.verticalLayout_3.addWidget(self.groupBox_2)


        self.verticalLayout.addWidget(self.input_w)

        self.warning_w = QWidget(self.start_w)
        self.warning_w.setObjectName(u"warning_w")
        self.horizontalLayout_3 = QHBoxLayout(self.warning_w)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.warning = QPushButton(self.warning_w)
        self.warning.setObjectName(u"warning")
        self.warning.setFont(font)
        self.warning.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.warning)


        self.verticalLayout.addWidget(self.warning_w)

        self.func_w = QWidget(self.start_w)
        self.func_w.setObjectName(u"func_w")
        self.verticalLayout_2 = QVBoxLayout(self.func_w)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.create_btn = QPushButton(self.func_w)
        self.create_btn.setObjectName(u"create_btn")
        self.create_btn.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setFamilies([u"JetBrains Mono"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.create_btn.setFont(font1)
        self.create_btn.setStyleSheet(u"#create_btn{	\n"
"	border : 2px solid;\n"
"	border-radius : 15px;\n"
"	height : 30px;\n"
"	background-color : rgb(255, 204, 152)\n"
"}\n"
"#create_btn:hover{\n"
"	background-color : rgb(255, 165, 167)\n"
"}\n"
"")
        self.create_btn.setCheckable(True)

        self.verticalLayout_2.addWidget(self.create_btn)

        self.start_stop_btn = QPushButton(self.func_w)
        self.start_stop_btn.setObjectName(u"start_stop_btn")
        self.start_stop_btn.setMaximumSize(QSize(16777215, 50))
        self.start_stop_btn.setFont(font1)
        self.start_stop_btn.setStyleSheet(u"#start_stop_btn{	\n"
"	border : 2px solid;\n"
"	border-radius : 15px;\n"
"	height : 30px;\n"
"	background-color : rgb(70, 255, 153)\n"
"}\n"
"#start_stop_btn:hover{\n"
"	background-color : rgb(90, 203, 255)\n"
"}\n"
"")
        self.start_stop_btn.setCheckable(True)

        self.verticalLayout_2.addWidget(self.start_stop_btn)


        self.verticalLayout.addWidget(self.func_w)


        self.gridLayout.addWidget(self.start_w, 0, 1, 1, 1)

        self.main_w = QWidget(self.centralwidget)
        self.main_w.setObjectName(u"main_w")
        self.main_w.setMinimumSize(QSize(600, 600))
        self.main_w.setMaximumSize(QSize(600, 600))
        self.gridLayout_2 = QGridLayout(self.main_w)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(15, 15, 15, 15)
        self.matrix_w = QWidget(self.main_w)
        self.matrix_w.setObjectName(u"matrix_w")

        self.gridLayout_2.addWidget(self.matrix_w, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.main_w, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Nh\u1eadp s\u1ed1 h\u00e0ng, c\u1ed9t", None))
        self.rc_box.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nh\u1eadp...", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Nh\u1eadp ma tr\u1eadn", None))
        self.matrix_box.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nh\u1eadp...", None))
        self.warning.setText(QCoreApplication.translate("MainWindow", u"Kh\u00f4ng h\u1ee3p l\u1ec7", None))
        self.create_btn.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.start_stop_btn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
    # retranslateUi

