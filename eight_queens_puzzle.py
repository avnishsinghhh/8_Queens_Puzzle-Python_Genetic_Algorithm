import random;
import math;

#Parameter Assigment
mutationRate = 0.2;
totalPopulation = 150;
crossOver = 0.5;
generationCount = 1000;
target_len = 8;
    
################################################################################################

#Function To Find Diagonals For Each Position
def findDiagonal(index,lst):
            
    diag1=[];
    diag2=[];
        
    x1=y1=x2=y2=0;
        
    x1=lst;
    y1=index;       
    while (x1 > -1 and x1 < 8 and y1 > -1 and y1 < 8): 
        if y1 != lst:
            diag1.append([x1,y1]);
        x1=x1+1;
        y1=y1-1;
        
        
    x1=lst;
    y1=index;     
    while (x1 > -1 and x1 < 8 and y1 > -1 and y1 < 8): 
        if diag1.count([x1,y1]) == 0 and y1 != lst:
            diag1.append([x1,y1]);
        
        x1=x1-1;
        y1=y1+1;


    x2=lst;
    y2=index;           
    while (x2 > -1 and x2 < 8 and y2 > -1 and y2 < 8):             
        if x2 != lst:
            diag2.append([y2,x2]);
            
        x2=x2-1;
        y2=y2-1;
            
    x2=lst;
    y2=index;          
    while (x2 > -1 and x2 < 8 and y2 > -1 and y2 < 8): 
        if diag2.count([y2,x2]) == 0 and x2 != lst:
            diag2.append([y2,x2]);
            
        x2=x2+1;
        y2=y2+1;
                     
    diag1.sort(key = lambda x : x[1], reverse=True); 
    diag2.sort(key = lambda x : x[1], reverse=False);
        
    return diag1, diag2;
    
    
#Function To Generate Random population
def generatePopulation(totalPopulation):
    population=[];

    for i in range(totalPopulation):
        
        rndm=[];
        for j in range(target_len):   
            elem = random.randint(0,7);
            rndm.append(elem);

        population.append(rndm);
    
    return population;


#Function To Check Fitness and probability of bieng picked
def find_fitness_and_probability(totalPopulation, population):
    fitness=[];
    probability=[];

    for i in range(totalPopulation): 
        
        fit=target_len;   
        
        for e in range(len(population[i])):
            for f in range(len(population[i])):
                if e != f:
                    if population[i][e] == population[i][f]:
                        fit-=1;
    
        for j in range(len(population[i])):
            diagonal1, diagonal2 = findDiagonal(j,population[i][j]);
    
            for m in range(len(diagonal1)):
                if (m >=0 and m < target_len and population[i][diagonal1[m][0]] == diagonal1[m][1]):
                    fit -= 1;
                    m = m+1;
    
            for m in range(len(diagonal2)):     
                if (m >=0 and m < target_len and population[i][diagonal2[m][0]] == diagonal2[m][1]):
                    fit -= 1;
                    m = m+1;
                
        fitness.append(fit);
        probability.append(fit/target_len);
        
    return fitness, probability;

#Function To Perform CrossOver and Mutation
def crossOver_Mutation(CrossOverPoint, mutationRate, parent1, parent2):
        child = parent1[0:CrossOverPoint] + parent2[CrossOverPoint:];
        
        #Removing Duplicate Elements  
        child = remove_duplicate_element(child);
    
        #Performing Mutation
        elem_to_mutate = math.ceil(mutationRate * target_len);
                
        for ele in range(elem_to_mutate):    
            pos1_child = random.randint(0,target_len-1);
            pos2_child = random.randint(0,target_len-1);
                            
            child[pos1_child], child[pos2_child] = child[pos2_child], child[pos1_child];
        
        return child;

#Function To Sort Fitness and Probability
def sort_probability(probability):
    prob_order = [];
    for p in range(len(probability)):
        prob_order.append([p,probability[p]]);
        
    prob_order.sort(key = lambda x : x[1], reverse=True);
    
    return prob_order;

#Function To Remove Duplicate Elements
def remove_duplicate_element(lst):
    for e in range(len(lst)):
        if lst.count(lst[e]) > 1:
            rndnum = random.randint(0,7);
        
            flag=0
            while(flag==0):
                if lst.count(rndnum) == 0:
                    lst[e] = rndnum;
                    flag=1;
                else:
                    rndnum = random.randint(0,7);
    return lst;

#Function To Print Results
def print_result(count,parent1,parent2,child1,child2):
    print("Generation:",count,"Parent1:",parent1,"Parent2:",parent2,"Child1:",child1,"Child2:",child2);


#Draw Chessboard
def draw_chessboard(lst): 
    print("\n   ","0"," ","1"," ","2"," ","3"," ","4"," ","5"," ","6"," ","7")  
    for i in range(0,8):
        Q0=Q1=Q2=Q3=Q4=Q5=Q6=Q7=' ';
        print("  + - + - + - + - + - + - + - + - +");
        pos = lst.index(i);
        if pos == 0:
            Q0='X';
        elif pos == 1:
            Q1='X';
        elif pos == 2:
            Q2='X';
        elif pos == 3:
            Q3='X';
        elif pos == 4:
            Q4='X';
        elif pos == 5:
            Q5='X';
        elif pos == 6:
            Q6='X';
        elif pos == 7:
            Q7='X';
        
        print(i,"|",Q0,"|",Q1,"|",Q2,"|",Q3,"|",Q4,"|",Q5,"|",Q6,"|",Q7,"|");
    print("  + - + - + - + - + - + - + - + - +");    
    
################################################################################################

def main():
    
    #Generate Random Population
    population = generatePopulation(totalPopulation);
    
    #Find Fitness and Probability
    fitness, probability = find_fitness_and_probability(len(population), population);
    
    #Sort Fitness and Probability
    prob_order = sort_probability(probability);
    
    #Performing Selection, Crossover, Mutation and Display Results
    count = 0;
    for _ in range(generationCount):
        
        count += 1;
                            
        parent1 = population[prob_order[0][0]];
        parent2 = population[prob_order[1][0]];
    
        CrossOverPoint = int(target_len * crossOver);
            
        child1 = crossOver_Mutation(CrossOverPoint, mutationRate, parent1, parent2);
        child2 = crossOver_Mutation(CrossOverPoint, mutationRate, parent2, parent1);
        
        if (fitness[prob_order[0][0]] == target_len):
            print_result(count,parent1,parent2,child1,child2);
            break;
        elif (fitness[prob_order[1][0]] == target_len):
            print_result(count,parent1,parent2,child1,child2);
            break;
    
        population.append(child1);
        population.append(child2);
                    
        fitns, probab = find_fitness_and_probability(2, [child1,child2]);
        
        for i in range(len(fitns)):
            fitness.append(fitns[i]);
            probability.append(probab[i]);
                            
        prob_order = sort_probability(probability);
        
        print_result(count,parent1,parent2,child1,child2);
            
    
    if count != generationCount:
        print("\n****************************************");
        print("Search Result: ",parent1);
        print("****************************************");
    else:
        print("\n****************************************************");
        print("Search Failed With-In Specified Generation Count !!!")
        print("****************************************************");
    
    #Draw Chessboard With Queen Positions
    draw_chessboard(parent1);
    
    #Just to display final result in case program is tested via automated tool
    print("\n",parent1)
    
if __name__ == '__main__':
    main()