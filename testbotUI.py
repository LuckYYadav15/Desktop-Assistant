# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testbotUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_desktop_ui(object):
    def setupUi(self, desktop_ui):
        desktop_ui.setObjectName("desktop_ui")
        desktop_ui.resize(730, 493)
        self.centralwidget = QtWidgets.QWidget(desktop_ui)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 471))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/bgimg.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(510, 420, 91, 31))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(620, 420, 91, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"background-color: rgb(88, 255, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 20, 131, 31))
        self.label_2.setStyleSheet("background:transparent;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"border-radius:none;\n"
"color: rgb(255, 255, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(470, 20, 111, 31))
        self.label_5.setStyleSheet("background:transparent;\n"
"border-radius:none;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(300, 30, 131, 21))
        self.textBrowser.setStyleSheet("background:transparent;\n"
"border-radius:none;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(470, 20, 111, 21))
        self.textBrowser_2.setStyleSheet("background:transparent;\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-radius:none;\n"
"color: rgb(255, 255, 255);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(510, 360, 201, 41))
        self.textBrowser_3.setStyleSheet("background:transparent;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(510, 180, 201, 171))
        self.textBrowser_4.setStyleSheet("background:transparent;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.textBrowser_4.setObjectName("textBrowser_4")
        desktop_ui.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(desktop_ui)
        self.statusbar.setObjectName("statusbar")
        desktop_ui.setStatusBar(self.statusbar)

        self.retranslateUi(desktop_ui)
        QtCore.QMetaObject.connectSlotsByName(desktop_ui)

    def retranslateUi(self, desktop_ui):
        _translate = QtCore.QCoreApplication.translate
        desktop_ui.setWindowTitle(_translate("desktop_ui", "MainWindow"))
        self.pushButton.setText(_translate("desktop_ui", "Run"))
        self.pushButton_2.setText(_translate("desktop_ui", "Exit"))
        self.textBrowser_2.setHtml(_translate("desktop_ui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("desktop_ui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    desktop_ui = QtWidgets.QMainWindow()
    ui = Ui_desktop_ui()
    ui.setupUi(desktop_ui)
    desktop_ui.show()
    sys.exit(app.exec_())