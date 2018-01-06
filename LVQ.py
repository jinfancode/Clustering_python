# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 21:00:42 2018

@author: Jin_F
"""
from random import choice
import math
import numpy as np
class LVQ:
    def __init__(self,datasets,classifications,k,learningrate,eps):
        self.datasets=datasets
        self.classifications=classifications
        self.learningrate=learningrate
        self.k=k
        self.eps=eps
        self.core=[]
        
        
    def init_core(self):
        seeds=[[] for i in range(self.k)]
        for i in range(self.classifications.shape[0]):
            seeds[self.classifications[i]].append(self.datasets[i])
        for i in range(self.k):
            self.core.append(choice(seeds[i]))
        return self.core
    
    def euclidean_distance(self,a,b):
        return math.sqrt(np.power(a - b, 2).sum())
    
    def lvq(self):
        self.core=self.init_core()
        for i in range(self.eps):
            for i in range(self.datasets.shape[0]):
                minDist=np.inf
                minIndex=-1
                for j in range(self.k):
                    dist=self.euclidean_distance(self.datasets[i],self.core[j])
                    if dist<minDist:
                        minDist=dist
                        minIndex=j
                if self.classifications[i]==minIndex:
                    self.core[minIndex]=self.core[minIndex]-self.learningrate*(self.datasets[i]-self.core[minIndex])
                else:
                    self.core[minIndex]=self.core[minIndex]+self.learningrate*(self.datasets[i]-self.core[minIndex])
        return self.core
                
if __name__ == '__main__':
    a=[[0.697,0.460],[0.774,0.376],[0.634,0.264],[0.608,0.318],[0.556,0.215],
       [0.403,0.237],[0.481,0.149],[0.437,0.211],[0.666,0.091],[0.243,0.267],
       [0.245,0.057],[0.343,0.099],[0.639,0.161],[0.657,0.198],[0.360,0.370],
       [0.593,0.042],[0.719,0.103],[0.359,0.188],[0.339,0.241],[0.282,0.257],
       [0.748,0.232],[0.714,0.346],[0.483,0.312],[0.478,0.437],[0.525,0.369],
       [0.751,0.489],[0.532,0.472],[0.473,0.376],[0.725,0.445],[0.446,0.459]]
    a=np.array(a)
    b=[2,2,2,2,3,0,3,0,3,0,1,1,3,3,0,3,3,0,0,0,2,2,4,4,4,2,4,4,2,4]
    b=np.array(b)
    m=b[5]
    r=LVQ(a,b,5,0.5,15)
    f=r.lvq()
