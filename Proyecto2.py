from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score,precision_recall_fscore_support
import matplotlib.pyplot as plt
import numpy as np


def calcularKmeans(archivo, clusters):
    #Archivo=open('Datos1.csv','r')
    try:
        Archivo = open(archivo,'r')
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
        print(Clases)
        print(kmeans.labels_)

        
        print(kmeans.cluster_centers_)
        print("Silhouete: ",silhouette_score(datos,kmeans.labels_))#generar silhoutte

        #todo precision y recall

        #Ejemplo=kmeans.predict([[5, 2], [4, 0], [4, 1]])
        #Ejemplo=kmeans.predict([[64,89], [50,90]])
        #print(Ejemplo)
        print("-------------------------------")


calcularKmeans('K2Todas.csv',2)
# calcularKmeans('K2Metricas.csv',2)
# calcularKmeans('K2Preguntas.csv',2)

# calcularKmeans('K3Todas.csv',3)
# calcularKmeans('K3Metricas.csv',3)
# calcularKmeans('K3Preguntas.csv',3)