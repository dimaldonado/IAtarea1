from queue import PriorityQueue
import random
class Grafo:
    def __init__(self):
        self.vertices = dict()
        self.aristas = dict()
        self.inicio = None
        self.meta = None

    def agregar_vertice(self, vertice, valor_heuristica):
    
        self.vertices[vertice] = valor_heuristica

    def agregar_arista(self, vertice1, vertice2, costo):
        if(vertice1 not in self.aristas):
            self.aristas[vertice1] = []
            self.aristas[vertice1].append(tuple([vertice2,costo]))
        else:
            self.aristas[vertice1].append(tuple([vertice2,costo]))
    
    
    def buqueda_profundidad(self):
        print("---Busqueda en profundida---")
        expansiones_por_nodo = self.vertices.copy()
        expansiones_por_nodo = dict.fromkeys(expansiones_por_nodo,0)
        costo_total=0
        camino = []
        expandidos = [(self.inicio,0)]
        numero_expanciones = 0
        primera_it = True
        index = 0

        while len(expandidos)!=0:
            if not primera_it:
                while(expandidos[index] not in self.aristas[nodo_actual[0]]):#mientras el nodo seleccionado del expandidos no sea hijo del nodo anterior(padre)
                    index = random.randint(0, len(expandidos)-1)#se selecciona un indice al azar
            nodo_actual = expandidos.pop(index)
            
            if nodo_actual[0] == self.meta:
                camino.append(nodo_actual)
                for nodo in camino:
                    costo_total += nodo[1]
                print("Camino encontrado: ",end='')
                for nodo in camino:
                    print(nodo[0]+" ",end='')
                print("")
                print("Costo total: "+str(costo_total))
                print("Expansiones totales: "+str(numero_expanciones))
                print("Expansiones por nodo:")
                for x in expansiones_por_nodo:
                    print(x+": "+str(expansiones_por_nodo[x]))
                break
            
            if nodo_actual[0] not in camino:#si el nodo no esta en el camino lo añadimos
                camino.append(nodo_actual)
                numero_expanciones+=1
                
                if nodo_actual[0] not in self.aristas:#pero si nodo no se encuentra en la lista de adyacencia, es decir, no tiene hijos
                    camino.pop()#se retira
                else:
                    for nodo in self.aristas[nodo_actual[0]]:#si esta en la lista de adyacencia, es decir, tiene hijos
                        expansiones_por_nodo[nodo_actual[0]] += 1
                        expandidos.append(nodo)#se agrega al expandidos
            primera_it = False

              
                


    def busqueda_greedy(self):
        print("---Busqueda Greedy---")
        expansiones_por_nodo = self.vertices.copy()
        expansiones_por_nodo = dict.fromkeys(expansiones_por_nodo,0)
        nodo_actual = self.inicio
        nodos_no_visitados = list(self.vertices)#En un inicio catalogamos todos los nodos como no visitados
        nodos_visitados = []
        costo_total = 0
        nodos_no_visitados.remove(nodo_actual)
        nodos_visitados.append(nodo_actual)#Partimos con el nodo de inicio como visitado
        
        
        while nodo_actual!=self.meta:#mientras no se llegue a la meta
            prox_nodo = self.inicio     
            for i in range(0,len(self.aristas[nodo_actual])):#revisamos todos los nodos vecinos
                expansiones_por_nodo[nodo_actual] += 1
                if self.vertices[self.aristas[nodo_actual][i][0]]<=self.vertices[prox_nodo[0]] and prox_nodo in self.aristas:#Buscamos entre los nodos "hijos" el que tenga la menor heuristica y ademas que tenga salida
                    prox_nodo = self.aristas[nodo_actual][i]
                    costo_total +=  self.aristas[nodo_actual][i][1]
            nodo_actual = prox_nodo[0]#una vez encontrado lo seleccionamos
            nodos_no_visitados.remove(nodo_actual)
            nodos_visitados.append(nodo_actual)#Lo agregamos como visitado
            prox_nodo = tuple(['ñ',99999999])#reiniciamos el valor de prox nodo
            
        print("Camino encontrado: ",end="")
        for i in nodos_visitados:
            print(i+" ",end="")
        print("")
        print("Costo total: "+str(costo_total))
        print("Expansiones totales:"+str(sum(expansiones_por_nodo.values())))
        print("Expansiones por nodo:")
        for x in expansiones_por_nodo:
            print(x+": "+str(expansiones_por_nodo[x]))
              
    

    def a_estrella(self):
        print("---Busqueda A*---")
        expansiones_por_nodo = self.vertices.copy()
        expansiones_por_nodo = dict.fromkeys(expansiones_por_nodo,0)
        expandidos = [(0, self.inicio)]  # Aqui se almacenaran los nodos expandidos
        costo_n = {self.inicio: 0}  #Aqui se almacenara el costo para llegar desde el nodo inicial hacia cada determinado nodo
        funcion_n = {self.inicio: self.vertices[self.inicio]}  # Aqui se alacenara el f(n)=c(n)+h(n) de cada nodo
        padre = {}  #Aqui se almacenaran el nodo "padre" de cada nodo
        
        while len(expandidos)>0:

            expandidos.sort()#Se ordena en funcion del f(n)
            aux , nodo_actual = expandidos.pop(0)  #Extraemos el nodo con el menor f(n)
            if nodo_actual == self.meta:  # Si es la meta, se construye el camino a partir de los padres
                camino = [self.meta]
                while nodo_actual in padre:
                    nodo_actual = padre[nodo_actual]
                    camino.append(nodo_actual)
                camino.reverse()
                print("Camino encontrado:  ",end="")
                for nodo in camino:
                    print(nodo,end=" ")
                print("")
                print("Costo total: "+str(costo_n[self.meta]))
                print("Expansiones totales:"+str(sum(expansiones_por_nodo.values())))
                print("Expansiones por nodo:")
                for x in expansiones_por_nodo:
                    print(x+": "+str(expansiones_por_nodo[x]))
                break

            for child in self.aristas[nodo_actual]:#Para cada nodo hijo
                nuevo_costo_child = costo_n[nodo_actual] + child[1]  #Calculamos su costo acumulado

                if child[0] not in costo_n or nuevo_costo_child < costo_n[child[0]]:  # Si su costo(acumulado) no esta registrado o ya hay un costo registrado pero es mayor
                    expansiones_por_nodo[nodo_actual] += 1
                    costo_n[child[0]] = nuevo_costo_child#Se almacena el nuevo costo calculado
                    funcion_n[child[0]] = nuevo_costo_child + self.vertices[child[0]]  #Se calcula y almacena el f(n) correspondiente al nodo
                    expandidos.append((funcion_n[child[0]], child[0]))  #se agrega el nodo junto a su f(n) a expandidos
                    padre[child[0]] = nodo_actual  # Actualizar el nodo padre del hijo

        
    def CostoUniforme(self):
        print("---Busqueda costo uniforme---")
        expansiones_por_nodo = self.vertices.copy()
        expansiones_por_nodo = dict.fromkeys(expansiones_por_nodo,0)
        nodo_actual = self.inicio
        nodo_ant = self.inicio
        nodo = tuple([self.inicio,0])
        visitado = []
        camino  = []
        suma_costos=0
     
        
        while nodo_actual!=self.meta:    
            camino.append(nodo)
 
            for child in self.aristas[nodo_actual]:
                
                if not any(child[0] in tupla for tupla in visitado) and not any(child[0] in tupla for tupla in camino):#Si el nodo hijo no esta en el camino y no fue visitado
                    expansiones_por_nodo[nodo_actual] += 1
                    visitado.append((child[0],child[1]+suma_costos))#se agrega a visitados
                
                elif any(child[0] in tupla for tupla in visitado):#si esta en visitados

                    pos = next((i for i,tupla in enumerate(visitado) if child[0] in tupla),-1)
                    expansiones_por_nodo[nodo_actual] += 1
                    if suma_costos + child[1] < visitado[pos][1]: #si el costo acumulado ya registrado es mayor, se quita y se pone el nuevo
                        visitado.pop(pos)
                        visitado.append((child[0],child[1]+suma_costos))

            visitado.sort(key=lambda x: x[1])#se ordena
            for visitados in visitado:
                if any(visitados[0] in tupla for tupla in self.aristas[nodo_actual]):#de esta forma obtenemos nodo con el menor coste acumulado y comprobamos que sea hijo
                    nodo_ant = nodo_actual
                    nodo = visitados
                    nodo_actual = visitados[0]
                    suma_costos = visitados[1]
                    visitado.remove(visitados)#lo quitamos de visitado para luego agregarlo al camino
                    break
        
        
        
        print("Camino encontrado: ",end="")
        for x in camino:
            print(x[0]+" ",end="")    
        print("Costo total: "+str(suma_costos))
        print("Numero de expansiones: "+str(sum(expansiones_por_nodo.values())))
        print("Expansiones por nodo:")
        for x in expansiones_por_nodo:
            print(x+": "+str(expansiones_por_nodo[x]))
                
            
       

    def cargar_desde_archivo(self, archivo):
        with open(archivo, 'r') as file:
            for linea in file:
                palabras = linea.split()
                if palabras[0] == 'Init:':
                    self.inicio = palabras[1]
                elif palabras[0] == 'Goal:':
                    self.meta = palabras[1]
                elif ',' in linea:
                    palabras = linea.split(',')
                    vertice1 = palabras[0].strip()
                    vertice2 = palabras[1].strip()
                    costo = int(palabras[2].strip())  
                    self.agregar_arista(vertice1, vertice2, costo)
                elif ',' not in linea:
                    vertice = palabras[0]
                    valor_heuristica = int(palabras[1])
                    self.agregar_vertice(vertice, valor_heuristica)

                
                

            
                

if __name__ == '__main__':
    grafo = Grafo()
    grafo.cargar_desde_archivo('archivo.txt')
    entrada = input("Ingrese la opcion:")
    if entrada == "g":
        grafo.busqueda_greedy()
    if entrada == "c":
        grafo.CostoUniforme()
    if entrada == "p":
        grafo.buqueda_profundidad()
    if entrada == "a":
        grafo.a_estrella()
   