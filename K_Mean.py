# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 20:39:55 2018

@author: ````````````````````
"""
from random import choice
import numpy as np
import math
from matplotlib import pyplot as plt

class K_Mean:
    
    def __init__(self,datasets,k):
        self.datasets=datasets
        self.k=k
        self.clusterAssment=np.mat(np.zeros((self.datasets.shape[0],1)))
        self.core=[]
        
    def init_core(self):   
        for i in range(self.k):
            self.core.append(choice(self.datasets))
        return self.core
    
    def euclidean_distance(self,a,b):
        return math.sqrt(np.power(a - b, 2).sum())
    
    def update_core(self):       
        for i in range(self.k):
            c=[]
            for j in range(len(self.clusterAssment)):
                if self.clusterAssment[j]==i:
                    c.append(self.datasets[j])
            if len(c)>0:
                d=np.mean(c,axis=0)
                self.core[i]=d
        return self.core
                        
    def k_mean(self):
        n=self.datasets.shape[0]
        self.core=self.init_core()
        clusterChanged=True
        while clusterChanged:
            clusterChanged=False
            for i in range(n):
                minDist=np.inf
                minIndex=-1
                for j in range(self.k):
                    dist=self.euclidean_distance(self.core[j],self.datasets[i])
                    if dist<minDist:
                        minDist=dist
                        minIndex=j
                if self.clusterAssment[i]!=minIndex:
                    clusterChanged=True
                    self.clusterAssment[i]=minIndex
            self.core=self.update_core()    
        return self.clusterAssment
    
    def show(self):
        plt.figure(figsize=(6,6))
        numSamples, dim = self.datasets.shape  
        mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']  
        for i in range(numSamples):  
            markIndex = int(self.clusterAssment[i])  
            plt.plot(self.datasets[i][0], self.datasets[i][1], mark[markIndex])  
        mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']  
        for i in range(self.k):  
            plt.plot(self.core[i][0], self.core[i][1], mark[i], markersize = 12)  
        plt.show()
    
if __name__ == '__main__':
    a=[[0.697,0.460],[0.774,0.376],[0.634,0.264],[0.608,0.318],[0.556,0.215],
       [0.403,0.237],[0.481,0.149],[0.437,0.211],[0.666,0.091],[0.243,0.267],
       [0.245,0.057],[0.343,0.099],[0.639,0.161],[0.657,0.198],[0.360,0.370],
       [0.593,0.042],[0.719,0.103],[0.359,0.188],[0.339,0.241],[0.282,0.257],
       [0.748,0.232],[0.714,0.346],[0.483,0.312],[0.478,0.437],[0.525,0.369],
       [0.751,0.489],[0.532,0.472],[0.473,0.376],[0.725,0.445],[0.446,0.459]]
    a=np.array(a)
    d=K_Mean(a,3)
    g=d.k_mean()
    d.show()
 
