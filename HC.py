import random
import time

class Individual:
    def __init__(self,data,fitness):
        self.data=data
        self.fitness=fitness

#mothed 1: change someone of initial list
def action(hc,iteration):
    #紀錄收斂速度(iteration)
    iterHC=[]

    for i in range(iteration):
        iterHC.append([i,hc.fitness])
        # new_list=init_list >>>>>ip(new) == id(init)
        new_list = hc.data[:]
        change_index = random.randint(0,99)
      
        if  new_list[change_index] == 0:
            new_list[change_index] = 1
        else:
            new_list[change_index] = 0
    
        hc = evaluation(hc,new_list)


    return hc,iterHC;
    
    


def evaluation(hc, new_list):
    data = hc.data
    fitness = hc.fitness

    next_fitness = new_list.count(1)
    
    if next_fitness > fitness :
        fitness=next_fitness
        data=new_list
    hc_ = Individual(data, fitness)
    return hc_


