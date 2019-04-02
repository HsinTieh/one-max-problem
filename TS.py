# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 19:11:57 2019

@author: toke8
"""
import random
import time
class Individual:
    def __init__(self,data,fitness,tabu_list):
        self.data=data
        self.fitness=fitness
        self.tabu_list=tabu_list

#mothed : change someone of initial list
def action(ts,iteration):
    #紀錄收斂速度(iteration)
    iterTS=[]

    for i in range(iteration):
        iterTS.append([i,ts.fitness])
        # new_list=init_list >>>>>ip(new) == id(init)
        new_list = ts.data[:]
        tabu_list=ts.tabu_list
        
        change_index = random.randint(0,99)
        #print(ts.fitness)
        #在禁忌表是否有重複
        while change_index in tabu_list:
            #print('I will')
            change_index=random.randint(0,99)
        
        #在最前面插入
        tabu_list.insert(0,change_index)
        #移除最後元素
        tabu_list.pop()
        
        if  new_list[change_index] == 0:
            new_list[change_index] = 1
        else:
            new_list[change_index] = 0
       
        ts = evaluation(ts,new_list)

    return ts,iterTS;

def evaluation(ts, new_list):
    data = ts.data
    fitness = ts.fitness
    tabu_list = ts.tabu_list
    
    next_fitness = new_list.count(1)
    
    if(fitness < next_fitness):
        fitness=next_fitness
        data=new_list
    
    ts_ = Individual(data,fitness,tabu_list)
    return ts_
    
    
    
    
    
    
    
    
    
    