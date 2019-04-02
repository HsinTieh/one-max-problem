import random
import math
import time
import matplotlib.pyplot as plt
#(資料, 適應度, 溫度,變化率)
class Individual:
    def __init__(self,data,fitness,T,K):
        self.data = data
        self.fitness = fitness
        self.T = T
        self.K = K 
        
        
#mothed : change someone of initial list
def action(sa,iteration):
    #紀錄收斂速度(iteration)
    iterSA=[]


    for i in range(iteration):
        iterSA.append([i,sa.fitness])
        # new_list=init_list >>>>>ip(new) == id(init)
        new_list = sa.data[:]
        change_index = random.randint(0,99)
        #print(sa.fitness)
        if  new_list[change_index] == 0:
            new_list[change_index] = 1
        else:
            new_list[change_index] = 0
       
        sa = evaluation(sa,new_list)

    return sa,iterSA;
    
#評估誰當前適應度較高
def evaluation(sa,new_list):
    T=sa.T
    K=sa.K
    list_=sa.data
    fitness=sa.fitness
    #evaluate state
    next_fitness = new_list.count(1)
    #find better
    if next_fitness > fitness:
        fitness=next_fitness
        list_=new_list

    else:
        #Simulate Anneal Arithmetic 
        pro=math.exp(-(K/T))
        rnd=random.random()
        if pro>rnd:
            fitness=next_fitness
            list_=new_list

    K=K+1
    sa_ = Individual(list_,fitness,T,K)
    return sa_



 
