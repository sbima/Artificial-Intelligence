import random
import copy

n=input("enter the number of queens")
n=int(n)
##global sol
##global other
sol=[]
other={}
population={}

for i in range(1,101):
    ran_unique=[0,1,2,3,4,5,6,7]
    old=random.choice(ran_unique)
    initial_pos=[old]
    ran_unique.remove(old)
    for j in range(0,n-1):
        new=random.choice(ran_unique)
        ran_unique.remove(new)
        initial_pos.append(new)
    population[i]=initial_pos              
#print (population)


def crossover(parent1,parent2):
    child=[]
    m=3
    n=6
    for i in range(m,n):
        child.append(parent1[i])
            
    for i in range(n,len(parent2)):
        if (parent2[i] not in child):
            child.append(parent2[i])

    child1=[]
    for i in range(0,len(parent2)):
        if (parent2[i] not in child):
            if (len(child) >= 5):
                child1.append(parent2[i])
            else:
                child.append(parent2[i])
    child=child1+child
    return child

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

sol_count=0
for run in range(100):
    result=[]
    var=1
    for s in range(50):
        result_child=[]
        ran_parents_index=[]
        for i in range(1,101):
            ran_parents_index.append(i)
        #print (ran_parents_index)

        ol=random.choice(ran_parents_index)
        indices=[ol]
        ran_parents_index.remove(ol)
        ol=random.choice(ran_parents_index)
        indices.append(ol)
        #print (indices)

        parent1=population[indices[0]]
        #print (parent1)
        parent2=population[indices[1]]
        #print (parent2)

        result_child=crossover(parent1,parent2)
        #print (result_child)

        result.append(result_child)
            
        heu=heuristic(result_child)
        #print (heu)
        if heu==0:
            print ("solution")
            print (result_child)
            sol_count+=1
        else:
            other[var]=result_child
            var+=1

    a=len(other)
    
    for u in range(a+1,101):
        ran_unique=[0,1,2,3,4,5,6,7]
        old=random.choice(ran_unique)
        initial_pos=[old]
        ran_unique.remove(old)
        for j in range(0,n-1):
            new=random.choice(ran_unique)
            ran_unique.remove(new)
            initial_pos.append(new)
        other[u]=initial_pos

    population=copy.copy(other)
    #print (population)
    other.clear()
print (sol_count)
        

    
# develope b+c population again
            
    


