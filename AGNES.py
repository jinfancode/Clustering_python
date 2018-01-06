# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 19:40:36 2018

@author:Jin_F
"""
import math
import numpy as np

class Hierarchical_Clustering:
    
    def __init__(self,datasets,ClusterNum):
        self.datasets=datasets
        self.ClusterNum=ClusterNum
        self.originalClusters=[]
    
    def initialize(self):  
        for i in range(len(self.datasets)):
            tempDataPoints=[]
            tempDataPoints.append(self.datasets[i])
            self.originalClusters.append(tempDataPoints)
        return self.originalClusters
    
    def euclidean_distance(self,point_one,point_two):
        size = len(point_one)
        result = 0.0
        for i in range(size):
            tmp = point_one[i] - point_two[i]
            result += pow(tmp, 2)
        result = math.sqrt(result)
        return result
    
    def mergeCluster(self,index_i,index_j):
        if index_i<index_j:
            for i in range(len(self.originalClusters[index_j])):
                self.originalClusters[index_i].append(self.originalClusters[index_j][i])
            del self.originalClusters[index_j]
        else:
            for i in range(len(self.originalClusters[index_i])):
                self.originalClusters[index_j].append(self.originalClusters[index_i][i])
            del self.originalClusters[index_i]
        
    def init_distance(self):
        self.originalClusters=self.initialize()
        while len(self.originalClusters)>self.ClusterNum:
            mindis=np.inf
            index_i=0
            index_j=0
            for i in range(len(self.originalClusters)-1):
                for j in range(i+1,len(self.originalClusters)):
                    for m in range(len(self.originalClusters[i])):
                        for n in range(len(self.originalClusters[j])):
                            tempdis=self.euclidean_distance(self.originalClusters[i][m],self.originalClusters[j][n])
                            if tempdis<mindis:
                                mindis=tempdis
                                index_i=i 
                                index_j=j
            self.mergeCluster(index_i,index_j)
        return self.originalClusters    

if __name__ == '__main__':
    a=[[0.697,0.460],[0.774,0.376],[0.634,0.264],[0.608,0.318],[0.556,0.215],
       [0.403,0.237],[0.481,0.149],[0.437,0.211],[0.666,0.091],[0.243,0.267],
       [0.245,0.057],[0.343,0.099],[0.639,0.161],[0.657,0.198],[0.360,0.370],
       [0.593,0.042],[0.719,0.103],[0.359,0.188],[0.339,0.241],[0.282,0.257],
       [0.748,0.232],[0.714,0.346],[0.483,0.312],[0.478,0.437],[0.525,0.369],
       [0.751,0.489],[0.532,0.472],[0.473,0.376],[0.725,0.445],[0.446,0.459]]
    b=Hierarchical_Clustering(a,7)
    d=b.init_distance()
