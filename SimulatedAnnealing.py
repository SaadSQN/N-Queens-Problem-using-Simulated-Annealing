import numpy as np 
import random
import copy
import math

def main():
    #Initiating board of random size
    boardSize = 4
    data = []
    outerCounter = 0
    innerCounter = 0

    while outerCounter < boardSize:
        innerCounter = 0
        row = []
        while innerCounter < boardSize:
            row.append(0)
            innerCounter = innerCounter + 1
        data.append(row)
        outerCounter = outerCounter + 1   

    i = 0
    #Initiating queens on board
    queenLocations = []

    #Populating Board with Queens
    while i < boardSize:
        a = random.randint(0,boardSize-1)
        b = random.randint(0,boardSize-1)
        checked = False
        if not queenLocations:
            checked = True

        while checked == False:
            for v in queenLocations:
                if (v[0] == a) and (v[1] == b):
                    a = random.randint(0,boardSize-1)
                    b = random.randint(0,boardSize)-1
                    checked = False
                else:
                    checked = True

        current = []  
        current.append(a)
        current.append(b)
        queenLocations.append(current)
        #print(current)
        data[a][b] = 1
        i = i + 1  

    #Calculate Objective Function
    def objectiveFunction(data):
        arrayValues = []
        count = 0
        while count < boardSize:
            arrayValues.append(0)
            count = count + 1
        
        currentQueen= 0
        for x in queenLocations:

            #Check row
            i = 0
            while i < boardSize:
                if (data[x[0]][i] == 1) and (i != x[1]) : 
                    arrayValues[currentQueen] = arrayValues[currentQueen] + 1
                i = i + 1

            #Check Column
            i = 0
            while i < boardSize:
                if (data[i][x[1]] == 1) and (i != x[0]) : 
                    arrayValues[currentQueen] = arrayValues[currentQueen] + 1
                i = i + 1

            #Check Left Diagonal Backwards
            r = x[0] -1
            c  = x[1] -1
            while r >= 0 and c >= 0:
                if (data[r][c] == 1) : 
                    arrayValues[currentQueen] = arrayValues[currentQueen] + 1
                r = r - 1
                c = c- 1

            #Check Left Diagonal Forwards
            r = x[0] + 1
            c  = x[1]  + 1
            while r <boardSize and c < boardSize:
                if (data[r][c] == 1) : 
                    arrayValues[currentQueen] = arrayValues[currentQueen] + 1
                r = r + 1
                c = c + 1

            #Check Right Diagonal Backwards
            r = x[0] +1
            c  = x[1] -1
            while r < boardSize and c >= 0:
                if (data[r][c] == 1) : 
                    arrayValues[currentQueen] = arrayValues[currentQueen] + 1
                r = r + 1
                c = c- 1

            #Check Right Diagonal Forwards
            r = x[0] - 1
            c  = x[1]  + 1
            while r >= 0 and c < boardSize:
                if (data[r][c] == 1) : 
                    arrayValues[currentQueen] = arrayValues[currentQueen] + 1
                r = r - 1
                c = c + 1

            currentQueen = currentQueen + 1

        #Final answer
        count = 0
        for u in arrayValues:
            count = count + u

        return count
    

    #Use simulated annealing to find solution

    #Initial Objective function
    obj = objectiveFunction(data)
    trial = copy.deepcopy(data)
    found = False
    x = 0
    while objectiveFunction(trial) != 0:
        print(trial)
        x= x + 1
        i = queenLocations[random.randint(0,boardSize-1)]
        urld = random.randint(0,3)
        
        #Check up
        if urld == 0:
            if(i[0] != 0 and trial[i[0]-1][i[1]] != 1):
                trial[i[0]][i[1]] = 0
                trial[i[0]-1][i[1]] = 1
                objNew = objectiveFunction(trial)
                DE = obj - objNew
                if objNew < obj :
                    i[0] = i[0] - 1
                    broke = True
                    obj = objNew
                elif (math.exp(DE / x) > random.uniform(0,1)):
                    i[0] = i[0] - 1
                    broke = True
                    obj = objNew
                else:
                    trial[i[0]][i[1]] = 1
                    trial[i[0]-1][i[1]] = 0

        #Check down
        if urld == 1:
            if (i[0] != boardSize - 1 and trial[i[0]+1][i[1]] != 1):
                trial[i[0]][i[1]] = 0
                trial[i[0]+1][i[1]] = 1
                objNew = objectiveFunction(trial)
                DE = obj - objNew
                if objNew < obj :
                    i[0] = i[0] + 1
                    broke = True
                    obj = objNew
                elif (math.exp(DE / x) > random.uniform(0,1)):
                    i[0] = i[0] + 1
                    broke = True
                    obj = objNew
                else:
                    trial[i[0]][i[1]] = 1
                    trial[i[0]+1][i[1]] = 0

        #Check right
        if urld == 2:

            if (i[1] != boardSize - 1 and trial[i[0]][i[1]+1] != 1):
                trial[i[0]][i[1]] = 0
                trial[i[0]][i[1]+1] = 1
                objNew = objectiveFunction(trial)
                DE = obj - objNew
                if objNew < obj :
                    i[1] = i[1] + 1
                    broke = True
                    obj = objNew
                elif (math.exp(DE / x) > random.uniform(0,1)):
                    i[1] = i[1] + 1
                    broke = True
                    obj = objNew    
                else:
                    trial[i[0]][i[1]] = 1
                    trial[i[0]][i[1]+1] = 0
            
        #Check left
        if urld == 3:
            if (i[1] != 0 and trial[i[0]][i[1]-1] != 1):
                trial[i[0]][i[1]] = 0
                trial[i[0]][i[1]-1] = 1
                objNew = objectiveFunction(trial)
                DE = obj - objNew
                if objNew < obj :
                    i[1] = i[1] - 1
                    broke = True
                    obj = objNew
                elif (math.exp(DE / x) > random.uniform(0,1)):
                    i[1] = i[1] - 1
                    broke = True
                    obj = objNew     
                else:
                    trial[i[0]][i[1]] = 1
                    trial[i[0]][i[1]-1] = 0
        

    print("\n")
    for x in data:
        print(x)
    print("\n")
        
    print("Initial Objective Function is : ")
    print(objectiveFunction(data))

    if(objectiveFunction(data) == objectiveFunction(trial)):
        print("INITIAL STATE IS BEST POSSIBLE SOLUTION")
    else:

        print("\n")
        for x in trial:
            print(x)
        print("\n")
        
        print("Final Objective Function is : ")
        print(objectiveFunction(trial))


if __name__ == "__main__":
    main()
