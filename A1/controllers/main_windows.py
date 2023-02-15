import random
import math
from itertools import combinations
from views.main_window import Formulario
from PySide2.QtWidgets import QWidget, QFileDialog, QTableWidget, QTableWidgetItem
import matplotlib.pyplot as plt
import numpy
import os
from shutil import rmtree

class AlgorithmsGenetic():
    
    def __init__(self,generaciones,rangoMaxima,rangoMinima,intervalo,poblacionMaxima, pCruza, poblacionInicial,pmi,pmg):
        self.generaciones = generaciones
        self.rangoMaxima = rangoMaxima
        self.rangoMinima = rangoMinima
        self.intervalo = intervalo
        self.poblacionMaxima = poblacionMaxima
        self.poblacionInicial = poblacionInicial
        self.pmi = pmi
        self.pmg = pmg
        
    def generaciones(self):

        pass

    def generarPoblacion(self, tambits):
        bitaje = 1
        cadena = ""
        for i in range(int(tambits)):
            for x in range(bitaje):
                cadena = cadena + "" + str(random.randint(0,1))
            return cadena
        pass



def dataFrame():

    generaciones= lineEditCantidadGeneraciones.setText(valueGeneraciones)
    rangoMaxima = lineEditRangoMaximo.setText(defaultRangoMax)
    rangoMinima = lineEditRangoMinimo.setText(defaultRangoMin)
    intervalo = lineEditIntervalo.setText(defaultIntervalo)
    poblacionMaxima = lineEditPMaxima.setText(defaulPobMaxima)
    pCruza = lineEditPCruza.setText(defaultPCruza)
    poblacionInicial = lineEditPInicial.setText(defaulPinicial)
    pmi = lineEditPMutacionI.setText(defaultPMI)
    pmg = lineEditPMutacionG.setText(defaultPMG)

    AlgorithmsGenetic(generaciones, rangoMaxima, rangoMinima, intervalo, poblacionMaxima, pobliacionMinima, pCruza, poblacionInicial, pmi,pmg)