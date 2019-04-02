# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 20:37:51 2019

@author: toke8
"""
import random
import time
"""
(族群大小/基因大小/迭代次數/選擇複製概率(留下多少)/交配概率/突變概率)
step1 生成族群
step2 評估適應度
step3 選擇數好的基因留下
step4 交配
step5 突變
step1..step2..step3..step4........

"""
class geneIndividual:
    def __init__(self,gene,fitness):
        self.gene=gene
        self.fitness=fitness
    
def creatGroup(scale,geneLength):
    #生成族群
    group=[]
    randlist=[]
    for i in range(scale):
        for j in range(geneLength):
            randlist.append(random.randint(0,1))
        
        group.append(randlist[:])      

        del randlist[:]
   
    return group
        
def evaluate(group):
    #評估個體適應度
    eva_pop=[]
    for i in range(len(group)):
        gene = geneIndividual(group[i],group[i].count(1))
        eva_pop.append(gene)

    return eva_pop

def selection(evaluate_group,selectPro,maxPop):
    #適者生存論

   sort_group=sorted(evaluate_group, key=lambda pop: pop.fitness, reverse=True)
   live_member = len(sort_group)*selectPro
   if live_member > maxPop:
       sort_group=sort_group[:maxPop]
   else:
       sort_group=sort_group[:int(live_member)]
   return sort_group
    

def crossover(select_group,geneLength,crossoverPro):
    #交配
    temp =[]
    add_crossover_gene = []
    for gene in select_group:
        add_crossover_gene.append(gene.gene[:])
        
    for i in range(1,len(select_group),2):
        
        if crossoverPro > random.random():
        
            gene1 = select_group[i-1].gene
            gene2 = select_group[i].gene
            #進行交配中....   
             
            #交換位置
            changePoint = random.randint(0,geneLength-1)
             
            #切斷基因組
            temp_front = gene1[:changePoint]
            temp_back = gene1[changePoint:]
            #暫存基因列
            temp.append(temp_front)
            temp.append(temp_back)
             
            #切斷基因組
            temp_front = gene2[:changePoint]
            temp_back = gene2[changePoint:]
            #暫存基因列
            temp.append(temp_front)
            temp.append(temp_back)
            
            #結合新的基因串
            crossover_after_for_A = temp[0]+temp[3]
            crossover_after_for_B = temp[2]+temp[1]
            
            add_crossover_gene.append(crossover_after_for_A)
            add_crossover_gene.append(crossover_after_for_B)
            
            temp = []

    return add_crossover_gene
    
    
def mutation(crossover_group,geneLength,mutationPro):
    #突變
    mutation_group =[]

    for member in crossover_group:
    #for member in range(len(crossover_group)):
        if mutationPro > random.random():
            mutationPoint = random.randint(0,geneLength-1)    

            if member[mutationPoint] == 0:
                member[mutationPoint]=1
            else:
                member[mutationPoint]=0
            mutation_group.append(member)
        else:
            mutation_group.append(member)
    return mutation_group


    
def action(data,scale,geneLength,selectPro,crossoverPro,mutationPro,itear1ation,maxPop):
    #紀錄收斂速度(iteration)
    iterGA=[]

    bestFitness=0
 
    #生成種群  (group={gene1,gene2,......,geneN})
    group = creatGroup(scale,geneLength)
    group.append(data)
    
    for i in range(itear1ation):

        #分析 (evaluate_group={gene1(gene,fitness),gene2(gene,fitness),......,geneN})
        evaluate_group = evaluate(group)
        
        #選擇
        select_group=selection(evaluate_group,selectPro,maxPop)
      #  print(len(select_group))
        
        #尋找目前最好的適應度的基因
        if select_group[0].fitness > bestFitness:
            bestGene=select_group[0].gene
            bestFitness=select_group[0].fitness
        
        #交配
        crossover_group = crossover(select_group,geneLength,crossoverPro)
       # print(len(crossover_group))
       
        #突變
        mutation_group= mutation(crossover_group,geneLength,mutationPro)
       # print(len(mutation_group))
          
        group = mutation_group
        iterGA.append([i,bestFitness])
       # print('iter : ',i)
       # print('best fitness : ',bestFitness)
       # print('best gene: ',bestGene)

    return iterGA
        
        
        
        
        
        
        
        
        
        
        
        




