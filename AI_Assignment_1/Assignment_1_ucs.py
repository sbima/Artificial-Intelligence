import sys
import copy
import time
from collections import defaultdict
from collections import deque


start_time = time.time()

d={}
print ("The following is the result for 3 people with the input (1,2,5,10) ")
print ("Please hard code the desired input values before you expect any results for different input other than (1,2,5,10) ")
d[1]=[1,2,5,10]                     ## Please hard code the appropriate input you desire to give  
t=d[1]
global node
node=1
parent={}
child={}
childparent={}
childparent[1]=[0]
cost={}
cost[1]=[0]
parent[1]=[1,2,5,10,'*']            ## Please hard code the same desired values once again which you have given above including the '*'


child = defaultdict(list)

def pairs(values):
    result=[]
    for i in range(len(values)):
        for j in range(i+1,len(values)):
            result.append([values[i],values[j]])
    return result

def stage1(arg1):
    b={}
    pair1=pairs(arg1)
    for j in pair1:
        r=list(set(arg1)-set(j))
        s=['*']
        a=r+s+j
        global node
        node+=1
        child[1].append(node)
        
        childparent[node]=1
        ##print (child)
        b[node]=a
        parent[node]=a
        cost[node]=max(j[0],j[1])

    return b 

def backfunc1(arg2):
    print("back function is executing")
    lis={}
    global node
    for i in arg2:

        val2=arg2[i]
        pos=val2.index('*')
        second=val2[pos+1:]
        for j in second:
            val3=copy.copy(val2)
            val3.remove(j)
            rem=[j]+val3
            global node
            node+=1
            parent[node]=rem
            
            lis[node]=rem
            child[i].append(node)
            childparent[node]=i
            cost[node]=j
##            print (cost)
##    

    frontfunc1(lis)


def frontfunc1(arg3):
    ##time.sleep(13)
    print ("front function is executing")
    new={}
    for i in arg3:
        val=arg3[i]
        
        global node
        pos=val.index('*')
        trim1=val[0:pos]
        trim2=val[pos:]
        pair=pairs(trim1)

            
        for j in pair:

            minused=list(set(trim1)-set(j))
            final=minused+trim2+j
            node+=1
            parent[node]=final

            new[node]=final
            child[i].append(node)
            ##print (child)

            childparent[node]=i
            cost[node]=max(j[0],j[1])
    
    # print ("cost dictionary")
    # print (cost)
    # print ("child dictionary")
    # print (child)
    # print ("child parent dictionary")
    # print (childparent)
        
    if final.index('*') != 0:
        backfunc1(new)

    return child, childparent
                                
	
def ucs():
	priority_queue =[]
	some_random = []
	storage_list=[]
	priority_queue_dictionary={}
	some_random=child[1]
	i=0
	for i in some_random:
		priority_queue_dictionary[i]=cost[i]
	
	sorted_values= sorted(priority_queue_dictionary.items(),key=lambda t:t[1])
	while True:
		new_values=sorted_values[0][0]
		del priority_queue_dictionary[new_values]
		for i in child[new_values]:
			
			priority_queue_dictionary[i]=cost[i]+sorted_values[0][1]
		sorted_values= sorted(priority_queue_dictionary.items(),key=lambda t:t[1])
		new_val=sorted_values[0][0]
		if(parent[new_val][0]=='*'):
			
			storage_list=[new_val]
			while True:
				z=childparent[new_val]
				storage_list.append(z)
				new_val=z
				if(new_val==1):
					break
			break
	length =len(storage_list)
	storage_list.reverse()
	sum=0
	for x in range (0,length):
		a=storage_list[x]
		if (x>0):
			v=cost[a]
			sum = sum + v
			print ("Level %s" % x)
		print(parent[a])
	print ("Total Time taken for the people to get to the other end is %s"%sum)
	

one = stage1(t)
#print("stage1")
backfunc1(one)
#print (parent)
ucs()
  
print("--- %s seconds ---" % (time.time() - start_time))