import random
import copy

n=input("enter the number of queens")
n=int(n)         #converting str object to integer
global solution_count
solution_count=0

for i in range(10):
    
    global initial_pos

    matrix = [[0 for x in range(n)] for y in range(n)] #initializing all the elements in the matirx to 0

    initial_pos=[] 

    for i in range(0,n):
        r=random.randint(0,n-1)
        #print (r)
        initial_pos.append(r)
        matrix[r][i]='Queen'   #placing the queens in some random initial positions, one per each column
    #print (matrix)
    print ("initial state")
    print (initial_pos)
    global back_up
    back_up=copy.copy(initial_pos)
    #print (back_up)

##    for s in range(0,8):
##        print (matrix[s])
        

    def heuristic(initial_pos):
        c=1
        count=0
        for i in range(len(initial_pos)):
            c=1
            for j in range(i+1,len(initial_pos)):
                #print (i,j)
                if initial_pos[i]==initial_pos[j]:
                    count+=1

                if initial_pos[i]-c==initial_pos[j] and i+c==j:
                    #print("counting")
                    count+=1
                if initial_pos[i]+c==initial_pos[j] and i+c==j:
                    #print("counting")
                    count+=1

                c+=1
                    
        return count
    global new
    
    new=copy.copy(back_up)
    
    def loading(initial_pos): 
        #global initial_pos
        global back_up
        global new
        global solution_count
        
        min_k=heuristic(initial_pos)
        flag=copy.copy(min_k)
        #print (min_k)
        
        for i in range(len(initial_pos)):       
            initial_pos=copy.copy(new)
            #print(initial_pos)
            #number=[]
            for j in range(len(initial_pos)):
                initial_pos[i]=j
                #print (initial_pos)
                k=heuristic(initial_pos)
                if k < min_k:
                    min_k=k
                    #print (min_k)
                    #print (initial_pos)
                    new=copy.copy(initial_pos)
                
                if min_k == 0:
                    print("final state- Solution")
                    print(new)
                    solution_count+=1
                    return new
        if flag==min_k:
            print ("final state-not a solution")
            print (new)
            return new

        #print(new)
        loading(new)
            
    loading(initial_pos)
print ("number of solutions is")
print (solution_count)

    #print (back_up)
    
    




