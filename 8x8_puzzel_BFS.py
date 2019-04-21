class Puzzle:
   State = []
   Path  = []
   Ci = -1 
   Ri = -1
   
P = Puzzle()
Goal=[[1,2,3],[4,5,6],[7,8,-1]]
Qeuee=[]
ExploredSet=[]


def PrintPuzzle(State):
    print()
    i=0
    while i < 3:
        if State[i][0] == -1:
            print(" ",State[i][1],State[i][2])
        elif State[i][1] == -1:
            print(State[i][0]," ",State[i][2]) 
        elif State[i][2] == -1:
            print(State[i][0],State[i][1]," ")
        else:
            print(State[i][0],State[i][1],State[i][2])    
        i+=1       
    print()   

def CheckInput(P,num):
    x = len(P.State)
    i=0
    while i < x:
        y = len(P.State[i])
        j=0
        while j < y:
            if P.State[i][j] == num:
                return False
            j+=1
        i+=1            
    return True            

def TakeInput(P):
    i=0
    while i < 3:
        j=0
        P.State.append([])
        while j < 3:
            while True:
                X = int((input("Enter Number Range(1-8): " )))
                if (X < 0 or X > 8) and X != -1:
                    print("Invalid Range")
                else:
                     if CheckInput(P,X)==False:
                         print("Already Entered")
                     else:
                          print("Entered Successfully")
                          if X == -1:
                             P.Ri = i
                             P.Ci  = j
                          P.State[i].append(X)  
                          break         
            j+=1
        i+=1  

def CheckGoal(Goal,State):
    if Goal != State:
        return False
    else:
        return True

def MoveRight(Temp): 
    P = Puzzle()
    import copy
    P.State = copy.deepcopy(Temp.State)
    P.Path = copy.deepcopy(Temp.Path)
    P.Ci=Temp.Ci
    P.Ri=Temp.Ri
    if P.Ci != 2: 
        P.State[P.Ri][P.Ci],P.State[P.Ri][P.Ci+1] = P.State[P.Ri][P.Ci+1] , P.State[P.Ri][P.Ci]
        P.Path.append("Right")
        P.Ci+=1
        return P
    else:
        return 0

def MoveLeft(Temp):
    P = Puzzle()
    import copy
    P.State = copy.deepcopy(Temp.State)
    P.Path = copy.deepcopy(Temp.Path)
    P.Ci=Temp.Ci
    P.Ri=Temp.Ri
    if P.Ci != 0: 
        P.State[P.Ri][P.Ci],P.State[P.Ri][P.Ci-1] = P.State[P.Ri][P.Ci-1] , P.State[P.Ri][P.Ci]
        P.Path.append("Left")
        P.Ci-=1

        return P
    else:
        return 0

def MoveUp(Temp):
    P = Puzzle()
    import copy
    P.State = copy.deepcopy(Temp.State)
    P.Path = copy.deepcopy(Temp.Path)
    P.Ci=Temp.Ci
    P.Ri=Temp.Ri
    if P.Ri != 0: 
        P.State[P.Ri][P.Ci],P.State[P.Ri-1][P.Ci] = P.State[P.Ri-1][P.Ci] , P.State[P.Ri][P.Ci]
        P.Path.append("Up")
        P.Ri-=1
        return P
    else:
        return 0

def MoveDown(Temp):
    P = Puzzle()
    import copy
    P.State = copy.deepcopy(Temp.State)
    P.Path = copy.deepcopy(Temp.Path)
    P.Ci=Temp.Ci
    P.Ri=Temp.Ri
    if P.Ri != 2: 
        P.State[P.Ri][P.Ci],P.State[P.Ri+1][P.Ci] = P.State[P.Ri+1][P.Ci] , P.State[P.Ri][P.Ci]
        P.Path.append("Down")
        P.Ri+=1
        return P
    else:
        return 0
            

def CheckExploredSet(State,ExploredSet):
    c = len(ExploredSet)
    i = 0
    while i < c:
       if ExploredSet[i] == State:
           return False
       i+=1    
    return True       

def BreakLoop(Check,Goal,ExploredSet,Qeuee):
    if Check != 0:
        if CheckExploredSet(Check.State,ExploredSet) == False and CheckGoal(Goal,Check.State) == False:
            return False
        elif CheckExploredSet(Check.State,ExploredSet) == True and CheckGoal(Goal,Check.State) == False:
            Qeuee.append(Check) 
            return False
        else:
            print("After Goal") 
            PrintPuzzle(Check.State)
            print("Path :: ")
            print(Check.Path)
            return True
    else:
         return False
                    
                    
            
TakeInput(P)

print("Before Goal")
PrintPuzzle(P.State)

if CheckGoal(Goal,P.State) == False:
    
    Qeuee.append(P)
    
    while True:
        
        if len(Qeuee)!= 0:
            Temp = Qeuee.pop(0)
            if CheckExploredSet(Temp.State,ExploredSet) == True:
                ExploredSet.append(Temp.State) 
                
            Check = MoveLeft(Temp) 
            if BreakLoop(Check,Goal,ExploredSet,Qeuee) == True:
                break
            Check = MoveRight(Temp)
            if BreakLoop(Check,Goal,ExploredSet,Qeuee) == True:
                break
            
            Check = MoveUp(Temp)
            if BreakLoop(Check,Goal,ExploredSet,Qeuee) == True:
                break
            
            Check = MoveDown(Temp)
            if BreakLoop(Check,Goal,ExploredSet,Qeuee) == True:
                break
               
else:
    print("After Goal") 
    PrintPuzzle(P.State)
    print("Path :: ")
    print(P.Path)                     

input("Press Enter to close!!!")