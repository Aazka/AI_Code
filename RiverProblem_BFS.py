class RiverProblem:
    State=[1,1,1,1,1]
    Path=[]
R=RiverProblem()
#0=Wolf,1=Goat,2=corn,3=Farmer,4=Boat
Goal=[0,0,0,0,0]
Qeuee=[]
ExploredSet=[]

def PrintRP(Temp):
   # i=0
   # while i < 3:
        print(" ",Temp.Path)
   #     i+=1     
def CheckGoal(Goal,State):
    if Goal != State:
        return False
    else:
        return True

def CheckExploredSet(State,ExploredSet):
    c = len(ExploredSet)
    i = 0
    while i < c:
       if ExploredSet[i] == State:
           return False
       i+=1    
    return True       

def Validation(State):
        if State[2]==0 and State[1]==0 and State[3]==1:
            return False
        elif State[0]==0 and State[1]==0 and State[3]==1:
            return False
        elif State[0] == 1 and State[1] == 1 and State[3]==0:
            return False
        elif State[1] == 1 and State[2] == 1 and State[3]==0:
            return False
        else:
            return True

def FarmerAndGoatRight(Temp):
    P = RiverProblem()
    import copy
    P.State=copy.deepcopy(Temp.State)
    P.Path=copy.deepcopy(Temp.Path)
    P.State[1] = 0
    P.State[3] = 0
    P.State[4] = 0
    if Validation(P.State) == True:
        P.Path.append("FarmerMoveGoatRight")
        return P
    else:
        return 0

def FarmerAndGoatleft(Temp):
    P = RiverProblem()
    import copy
    P.State=copy.deepcopy(Temp.State)
    P.Path=copy.deepcopy(Temp.Path)
    P.State[1] = 1
    P.State[3] = 1
    P.State[4] = 1
    if Validation(P.State) == True:
        P.Path.append("FarmerMoveGoatLeft")
        return P
    else:
        return 0


def FarmerAndWolfRight(Temp):
    P = RiverProblem()
    import copy
    P.State=copy.deepcopy(Temp.State)
    P.Path=copy.deepcopy(Temp.Path)
    P.State[0] = 0
    P.State[3] = 0
    P.State[4] = 0
    if Validation(P.State) == True:
        P.Path.append("FarmerMoveWolfRight")
        return P
    else:
        return 0

def FarmerAndWolfleft(Temp):
    P = RiverProblem()
    import copy
    P.State=copy.deepcopy(Temp.State)
    P.Path=copy.deepcopy(Temp.Path)
    P.State[0] = 1
    P.State[3] = 1
    P.State[4] = 1
    if Validation(P.State) == True:
        P.Path.append("FarmerMoveWolfLeft")
        return P
    else:
        return 0


def FarmerAndCornRight(Temp):
    P = RiverProblem()
    import copy
    P.State=copy.deepcopy(Temp.State)
    P.Path=copy.deepcopy(Temp.Path)
    P.State[2] = 0
    P.State[3] = 0
    P.State[4] = 0
    if Validation(P.State) == True:
        P.Path.append("FarmerMoveCornRight")
#        if CheckExploredSet(P.State,ExploredSet) == False:
#             ExploredSet.append(P.State)
        return P
    else:
        return 0

def FarmerAndCornleft(Temp):
    P = RiverProblem()
    import copy
    P.State=copy.deepcopy(Temp.State)
    P.Path=copy.deepcopy(Temp.Path)
    P.State[2] = 1
    P.State[3] = 1
    P.State[4] = 1
    if Validation(P.State) == True:
        P.Path.append("FarmerMoveCornLeft")
        return P
    else:
        return 0


def FarmerBackToLeft(Temp):
    P = RiverProblem()
    import copy
    P.State=copy.deepcopy(Temp.State)
    P.Path=copy.deepcopy(Temp.Path)
    P.State[3] = 1
    P.State[4] = 1
    if Validation(P.State) == True:
        P.Path.append("FarmerMoveLeft")
        return P
    else:       
        return 0

def CheckLeft(Temp):
    if Temp.State[3]==0 and Temp.State[4]==0:
        return 1
    else:
        return 0

def BreakLoop(Check,Goal,ExploredSet,Qeuee):
    if Check != 0:
        if CheckExploredSet(Check.State,ExploredSet) == False and CheckGoal(Goal,Check.State) == False:
            return False
        elif CheckExploredSet(Check.State,ExploredSet) == True and CheckGoal(Goal,Check.State) == False:
            Qeuee.append(Check) 
            return False
        else:
            print("Goal Found") 
          #  PrintRP(Check)
            print("Path :: ")
            print(Check.Path)
            return True
    else:
         return False
   

Check=RiverProblem()

if CheckGoal(Goal,Check.State) == False:
    Qeuee.append(Check)
    while True:
        if len(Qeuee)==0:
            break
        else:
            Temp =Qeuee.pop(0)
            #else:    
            if CheckGoal(Goal,Temp.State) == True:
                    break    
            if CheckExploredSet(Temp.State,ExploredSet) == True:
                    ExploredSet.append(Temp.State)
            if(CheckLeft(Temp) == 1):
                    Check = FarmerBackToLeft(Temp)
                    if BreakLoop(Check,Goal,ExploredSet,Qeuee) == True:
                        break
                    if Temp.State[1]==0 and Temp.State[3]==0 and Temp.State[4]==0:
                        Check = FarmerAndGoatleft(Temp)
                        if BreakLoop(Check,Goal,ExploredSet,Qeuee) == True:
                            break
                    if Temp.State[0]==0 and Temp.State[3]==0 and Temp.State[4]==0:
                        Check = FarmerAndWolfleft(Temp)
                        if BreakLoop(Check,Goal,ExploredSet,Qeuee) == True:
                            break
                    if Temp.State[2]==0 and Temp.State[3]==0 and Temp.State[4]==0:
                        Check = FarmerAndCornleft(Temp)
                        if BreakLoop(Check,Goal,ExploredSet,Qeuee) == True:
                            break
               
            else:    
                if Temp.State[1]==1 and Temp.State[3]==1 and Temp.State[4]==1:
                    Check = FarmerAndGoatRight(Temp)
                    if BreakLoop(Check,Goal,ExploredSet,Qeuee) == True:
                        break
                
                if Temp.State[0]==1 and Temp.State[3]==1 and Temp.State[4]==1:   
                    Check = FarmerAndWolfRight(Temp)
                    if BreakLoop(Check,Goal,ExploredSet,Qeuee) == True:
                        break
                if Temp.State[2]==1 and Temp.State[3]==1 and Temp.State[4]==1:   
                    Check = FarmerAndCornRight(Temp)
                    if BreakLoop(Check,Goal,ExploredSet,Qeuee) == True:
                      break
                   
else:
    print("Goal found") 
    #PrintRP(Check.State)
    print("Path :: ")
    print(Check.Path)
    input("Press Enter to close!!!")
    
                    
input("Press Enter to close!!!")