# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_isoline.ui'
#
# Created: Sat Mar 29 08:18:10 2014
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_isoline(object):
    def setupUi(self, isoline):
        isoline.setObjectName(_fromUtf8("isoline"))
        isoline.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(isoline)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(isoline)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), isoline.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), isoline.reject)
        QtCore.QMetaObject.connectSlotsByName(isoline)

    def retranslateUi(self, isoline):
        isoline.setWindowTitle(_translate("isoline", "isoline", None))

