# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Formulario(object):
    def setupUi(self, Formulario):
        if not Formulario.objectName():
            Formulario.setObjectName(u"Formulario")
        Formulario.resize(1129, 387)
        self.labelRangoMaximo = QLabel(Formulario)
        self.labelRangoMaximo.setObjectName(u"labelRangoMaximo")
        self.labelRangoMaximo.setGeometry(QRect(60, 40, 111, 31))
        font = QFont()
        font.setPointSize(10)
        self.labelRangoMaximo.setFont(font)
        self.pushButtonCalcular = QPushButton(Formulario)
        self.pushButtonCalcular.setObjectName(u"pushButtonCalcular")
        self.pushButtonCalcular.setGeometry(QRect(720, 200, 281, 51))
        self.pushButtonCalcular.setFont(font)
        self.lineEditRangoMaximo = QLineEdit(Formulario)
        self.lineEditRangoMaximo.setObjectName(u"lineEditRangoMaximo")
        self.lineEditRangoMaximo.setGeometry(QRect(60, 90, 121, 31))
        self.labelRangoMinimo = QLabel(Formulario)
        self.labelRangoMinimo.setObjectName(u"labelRangoMinimo")
        self.labelRangoMinimo.setGeometry(QRect(220, 40, 111, 31))
        self.labelRangoMinimo.setFont(font)
        self.lineEditRangoMinimo = QLineEdit(Formulario)
        self.lineEditRangoMinimo.setObjectName(u"lineEditRangoMinimo")
        self.lineEditRangoMinimo.setGeometry(QRect(220, 90, 121, 31))
        self.labelGeneraciones = QLabel(Formulario)
        self.labelGeneraciones.setObjectName(u"labelGeneraciones")
        self.labelGeneraciones.setGeometry(QRect(370, 40, 201, 31))
        self.labelGeneraciones.setFont(font)
        self.labelGeneraciones.setTextFormat(Qt.AutoText)
        self.labelGeneraciones.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.lineEditCantidadGeneraciones = QLineEdit(Formulario)
        self.lineEditCantidadGeneraciones.setObjectName(u"lineEditCantidadGeneraciones")
        self.lineEditCantidadGeneraciones.setGeometry(QRect(370, 90, 191, 31))
        self.labelIntervalo = QLabel(Formulario)
        self.labelIntervalo.setObjectName(u"labelIntervalo")
        self.labelIntervalo.setGeometry(QRect(610, 40, 111, 31))
        self.labelIntervalo.setFont(font)
        self.labelIntervalo.setLayoutDirection(Qt.LeftToRight)
        self.lineEditIntervalo = QLineEdit(Formulario)
        self.lineEditIntervalo.setObjectName(u"lineEditIntervalo")
        self.lineEditIntervalo.setGeometry(QRect(600, 90, 121, 31))
        self.lineEditPMaxima = QLineEdit(Formulario)
        self.lineEditPMaxima.setObjectName(u"lineEditPMaxima")
        self.lineEditPMaxima.setGeometry(QRect(760, 90, 141, 31))
        self.labelPoblacionMaxima = QLabel(Formulario)
        self.labelPoblacionMaxima.setObjectName(u"labelPoblacionMaxima")
        self.labelPoblacionMaxima.setGeometry(QRect(760, 40, 201, 31))
        self.labelPoblacionMaxima.setFont(font)
        self.labelPoblacionMaxima.setTextFormat(Qt.AutoText)
        self.labelPoblacionMaxima.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.labelPCruza = QLabel(Formulario)
        self.labelPCruza.setObjectName(u"labelPCruza")
        self.labelPCruza.setGeometry(QRect(60, 190, 171, 31))
        self.labelPCruza.setFont(font)
        self.labelPCruza.setTextFormat(Qt.AutoText)
        self.labelPCruza.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.lineEditPCruza = QLineEdit(Formulario)
        self.lineEditPCruza.setObjectName(u"lineEditPCruza")
        self.lineEditPCruza.setGeometry(QRect(60, 240, 161, 31))
        self.labelPoblacionInicial = QLabel(Formulario)
        self.labelPoblacionInicial.setObjectName(u"labelPoblacionInicial")
        self.labelPoblacionInicial.setGeometry(QRect(940, 40, 201, 31))
        self.labelPoblacionInicial.setFont(font)
        self.labelPoblacionInicial.setTextFormat(Qt.AutoText)
        self.labelPoblacionInicial.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.lineEditPInicial = QLineEdit(Formulario)
        self.lineEditPInicial.setObjectName(u"lineEditPInicial")
        self.lineEditPInicial.setGeometry(QRect(940, 90, 141, 31))
        self.lineEditPMutacionG = QLineEdit(Formulario)
        self.lineEditPMutacionG.setObjectName(u"lineEditPMutacionG")
        self.lineEditPMutacionG.setGeometry(QRect(250, 240, 161, 31))
        self.labelPMutacionG = QLabel(Formulario)
        self.labelPMutacionG.setObjectName(u"labelPMutacionG")
        self.labelPMutacionG.setGeometry(QRect(250, 180, 151, 41))
        self.labelPMutacionG.setFont(font)
        self.labelPMutacionG.setTextFormat(Qt.AutoText)
        self.labelPMutacionG.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.labelPMutacionG_2 = QLabel(Formulario)
        self.labelPMutacionG_2.setObjectName(u"labelPMutacionG_2")
        self.labelPMutacionG_2.setGeometry(QRect(450, 180, 151, 41))
        self.labelPMutacionG_2.setFont(font)
        self.labelPMutacionG_2.setTextFormat(Qt.AutoText)
        self.labelPMutacionG_2.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.lineEditPMutacionI = QLineEdit(Formulario)
        self.lineEditPMutacionI.setObjectName(u"lineEditPMutacionI")
        self.lineEditPMutacionI.setGeometry(QRect(450, 240, 161, 31))

        self.retranslateUi(Formulario)

        QMetaObject.connectSlotsByName(Formulario)
    # setupUi

    def retranslateUi(self, Formulario):
        Formulario.setWindowTitle(QCoreApplication.translate("Formulario", u"Formulario", None))
        self.labelRangoMaximo.setText(QCoreApplication.translate("Formulario", u"Rango Maximo", None))
        self.pushButtonCalcular.setText(QCoreApplication.translate("Formulario", u"Calcular", None))
        self.labelRangoMinimo.setText(QCoreApplication.translate("Formulario", u"Rango Minimo", None))
        self.labelGeneraciones.setText(QCoreApplication.translate("Formulario", u"Cantidad de Generaciones", None))
        self.labelIntervalo.setText(QCoreApplication.translate("Formulario", u"Intervalo", None))
        self.lineEditPMaxima.setText("")
        self.labelPoblacionMaxima.setText(QCoreApplication.translate("Formulario", u"Poblacion Maxima", None))
        self.labelPCruza.setText(QCoreApplication.translate("Formulario", u"Probabilidad de cruza", None))
        self.lineEditPCruza.setText("")
        self.labelPoblacionInicial.setText(QCoreApplication.translate("Formulario", u"Poblacion Inicial", None))
        self.lineEditPInicial.setText("")
        self.lineEditPMutacionG.setText("")
        self.labelPMutacionG.setText(QCoreApplication.translate("Formulario", u"Probabilidad de MG", None))
        self.labelPMutacionG_2.setText(QCoreApplication.translate("Formulario", u"Probabilidad de MI", None))
        self.lineEditPMutacionI.setText("")
    # retranslateUi

