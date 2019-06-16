import random

Chromosomes = [[0 for col in range(10)] for row in range(50)] 
Ratio = [0 for cols in range(50)]
LocalMaxima = [0 for col in range(10)]
MutationCount = 0
CitiesData = [
    [0, 130, 181, 336, 423, 358, 376, 1246, 55, 180],
    [130, 0, 107, 217, 283, 407, 425, 1105, 165, 108],
    [181, 107, 0, 242, 329, 303, 321, 1152, 96, 2],
    [336, 217, 242, 0, 103, 519, 538, 925, 329, 242],
    [423, 283, 329, 103, 0, 591, 610, 833, 401, 314],
    [358, 407, 303, 519, 591, 0, 20, 1429, 307, 301],
    [376, 425, 321, 538, 610, 20, 0, 1446, 324, 317],
    [1246, 1105, 1152, 925, 833, 1429, 1446, 0, 1224, 1137],
    [55, 165, 96, 329, 401, 307, 324, 1224, 0, 135],
    [180, 108, 2, 242, 314, 301, 317, 1137, 135, 0]]

def ParentInitialization():
    for i in range(50):
        for j in range(10):
            check = True
            while check:
                value = random.randint(1, 10)
                if value not in Chromosomes[i]:
                    Chromosomes[i][j] = value
                    check = False

def FitnessRatio():
    FitnessRatio = [0 for col in range(50)]
    Fitness = [0 for col in range(50)]
    TotalFitness = 0
    for i in range(50):
        Fitness[i] = Fitnes(Chromosomes[i])
        TotalFitness += Fitness[i]
    for i in range(50):
         FitnessRatio[i] = (Fitness[i] / TotalFitness) * 100
    return  FitnessRatio    

def Fitnes(Data):
    Distance = 0
    for i in range(10):
        Distance += CitiesData[Data[i-1]-1][Data[i]-1]
    Distance += CitiesData[Data[9]-1][Data[0]-1]
    return 1 / Distance
                
def WheelRotation(Ratio):
    Wheel = [0 for cols in range(50)]
    Wheel[0] = Ratio[0]
    for i in range(1, 50):
        Wheel[i] = Wheel[i - 1] + Ratio[i]
    return Wheel

def ParentSelection(Wheel):
    NextGenerationParent = [0 for cols in range(50)]
    for i in range(50):
        Temp = random.randint(0, 100)
        for j in range(50):
            if Temp <= Wheel[j]:
                NextGenerationParent[i] = j
                break
    return NextGenerationParent

def TwoChromosomeCrossover(Chromosome1, Chromosome2):
    NewChromosome1, NewChromosome2 = [0 for cols in range(10)], [0 for cols in range(10)]    
    for i in range(3,7):
        NewChromosome1[i] = Chromosome2[i]
        NewChromosome2[i] = Chromosome1[i]

    Col1 = 7;
    Col2 = 7;
    for i in range(7,10):
        if Chromosome1[i] not in NewChromosome1:
            NewChromosome1[Col1] = Chromosome1[i]
            Col1+=1
        if Chromosome2[i] not in NewChromosome2:
            NewChromosome2[Col2] = Chromosome2[i]
            Col2+=1    
    
    for i in range(0,3):
        if Col1 == 10:
            Col1 = 0
        if Chromosome1[i] not in NewChromosome1:
            NewChromosome1[Col1] = Chromosome1[i]
            Col1+=1              
        if Col2 == 10:
            Col2 = 0
        if Chromosome2[i] not in NewChromosome2:
            NewChromosome2[Col2] = Chromosome2[i]
            Col2+=1

    for i in range(3,7):
        if Col1 == 3 & Col2 == 3:
            break
        if Col1 == 10:
            Col1 = 0
        if Col1 == 3:
            Col1 = 3
        if Chromosome1[i] not in NewChromosome1:
            NewChromosome1[Col1] = Chromosome1[i]
            Col1+=1  
        if Col2 == 10:
            Col2 = 0            
        if Col2 == 3:
            Col2 = 3
        if Chromosome2[i] not in NewChromosome2:
            NewChromosome2[Col2] = Chromosome2[i]
            Col2+=1
    return NewChromosome1,NewChromosome2
         
def Crossover(NextGenerationParent):
   NextGeneration = [[0 for cols in range(10)] for rows in range(50)]
   for i in range(0, 50,2):
       j = NextGenerationParent[i+1]
       k = NextGenerationParent[i]
       Temp =  TwoChromosomeCrossover(Chromosomes[j], Chromosomes[k])
       NextGeneration[i], NextGeneration[i+1] = Temp[0], Temp[1]
   return NextGeneration

def Mutation():
    LocalMaxima[2], LocalMaxima[8] = LocalMaxima[8], LocalMaxima[2]
    LocalMaxima[5], LocalMaxima[9] = LocalMaxima[9], LocalMaxima[5]
    return LocalMaxima

ParentInitialization()      
for i in range(50):  
    Ratio=FitnessRatio()
    Wheel=WheelRotation(Ratio)
    NextGenerationParent = ParentSelection(Wheel)
    Chromosomes = Crossover(NextGenerationParent)
    Ratio = FitnessRatio()
    MaxIndex = Ratio.index(max(Ratio))  
    
    if LocalMaxima != Chromosomes[MaxIndex]:
        LocalMaxima = Chromosomes[MaxIndex]    
    else:
        MutationCount += 1
        if MutationCount == 5:
            MutationCount = 0
            Chromosomes[MaxIndex] = Mutation()  
 
print("Local Maxima: ",LocalMaxima)       
input()
