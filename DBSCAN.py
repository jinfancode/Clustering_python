# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 10:42:11 2018

@author:Jin_F
"""
import math
import numpy as np
from random import choice
class DBSCAN:
    def __init__(self,datasets,minpts,eps):
        '''
            self.datasets:数据集
            self.minpts:邻域内的个数
            self.eps:邻域的大小
            self.classifications:聚类簇集合
        '''
        self.datasets=datasets
        self.minpts=minpts
        self.eps=eps
        self.NOISE=None
        self.UNCLASSIFIED=False
        self.classifications = [self.UNCLASSIFIED] * self.datasets.shape[0]
        
    def euclidean_distance(self,a,b):
        '''
            计算两点之间的欧式距离
            input:
                a:第一个点
                b:第二个点
            return：两点之间的欧式距离 
        '''
        return math.sqrt(np.power(a - b, 2).sum())
    
    def eps_neighbor(self,a,b):
        '''
           判断a,b之间的距离是否小于self.eps
           input:
                a:第一个点
                b:第二个点
            return：True or False  
        '''
        return self.euclidean_distance(a,b)<self.eps
       
    def region_query(self,pointId):
        '''
            查询某个点的邻域值
            input:
                pointId:给定点的下标
            return:返回该点邻域内所有点的下标
        '''
        n=self.datasets.shape[0]
        seeds=[]
        for i in range(n):
            if self.eps_neighbor(self.datasets[pointId],self.datasets[i]):
                seeds.append(i)
        return seeds
    
    def select_core(self):
        core=[]
        for i in range(self.datasets.shape[0]):
            if len(self.region_query(i))>=self.minpts:
                core.append(i)
        return core
    
    def mydbscan(self):
        '''
            core:初始化核心对象
            自顶向下
        '''
        cluster_id = 1
        core=self.select_core() 
        while len(core)>0:  
            coreId=choice(core)
            seeds=self.region_query(coreId)
            while len(seeds)>0:
                current_point = seeds[0]
                if len(self.region_query(current_point))>=self.minpts:
                    core.remove(current_point)
                else:
                    self.classifications[current_point]=self.NOISE
                if self.classifications[current_point] == self.UNCLASSIFIED or self.classifications[current_point] == self.NOISE:
                    self.classifications[current_point] = cluster_id 
                seeds = seeds[1:]
            cluster_id=cluster_id+1
        return self.classifications

    def expand_cluster(self,classifications, point_id, cluster_id):
        seeds = self.region_query(point_id)
        if len(seeds)<self.minpts:
            classifications[point_id] = self.NOISE
            return False
        else:
            classifications[point_id] = cluster_id
            for i in seeds:
                classifications[i] = cluster_id  
            while len(seeds) > 0:
                current_point = seeds[0]
                results = self.region_query(current_point)
                if len(results) >= self.minpts:
                    for i in range(len(results)):
                        result_point = results[i]
                        if classifications[result_point] == self.UNCLASSIFIED or classifications[result_point] == self.NOISE:
                            if classifications[result_point] == self.UNCLASSIFIED:
                                seeds.append(result_point)
                            classifications[result_point] = cluster_id
                seeds = seeds[1:]
        return True
   
    def dbscan(self):
        '''
            自底向上
        '''
        cluster_id = 1
        n=self.datasets.shape[0]
        for i in range(n):
            if self.classifications[i] == self.UNCLASSIFIED:
                if self.expand_cluster(self.classifications, i, cluster_id):
                    cluster_id = cluster_id + 1
        return self.classifications    
    
if __name__ == '__main__':
    m=[[1,1.1],[1.2,0.8],[0.8,1],[3.7,4],[3.9,3.9],[3.6,4.1],[10,10]]
    m = np.array(m)
    e=DBSCAN(m,2,0.5)
    f=e.mydbscan()
    f1=e.dbscan()
