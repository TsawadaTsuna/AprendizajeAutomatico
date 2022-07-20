from cProfile import label
from collections import defaultdict
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score,precision_recall_fscore_support
import matplotlib.pyplot as plt
import numpy as np

def calcularKmeans(archivo, clusters):
    #Archivo=open('Datos1.csv','r')
    try:
        Archivo = open(archivo,'r')
        print(f'K means \nCon el archivo {archivo} \nk={clusters} ')
    except:
        print("Archivo invalido")
    else:
        datos = []
        cont = 1
        Clases = []

        with Archivo:
            for x in Archivo.readlines():#leer los datos
                if len(x)>2:
                    if cont==1:
                        Atributos=x.replace('\n','').split(',')
                        cont+=1
                    else:
                        atrib=x.replace('\n','').split(',')
                        Clases.append(atrib[len(atrib)-1])
                        datos.append(list(map(float,atrib[:-1])))

        kmeans = KMeans(n_clusters=clusters, max_iter=500).fit(datos)#500 es default
        #print(Clases)
        prediccion=kmeans.labels_
        #print(kmeans.labels_)

        #print(kmeans.cluster_centers_)
        #todo precision y recall
        #clase labels
        diccionario = defaultdict(int)
        for x in Clases:
            diccionario[x]=[0]*clusters
        for x, y in zip(Clases, prediccion):
            #diccionario[str(y) + x] += 1
            diccionario[x][y]+=1
            #print(x,y)
        
        
        if clusters==2:
            #print(diccionario)    
            #print(Clases)
            for i in diccionario:
                #print(i)        
                mayor=-1  
                tmp=-1
                for j in range(len(diccionario[i])):
                    if mayor<diccionario[i][j]:
                        mayor=diccionario[i][j]
                        tmp=j
                #print(tmp)
                Clases=cambairDatos(Clases,i,tmp)
            
            #print(prediccion)
            #print(Clases)
        elif clusters==3:
            #k3Todas
            print(diccionario)    
            print(Clases)
            print(prediccion)
            Clases=cambairDatos(Clases,"Profundo",0)
            Clases=cambairDatos(Clases,"Superficial",1)
            Clases=cambairDatos(Clases,"Logro",2)
            print(Clases)
            #k3Metricas

            #k3pregutnas



        # print(Clases)
        metricas=precision_recall_fscore_support(Clases,prediccion)
        printMetricas(metricas,silhouette_score(datos,kmeans.labels_))


def printMetricas(metricas,silhoute):
    print("---------------------------------------------------------------------------------------------")
    print(f"Silhouete: {silhoute}")#generar silhoutte
    for i in range(len(metricas[0])):
        print(f'Cluster:{i}\tPrecision:{metricas[0][i]}\tRecall:{metricas[1][i]}\tF-Score:{metricas[2][i]}')
        
    print("---------------------------------------------------------------------------------------------")
def cambairDatos(arreglo,datoOriginal, datoCambiar):
    for i in range(len(arreglo)):
        if arreglo[i]==datoOriginal:
            arreglo[i]=datoCambiar
    return arreglo

#calcularKmeans('K2Todas.csv',2)
# calcularKmeans('K2Metricas.csv',2)
# calcularKmeans('K2Preguntas.csv',2)

calcularKmeans('K3Todas.csv',3)
# calcularKmeans('K3Metricas.csv',3)
# calcularKmeans('K3Preguntas.csv',3)