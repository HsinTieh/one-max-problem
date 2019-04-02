# This is about OneMax-probram
import random 
import time
import HC
import SA
import TS
import GA
import matplotlib.pyplot as plt

def plotData(plt, data, name):
  x = [p[0] for p in data]
  y = [p[1] for p in data]
  plt.plot(x, y,label=name, linestyle="-")
 
def SAFun(randlist,iteaation):
    #SA  (list, fitness,T(customize),K)  
    start = time.time()    
    sa=SA.Individual(randlist,randlist.count(1),100,0) 
    
    sa,iterSA = SA.action(sa,iteaation)
    
    end = time.time() 
    print('SA : ',end-start)     
    #print(sa.init_list)
    #print(sa.fitness)
    plotData(plt, iterSA, 'SA')

def HCFun(randlist,iteaation):
    #HC
    start = time.time()    
    hc=HC.Individual(randlist,randlist.count(1))
    #for i in range(1000):
    hc,iterHC = HC.action(hc,iteaation)
        
    end = time.time() 
    print('HC : ',end-start)    
    #print(hc.data)
    #print(hc.fitness)
    plotData(plt, iterHC, 'HC')
    
def TSFun(randlist,iteaation):
    #TS  (list, fitness,tabu list)    
    #禁忌表初始化
    start = time.time()
    tabu_list = []
    tabu_len=10
    
    for i in range(tabu_len):
        tabu_list.append(-1)
    
    ts=TS.Individual(randlist,randlist.count(1),tabu_list) 
    
    
    ts,iterTS = TS.action(ts,iteaation)
    end = time.time() 
    print('TS : ',end-start)  
    plotData(plt, iterTS,'TS')    
    #print(ts.data)
    #print(ts.fitness)
 
def GAFun(randlist,iteaation):
  #data,scale,geneLength,selectPro,crossoverPro,mutationPro,itear1ation,maxPop
    start = time.time()
    iterGA = GA.action(randlist,1000,100,0.8,0.8,0.01,iteaation,3000)
    end = time.time() 
    print('GA : ',end-start)  
    plotData(plt, iterGA, 'GA')   
    
#main
    
iteaation=800
#initial list
randlist = []
for i in range(100):
    randlist.append(random.randint(0,1))

SAFun(randlist,iteaation)
HCFun(randlist,iteaation)
TSFun(randlist,iteaation)
GAFun(randlist,iteaation)

plt.title('One Max Problem')
plt.xlabel('iteration')
plt.ylabel('fitness')
plt.legend(loc='best')
plt.savefig('result.png')
plt.show()

 
 
 
 