# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 19:40:36 2018

@author:Jin_F
"""
import math
class Hierarchical_Clustering:
    
    def __init__(self,datasets,ClusterNum):
        self.datasets=datasets
        self.ClusterNum=ClusterNum
        
    
    def initialize(self):
        self.originalClusters=[]
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
        while len(self.originalClusters)>self.ClusterNum:
            size=len(self.originalClusters)
            mindis=999999999999
            index_i=0
            index_j=0
            for i in range(size-1):
                for j in range(i+1,size):
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
    a=[[1,4,5], [3,6,1], [5,6,10], [7,2,11], [9,6,1], [2,1,5], [4,2,1], [6,6,5], [8,7,1], [0,1,0]]
    b=Hierarchical_Clustering(a,5)
    c=b.initialize()
    d=b.init_distance()
   
        
        
