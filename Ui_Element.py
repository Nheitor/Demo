# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_ElementggIPoC.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QPushButton, QSizePolicy,
    QWidget)

class Ui_ElMatr(object):
    def setupUi(self, ElMatr):
        if not ElMatr.objectName():
            ElMatr.setObjectName(u"ElMatr")
        ElMatr.resize(50, 50)
        ElMatr.setMinimumSize(QSize(50, 50))
        ElMatr.setMaximumSize(QSize(50, 50))
        ElMatr.setStyleSheet(u"background-color : #fff;\n"
"border : 1px solid;\n"
"")
        self.gridLayout = QGridLayout(ElMatr)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.cell_w = QWidget(ElMatr)
        self.cell_w.setObjectName(u"cell_w")
        self.cell_w.setMinimumSize(QSize(50, 50))
        self.cell_w.setMaximumSize(QSize(50, 50))
        self.gridLayout_2 = QGridLayout(self.cell_w)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.cell_p = QPushButton(self.cell_w)
        self.cell_p.setObjectName(u"cell_p")
        self.cell_p.setMinimumSize(QSize(50, 50))
        self.cell_p.setMaximumSize(QSize(50, 50))
        font = QFont()
        font.setFamilies([u"JetBrains Mono"])
        font.setPointSize(10)
        font.setBold(True)
        self.cell_p.setFont(font)
        self.cell_p.setStyleSheet(u"")
        self.cell_p.setFlat(True)
        self.cell_p.setDisabled(True)
        self.gridLayout_2.addWidget(self.cell_p, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.cell_w, 0, 0, 1, 1)


        self.retranslateUi(ElMatr)

        QMetaObject.connectSlotsByName(ElMatr)
    # setupUi

    def retranslateUi(self, ElMatr):
        ElMatr.setWindowTitle(QCoreApplication.translate("ElMatr", u"Form", None))
        self.cell_p.setText("")
    # retranslateUi

