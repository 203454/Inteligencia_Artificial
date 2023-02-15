import random
import math
from itertools import combinations
from views.main_window import Formulario
#from views.alerta import DialogAlerta
from PySide2.QtWidgets import QWidget, QFileDialog, QTableWidget, QTableWidgetItem
import matplotlib.pyplot as plt
import numpy
import os
from shutil import rmtree

class MainFormWindow (QWidget,Formulario):

        def __init__(self):
        
            super().__init__()
            self.ui = Formulario()
            #self.ui2 =DialogAlerta()
            self.setupUi(self)
            valueGeneraciones = "2"
            defaultRangoMax = "20"
            defaultRangoMin = "10"
            defaultIntervalo = "1"
            defaulPobMaxima = "10"
            defaultPCruza = ".6"
            defaulPinicial = "4"
            defaultPMI = "0.25"
            defaultPMG = "0.50"

            generaciones= self.lineEditCantidadGeneraciones.setText(valueGeneraciones)
            rangoMaxima = self.lineEditRangoMaximo.setText(defaultRangoMax)
            rangoMinima = self.lineEditRangoMinimo.setText(defaultRangoMin)
            intervalo = self.lineEditIntervalo.setText(defaultIntervalo)
            poblacionMaxima = self.lineEditPMaxima.setText(defaulPobMaxima)
            pCruza = self.lineEditPCruza.setText(defaultPCruza)
            poblacionInicial = self.lineEditPInicial.setText(defaulPinicial)
            pmi = self.lineEditPMutacionI.setText(defaultPMI)
            pmg = self.lineEditPMutacionG.setText(defaultPMG)



            self.pushButtonCalcular.clicked.connect(self.inicial)


        # def alerta(self):
        #     dialog=DialogAlerta()
        #     dialog


        def inicial(self):
            
            generaciones = 0
            rangoMaxima = 0
            rangoMinimo = 0

            generaciones = self.generaciones()
            rangoMaxima, rangoMinimo =self.rangos()
            print(rangoMaxima,rangoMinimo)
            self.generarDatos(generaciones, rangoMaxima, rangoMinimo)

        def generaciones(self):

            generaciones= int(self.lineEditCantidadGeneraciones.text())
            return generaciones


        #Generar Poblacion

        def generarPoblacion(self,tambits):
            bitaje = 1
            cadena = ""
            for i in range(int(tambits)):
                for x in range(bitaje):
                    cadena = cadena + "" + str(random.randint(0,1))
            return cadena

        def rangos(self):

            #listMejores = []
            #Dato generado por el usuario
            rangoMaxima= int(self.lineEditRangoMaximo.text())
            #print("rango maximo:",rangoMaxima)
            #Dato generado por el usuario
            rangoMinima = int(self.lineEditRangoMinimo.text())
            #print("rango minimo:", rangoMinima)
            # rangoMinima= int(input())
            
            #listMejores = self.genIntervalo(rangoMaxima, rangoMinima,generaciones,i)

            return rangoMaxima, rangoMinima

        def generarDatos(self, generaciones, rangoMaxima, rangoMinima):
            #Dato generado por el usuario

            listElementosBin = []
            listElementosDec = []
            listAptitud = []
            listFx = []
            listFx2 = []
            listParejas = [] 
            listCruza = []
            listPc = []
            listMutados = []
            listElementosDecMut = []
            listAptitudMut = []
            listNuevaPBin =[]
            listNuevaPAptitud = []
            listNuevaFx = []
            listNuevaPAptitud1 = []
            listNuevaFx1 = []
            listMutadoyConc = []
            listPoda = []
            listMejores = []
            mejoresBinarios = []
            mejoresDecimal = []
            mejoresX = []
            mejoresFx = []
            aux = 0
            index = 0

            print("Cantidad de Generaciones:", generaciones)

            print('Rango Maximo:', rangoMaxima)

            print("Rango Minimo:", rangoMinima)

            intervalo = float(self.lineEditIntervalo.text())
            print("intervalo:", intervalo)

            rango = (rangoMaxima-rangoMinima)# r = 20 -10 = 10
            puntos = int((rango/intervalo))+1 # 11
            print("Puntos:", puntos) #11

            valbits = (bin(puntos)) 
            print('Valbits:',valbits)
            bits= valbits.removeprefix("0b")

            tambits = len(bits)
            print("Tam bits:", tambits)

            poblacionMaxima = int(self.lineEditPMaxima.text())
            print("poblacion maxima:", poblacionMaxima)

            poblacionInicial = int(self.lineEditPInicial.text())
            print("poblacion inicial", poblacionInicial)

            print()
            print('-------------- Generacion Inicial -----------------')
            print()
            for i in range(poblacionInicial):
                cadenaBin = self.generarPoblacion(tambits)
                listElementosBin.append(cadenaBin)

            for x in range(len(listElementosBin)):
                cadenaDec=self.convertirBinarios(listElementosBin[x])
                listElementosDec.append(cadenaDec)

            print("lista Binaria PobInicial:", listElementosBin)
            print("lista Decimal Individuo:", listElementosDec)

            listAptitud=self.fitness(intervalo,rangoMinima, listElementosDec)

            print("list valX PobInicial:", listAptitud)

            for z in range(len(listAptitud)):
                cadenaFx = self.fx(listAptitud[z])
                listFx.append(cadenaFx)
            print("lista Aptitud:", listFx)
            print()


            #qui generar el for para las generaciones
            
            for i in range(generaciones):
                index = i
                print("----------- Generacion:", i,"------------------")
                print('----------- Probabilidad de cruza ------------------------')
                listPc = self.probabilidadC(listElementosBin)

                print('-------------- Parejas creadas ----------------------------')

                listParejas = self.posiblesParejasX(listPc)
                print("Lista de parejas: ",listParejas)
                print('------------------- Cruza -------------------------------')

                # listCruza =self.cruza(listParejas)
                listCruza = self.cruzax(listParejas,tambits)

                print('------------------- Mutacion -----------------------------')

                listMutados =self.mutacion(listCruza)#[0001,0000]
                #listMutadoyConc =self.mutacion(listCruza)#[0001,0000]
                print('Binarios Mutados y no mutados:',listMutados)
                listMutadoyConc= list(numpy.concatenate((listMutados), axis=None))
                print('Binarios Mutados y no mutados unidos:', listMutadoyConc)
                # Se manda a convertir la lista de los mutados y no mutados a decimal reusando la funcion de conversion a decimales
                print("---------- Valores de la generacion CyM:", i,"--------------------")
                for y in range(len(listMutadoyConc)):
                    cadenaDec=self.convertirBinarios(listMutadoyConc[y])
                    listElementosDecMut.append(cadenaDec)
                print("lista Decimal Individuos Mutados:", listElementosDecMut)

                #se le calcula la aptitud a la generacion de los mutados
                listAptitudMut=self.fitness(intervalo,rangoMinima, listElementosDecMut)
                print('valor de "X" mutados:', listAptitudMut)

                for m in range(len(listAptitudMut)):
                    cadenaFx = self.fx(listAptitudMut[m])
                    listFx2.append(cadenaFx)
                print("lista Aptitud Mutados:", listFx2)
                print('-------------------------- Nueva generacion (juntando la generacion) ----------------------------')

                # listNuevaPBin=self.nuevaPoblacionBin(listMutados,listElementosBin)
                #print('La nueva poblacion binaria es:', listNuevaPBin)
                print('La nueva poblacion binaria es:', listMutadoyConc)

                # listNuevaPDec=self.nuevaPoblacionDec(listElementosDecMut,listElementosDec)
                # print('Valores de los individuos de la nueva poblacion:', listNuevaPDec)
                print('La nueva poblacion decimal es:', listElementosDecMut)

                # listNuevaPAptitud=self.nuevaPoblacionAptitud(listAptitud, listAptitudMut)
                # print('El valor "X" de los nuevos individuos es:', listNuevaPAptitud)
                print('La nueva X es:', listAptitudMut)

                # listNuevaFx=self.nuevaPoblacionFx(listFx,listFx2)
                # print('La nueva aptitud de los nuevos individuos:', listNuevaFx)
                print('La nueva aptitud de los nuevos individuos:', listFx2)
                print('index de graficas:', index)
                #self.graficasXgeneracion(listNuevaPAptitud,listNuevaFx,index)
                self.graficasXgeneracion(listAptitudMut,listFx2,index)

                
                #listNuevaPAptitud1 = sorted(set(listNuevaPAptitud))
                #listNuevaFx1 = sorted(set(listNuevaFx))

                #Graficas
                

                try:
                    listMejores = self.mejores(listMutadoyConc,listElementosDecMut,listAptitudMut,listFx2,generaciones)
                    
                    mejoresBinarios.append(listMejores[0])
                    mejoresDecimal.append(listMejores[1])
                    mejoresX.append(listMejores[2])
                    mejoresFx.append(listMejores[3])

                    print("Lista mejores Binarios",mejoresBinarios)
                    print("Lista mejores Decimales",mejoresDecimal)
                    print("Lista mejores X",mejoresX)
                    print("Lista mejores Fx",mejoresFx)

                except:
                    pass
                listPoda=self.podaAptitud(listMutadoyConc,listElementosDecMut,listAptitudMut,listFx2, poblacionMaxima,rango)
                listElementosBin = listPoda[0]
                listElementosDec = listPoda[1]
                listAptitud = listPoda[2]
                listFx = listPoda[3]
                
                listElementosDecMut.clear()
                listAptitudMut.clear()
                listFx2.clear()
                print('--------------------------------------------------------------')
                print('Despues de la poda los datos binarios son:', listElementosBin)
                print('Despues de la poda los datos decimales de los individuos son:', listElementosDec)
                print('Despues de la poda los datos de x son:', listAptitud)
                print('Despues de la poda los datos de Fx son:', listFx)

            #Salio del for
            
            if i == generaciones -1:
                try:
                    x2 = list(numpy.concatenate(sorted((mejoresX)), axis=None))
                    fx2 = list(numpy.concatenate(sorted((mejoresFx)), axis=None))
                    print('Los mejores x son:', x2)
                    print('Los mejores fx son:', fx2)
                    
                    self.graficasXiteracion(x2,fx2)
                except:
                    pass

            #print('listPoda:',listPoda )
            #cruza(listElementosBin, listPc)

        def convertirBinarios(self,numBinario):
                n=int(numBinario)
                s=0
                i=0
                while(n >=1):
                    d=n%10
                    n=int(n/10)
                    s=s+d*pow(2,i)
                    i=i+1
                return s

        def fitness(self,intervalo,rangoMinima, listElementosDec):
            listX = [] #1,2,3
            x = 0
            for i in range(len(listElementosDec)):
                x=rangoMinima + listElementosDec[i] * intervalo
                listX.append(x)
            return listX

        #Formula matematica
        def fx(self,z):
            x = float(z)
            resultado = 0.0
            if x > 0:
                try:
                    resultado = float("{:.4f}".format(math.sin(math.radians(x))*math.sqrt(2*pow(x,2)-x-2)))
                except:
                    pass
            else:
                print("valor descartado")
            return resultado

        def probabilidadC(self, listElementosBin):

            listPcruzaR = []
            listElementosxCruzar = []

            pCruza = float(self.lineEditPCruza.text())
            print('probabilidad de cruza',pCruza)
            
            for i in range(len(listElementosBin)):
                
                pCruzaRandom = random.uniform(0.1,1.0)
                a = float("{:.4f}".format(pCruzaRandom))
                listPcruzaR.append(a)

            for x in range(len(listElementosBin)):
                print('Individuo #', x, ':', listElementosBin[x])
                print('Valor Random para la cruza:', listPcruzaR[x])
                if listPcruzaR[x] <= pCruza:
                    listElementosxCruzar.append(listElementosBin[x])
                    print('El mono puede cruzar')
                else:
                    print('El mono no cruza')

            print('elemntos x cruzar:', listElementosxCruzar)

            return listElementosxCruzar


        def posibleParejas(self, listPc):
            listCombinaciones = []
            # print("ESTA ES LA LISTA PARA CREAR LAS PAREJAS: ", listPc)
            if (len(listPc)>1):
                temp = combinations(listPc,2)
                for i in list(temp):
                    listCombinaciones.append(i)
                print('combinaciones', listCombinaciones)
            else:
                print("retorno listPc:", listPc)
                return listPc
            # print(listCombinaciones)
            return listCombinaciones


    #Nuevo metodo de seleccion de padres
        def posiblesParejasX(self, listPc):
            listCombinaciones = []
            padres = []
            for i in range(len(listPc)):
                num_individuals = random.randint(2, len(listPc))
                candidatos = random.sample(listPc, num_individuals)
                ganador = max(candidatos)
                padres.append(ganador)
                print('CANDIDATOS: ',candidatos)
            temp = combinations(padres,2)
            for i in list(temp):
                listCombinaciones.append(i)
            print('combinaciones', listCombinaciones)
            print("NUEVOS PADRES: ",padres) 
            return listCombinaciones

        def cruza(self,listParejas):

            listNewgen = []
            if (len(listParejas) > 1):
                for i in range(len(listParejas)):
                    var = listParejas[i]
                    for x in range(len(var)):
                        #print(var[x])
                        gen1= var[0]
                        gen2 = var[1]
                    print('Gen1:',gen1)
                    print('Gen2:',gen2)
                    
                    div1 = gen1[:len(gen1)//2]
                    div2 = gen2[len(gen2)//2:] 

                    div3 = gen2[:len(gen2)//2]
                    div4 = gen1[len(gen1)//2:]

                    temp = div1 + div2
                    temp2 = div3 + div4
                    listNewgen.append(temp)
                    listNewgen.append(temp2)
            else:
                print('Retorno lista parejas', listParejas)
                return listParejas

            print('lista de nuevos G:', listNewgen)
            return listNewgen


        #Nuevo metodo de cruza    
        def cruzax(self,listParejas, tambits):
            listNewgen = []
            if(len(listParejas) > 1):
                for i in range(len(listParejas)):
                    MascaraDeCruce = ''
                    child1 = ''
                    child2 = ''
                    for y in range(tambits):
                        MascaraDeCruce = MascaraDeCruce + "" + str(random.randint(0,1))
                    print(MascaraDeCruce, "en iteracion", [i])
                    var = listParejas[i]
                    for x in range(len(var)):
                        gen1= var[0]
                        gen2 = var[1]
                    print('Gen1:',gen1)
                    print('Gen2:',gen2)

                    for j in range(len(gen1)):
                        if MascaraDeCruce[j] == '0':
                            child1 = child1 + gen1[j]
                            child2 = child2 + gen2[j]
                        else:
                            child1 = child1 + gen2[j]
                            child2 = child2 + gen1[j]

                    print("hijo 1:",child1)
                    print("hijo 2:",child2)
                    listNewgen.append(child1)
                    listNewgen.append(child2)
                        
            else:
                print('Retorno lista parejas', listParejas)
                return listParejas
            
            print('lista de nuevos G:', listNewgen)
            return listNewgen


        def mutacion(self, listCruza):

            listNewInd = []
            listNewBit = []
            listNewBit2 = []
            listAnalizador= []
            listNoCruza= []
            listNew = []
            
            pmi = float(self.lineEditPMutacionI.text())
            print("probabilidad de mutación del inidividuo:", pmi)
            pmg = float(self.lineEditPMutacionG.text())
            print("probabilidad de mutación del gen:", pmg)

            for i in range(len(listCruza)):
                var = listCruza[i]
                print("Individuo seleccionado: ",listCruza[i])
                pmir=float("{:.4f}".format(random.uniform(0.0,1.0)))
                print("Su probabilidad es: ",pmir)
                if pmir < pmi:
                    listNewInd.append(listCruza[i])
                print('Mutan:',listNewInd)
                if pmir > pmi:
                    listNoCruza.append([listCruza[i]])
                print("No mutan: ",listNoCruza)
            for i in range(len(listNewInd)):
                    var =listNewInd[i]
                    for y in range(len(var)):
                        listNew.append(var[y])
                    for y in range(len(var)):
                        listAnalizador.append(var[y])
                        pmgr= random.randint(0,len(var)-1)
                        listNew[pmgr]
                        lis1=var[y]
                        lis2=listNew[pmgr]
                        listNewBit.append(lis2)
                    bit2 = ''.join(listNewBit)
                    listNewBit2.append(bit2)
                    listAnalizador.clear()
                    listNewBit.clear()
                    listNew.clear()
            return [listNewBit2,listNoCruza]

                        
        
        def nuevaPoblacionBin(self,listMutadoyConc,listElementosBin):
            listNuevaP = []
            #se une la lista de elementos binarios originales + lista de binarios mutados
            listNuevaP = listElementosBin + listMutadoyConc
            return listNuevaP
        
        def nuevaPoblacionDec(self,listElementosDecMut,listElementosDec):
            listNuevaP = []
            #se une la lista de elementos decimales originales + lista de decimales mutados
            listNuevaP = listElementosDec + listElementosDecMut
            return listNuevaP
        
        def nuevaPoblacionAptitud(self,listAptitud, listAptitudMut):
            listNuevaP = []
            #se une la lista de elementos de aptitud originales + lista de aptitud mutados
            listNuevaP = listAptitud + listAptitudMut
            return listNuevaP

        def nuevaPoblacionFx(self,listFx,listFx2):
            listNuevaP = []
            #se une la lista de elementos de Fx originales + lista de Fx mutados
            listNuevaP = listFx + listFx2
            return listNuevaP

        def podaAptitud(self,listNuevaPBin,listNuevaPDec,listNuevaPAptitud,listNuevaFx, poblacionMaxima, rango):
            
            ordenadosBin = []
            ordenadosPDec = []
            ordenadosPAptitud = []
            ordenadosFx = []
            ordenadosBin = sorted(set(listNuevaPBin))
            ordenadosPDec = sorted(set(listNuevaPDec))
            ordenadosPAptitud = sorted(set(listNuevaPAptitud))
            ordenadosFx = sorted(set(listNuevaFx))

            print('ordenadosBin sin eliminar:', ordenadosBin)
            print('ordenadosPDec sin eliminar:', ordenadosPDec)
            print('ordenadosPAptitud sin eliminar:', ordenadosPAptitud)
            print('ordenadosFx sin eliminar:', ordenadosFx)
            print('-------------------------------------------------')
            tam = len(ordenadosFx)
            try:
                if tam > poblacionMaxima:
                    print('Eliminacion por Aptitud')
                    resta = tam - poblacionMaxima
                    print('Resta:', resta)

                    for i in range(resta):
                        #print('i',i)
                        numeroDato = random.randint(0,resta-1)
                        print('elemento eliminado:',ordenadosBin.pop(numeroDato)) 
                        print('elemento eliminado', ordenadosPDec.pop(numeroDato)) 
                        print('elemento eliminado', ordenadosPAptitud.pop(numeroDato)) 
                        print('elemento eliminado', ordenadosFx.pop(numeroDato))

                        # 0,0,0

                    print('ordenadosBin resultantes:', ordenadosBin)
                    print('ordenadosPIndividuo resultantes:', ordenadosPDec)
                    print('ordenadosPAptitud resultantes:', ordenadosPAptitud)
                    print('ordenadosFx resultantes:', ordenadosFx)
            except:
                #print('No existen elementos para hacer poda por aptitud') 
                pass

            return [ordenadosBin,ordenadosPDec,ordenadosPAptitud,ordenadosFx]   
        
        def mejores(self,listNuevaPBin,listNuevaPDec,listNuevaPAptitud,listNuevaFx,generaciones):
            listPbinMayor = []
            listPDecMayor = []
            listPAptitudMayor = []
            listPFxMayor = []
            # 1,2,4,5
            #5,4,2,1
            listNuevaPBin.sort(reverse = True)
            listNuevaPDec.sort(reverse = True)
            listNuevaPAptitud.sort(reverse = True)
            listNuevaFx.sort(reverse = True)
            listPbinMayor.append(listNuevaPBin[0])
            listPDecMayor.append(listNuevaPDec[0])
            listPAptitudMayor.append(listNuevaPAptitud[0])
            listPFxMayor.append(listNuevaFx[0])

            return [listPbinMayor,listPDecMayor,listPAptitudMayor, listPFxMayor]

        def graficasXiteracion(self,x, fx):
        
            try:
                rmtree("assets\GraficaHistorial\img")
            except:
                pass
            plt.plot(x,fx, label="Mejores individuo", color="green", linestyle="-",marker ='.')
            plt.legend()
            os.makedirs("assets\GraficaHistorial\img", exist_ok=True)
            plt.savefig("assets\GraficaHistorial\img\GraficaGeneral.png")
            plt.close()

        def graficasXgeneracion(self, listNuevaPAptitud,listNuevaFx,index):
            print('Entro a graficas x generacion')
            plt.title("Generacion: "+str(index))
            plt.plot(listNuevaPAptitud,listNuevaFx, label="Generacion "+str(index), color="blue", linestyle="none",marker ='.')
            plt.legend()
            os.makedirs("assets\GraficasIndividuales\img", exist_ok=True)
            plt.savefig("assets\GraficasIndividuales\img\GraficaIndividual "+str(index)+".png")
            plt.close()