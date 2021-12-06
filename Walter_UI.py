# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Walter_UI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_Walter(object):
    def setupUi(self, Walter):
        Walter.setObjectName("Walter")
        Walter.resize(1743, 941)
        Walter.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(Walter)
        self.centralwidget.setObjectName("centralwidget")
        self.bg_lab = QtWidgets.QLabel(self.centralwidget)
        self.bg_lab.setGeometry(QtCore.QRect(-120, 0, 1991, 971))
        self.bg_lab.setText("")
        self.bg_lab.setPixmap(QtGui.QPixmap("image/Walter bg.gif"))
        self.bg_lab.setScaledContents(True)
        self.bg_lab.setObjectName("bg_lab")
        self.chat_box_lab = QtWidgets.QLabel(self.centralwidget)
        self.chat_box_lab.setGeometry(QtCore.QRect(1320, 150, 371, 601))
        self.chat_box_lab.setText("")
        self.chat_box_lab.setPixmap(QtGui.QPixmap("image/chatbox_image_2.jpeg"))
        self.chat_box_lab.setScaledContents(True)
        self.chat_box_lab.setObjectName("chat_box_lab")
        self.footer_img = QtWidgets.QLabel(self.centralwidget)
        self.footer_img.setGeometry(QtCore.QRect(10, 890, 1901, 41))
        self.footer_img.setText("")
        self.footer_img.setPixmap(QtGui.QPixmap("image/footer(line).gif"))
        self.footer_img.setScaledContents(True)
        self.footer_img.setObjectName("footer_img")
        self.time_lab = QtWidgets.QLabel(self.centralwidget)
        self.time_lab.setGeometry(QtCore.QRect(120, 40, 331, 171))
        self.time_lab.setText("")
        self.time_lab.setPixmap(QtGui.QPixmap("image/date-time_border-removebg-preview.png"))
        self.time_lab.setScaledContents(True)
        self.time_lab.setObjectName("time_lab")
        self.date_lable = QtWidgets.QLabel(self.centralwidget)
        self.date_lable.setGeometry(QtCore.QRect(120, 170, 261, 111))
        self.date_lable.setText("")
        self.date_lable.setPixmap(QtGui.QPixmap("image/date-time_border-removebg-preview.png"))
        self.date_lable.setScaledContents(True)
        self.date_lable.setObjectName("date_lable")
        self.run_button = QtWidgets.QPushButton(self.centralwidget)
        self.run_button.setGeometry(QtCore.QRect(870, 470, 163, 39))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.run_button.setFont(font)
        self.run_button.setStyleSheet("background-color: rgb(255, 78, 81);\n"
"")
        self.run_button.setObjectName("run_button")
        self.state_lab = QtWidgets.QLabel(self.centralwidget)
        self.state_lab.setGeometry(QtCore.QRect(1140, 750, 241, 121))
        self.state_lab.setText("")
        self.state_lab.setPixmap(QtGui.QPixmap("image/date-time_border-removebg-preview.png"))
        self.state_lab.setScaledContents(True)
        self.state_lab.setObjectName("state_lab")
        self.Time = QtWidgets.QTextBrowser(self.centralwidget)
        self.Time.setGeometry(QtCore.QRect(160, 90, 291, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Time.setFont(font)
        self.Time.setStyleSheet("background:transparent;\n"
"color: rgb(255, 255, 255);\n"
"border-radius:none;")
        self.Time.setObjectName("Time")
        self.state_of_assistant = QtWidgets.QTextBrowser(self.centralwidget)
        self.state_of_assistant.setGeometry(QtCore.QRect(1170, 790, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.state_of_assistant.setFont(font)
        self.state_of_assistant.setStyleSheet("background:transparent;\n"
"color: rgb(255, 255, 255);\n"
"border-radius:none;")
        self.state_of_assistant.setObjectName("state_of_assistant")
        self.Date = QtWidgets.QTextBrowser(self.centralwidget)
        self.Date.setGeometry(QtCore.QRect(160, 200, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Date.setFont(font)
        self.Date.setStyleSheet("background:transparent;\n"
"color: rgb(255, 255, 255);\n"
"border-radius:none;")
        self.Date.setObjectName("Date")
        self.Chat_box = QtWidgets.QTextBrowser(self.centralwidget)
        self.Chat_box.setGeometry(QtCore.QRect(1350, 210, 311, 521))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Chat_box.setFont(font)
        self.Chat_box.setStyleSheet("background:transparent;\n"
"color: rgb(255, 255, 255);\n"
"border-radius:none;")
        self.Chat_box.setObjectName("Chat_box")
        self.Terminate = QtWidgets.QPushButton(self.centralwidget)
        self.Terminate.setGeometry(QtCore.QRect(60, 790, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Terminate.setFont(font)
        self.Terminate.setStyleSheet("background-color: rgb(75, 255, 228);\n"
"color: rgb(0, 0, 0);")
        self.Terminate.setObjectName("Terminate")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 360, 491, 281))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("image/date-time_border-removebg-preview.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(40, 450, 411, 111))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background:transparent;\n"
"border-radius:none;\n"
"color: rgb(44, 255, 238);")
        self.textBrowser.setObjectName("textBrowser")
        Walter.setCentralWidget(self.centralwidget)

        self.retranslateUi(Walter)
        QtCore.QMetaObject.connectSlotsByName(Walter)

    def retranslateUi(self, Walter):
        _translate = QtCore.QCoreApplication.translate
        Walter.setWindowTitle(_translate("Walter", "Desktop Assistant - WALTER"))
        Walter.setWindowIcon(QIcon("image/logo.png"))
        self.run_button.setText(_translate("Walter", "Run"))
        self.Time.setHtml(_translate("Walter", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:24pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:28pt;\"><br /></p></body></html>"))
        self.state_of_assistant.setHtml(_translate("Walter", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Date.setHtml(_translate("Walter", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:17pt;\"><br /></p></body></html>"))
        self.Chat_box.setHtml(_translate("Walter", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p></body></html>"))
        self.Terminate.setText(_translate("Walter", "Terminate"))
        self.textBrowser.setHtml(_translate("Walter", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:30pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt;\">W A L T E R</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Walter = QtWidgets.QMainWindow()
    ui = Ui_Walter()
    ui.setupUi(Walter)
    Walter.show()
    sys.exit(app.exec_())

