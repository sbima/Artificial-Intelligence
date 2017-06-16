import sys
import copy
import time 

start_time = time.time()

with open('wordsfile.txt', 'r') as f:
    data = f.read().splitlines()

    words_dic = {}

    for number in range(3,9):
        group = []
        for line in data:
            if(len(line)==number):
                group.append(line)
                words_dic[number]=group
    #print (group_dict)

length = {8:[8], 7:[7], 6:[6], 5:[5], 4:[4], 3:[3]}

dependencies={3:[4,7,8],4:[5,3],5:[4,7,8],6:[8],7:[5,3],8:[6,5,3]}

depend_pos1={3:{3:4,4:7,5:8},4:{3:5,4:3},
             5:{1:4,2:7,3:8},6:{2:8},7:{2:5,3:3},8:{1:6,4:5,5:3}
            }

depend_pos2={3:{4:4,7:3,8:5},4:{5:1,3:3},
             5:{4:3,7:2,8:4},6:{8:1},7:{5:2,3:4},8:{6:2,5:3,3:5}
            }
    
min_value = min(words_dic.values())             #['AFT', 'ALE', 'LEE']

result = [key for key, value in words_dic.iteritems() if value == min_value]  #[6, 7]
  
num = min(result)  
nu = 3      
solution = {}

def forwardcheck(number,words_dicy,i):
    global words_dic
    print 'forward'
    depend_dict = {}
    depend_dict = depend_pos1[number]
    for dependent in dependencies[number]:

        dependent_dependent_at = list(depend_dict.keys())[list(depend_dict.values()).index(dependent)]
        
        dependent_starts_at = depend_pos2[number][dependent]
        
        for dep in words_dicy[dependent]:
            print dep
            if (dep[dependent_starts_at-1] != i[dependent_dependent_at-1]):
                words_dic[dependent].remove(dep)
        
#        if (solution[number] == i):
#            break                              
    print words_dic 
    return words_dic
    
def crossword(number):
        if (number == 9):
                return True
        global words_dic
        words_dic_cop = copy.deepcopy(words_dic)
        for i in words_dic_cop[number]:
                depend_dict = {}
                depend_dict = depend_pos1[number]
                count = 0
                words_dic_copy = copy.deepcopy(words_dic)
                for x in length[len(i)]:
                        words_dic[x].remove(i)
                #print ("number")
                #print (number)
                #print (i)
                #print (words_dic)
                for dependent in dependencies[number]:
                        #print ("dependencies")
                        #print (dependent)
                        dependent_dependent_at = list(depend_dict.keys())[list(depend_dict.values()).index(dependent)]  #get key if we have value
                        #print ("dependent of "+ str(number)+ " at following position")
                        #print (dependent_dependent_at)
                        #print ("dependency starts at")
                        dependent_starts_at = depend_pos2[number][dependent]
                        #print (dependent_starts_at)

                        if dependent in solution:
                                #print (dependent)
                                if (solution[dependent][dependent_starts_at-1]==i[dependent_dependent_at-1]):
                                        count+=1
                        else:
                                for s in words_dic[dependent]:
                                        if (s[dependent_starts_at-1]==i[dependent_dependent_at-1]):
                                                count+=1
                                                break
                
                if(count == len(dependencies[number])):
                        solution[number] = i
                        print solution
                        words_dic = forwardcheck(number,words_dicy,i)
                        #print words_dic
                        #break
                        #return True
                        len_dic={}
                        for keyss in words_dic:
                            len_dic[keyss]=len(words_dic[keyss])    #{1: 5, 2: 5, 3: 5, 4: 4, 5: 4, 6: 2, 7: 2, 8: 1}
                        print len_dic
                        
                        res = min(len_dic, key=len_dic.get)
                        print res
                        
                        if 0 not in len_dic.values():
                            if(crossword(res)):
                                    return True
                            else:
                                    words_dic = copy.deepcopy(words_dic_copy)
                                    del solution[number]
                                
                else:
                        words_dic = copy.deepcopy(words_dic_copy)


                

        return False
                        
                               
                        
                        #check_dependency(number,dependent,dependent_dependent_at,dependent_starts_at)

if(crossword(nu)):
        print (solution)

print("--- %s seconds ---" % (time.time() - start_time))

