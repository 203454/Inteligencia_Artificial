import random

def cruzax(self,listParejas):

            listNewgen = []
            if (len(listParejas) > 1):
                for i in range(len(listParejas)):
                    MascaraDeCruce = ""
                    for i in range(tambits):
                        MascaraDeCruce = MascaraDeCruce + "" + str(random.randint(0,1))
                    var = listParejas[i]
                    for x in range(len(var)):
                        #print(var[x])
                        gen1= var[0]
                        gen2 = var[1]
                    print('Gen1:',gen1)
                    print('Gen2:',gen2)
                    
                    

                    listNewgen.append(temp)
                    listNewgen.append(temp2)

                
            else:
                print('Retorno lista parejas', listParejas)
                return listParejas
            
            print('lista de nuevos G:', listNewgen)
            return listNewgen

def cruza(self,listParejas, tambits):
            listNewgen = []
            if(len(listParejas) > 1):
                child1 = ''
                child2 = ''
                for i in range(len(listParejas)):
                    MascaraDeCruce = ""
                    for i in range(tambits):
                        MascaraDeCruce = MascaraDeCruce + "" + str(random.randint(0,1))
                    var = listParejas[i]
                    for x in range(len(var)):
                        gen1= var[0]
                        gen2 = var[1]
                    print('Gen1:',gen1)
                    print('Gen2:',type(gen2) , "gen2: ",gen2)

                    for i in range(len(gen1)):
                        if MascaraDeCruce[i] == '0':
                            child1 += gen1[i]
                            child2 += gen2[i]
                        else:
                            child1 += gen2[i]
                            child2 += gen1[i]
                        listNewgen.append(child1)
                        listNewgen.append(child2)
            else:
                print('Retorno lista parejas', listParejas)
                return listParejas
            
            print('lista de nuevos G:', listNewgen)
            return listNewgen

   

listParejas = [[[1001],[1100]],[[1110],[1011]]]
tambits = 4
cruzax(listParejas,tambits)
            
