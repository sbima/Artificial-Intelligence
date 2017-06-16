import sys
import copy
import time

start_time = time.time()

words_dic={1:['HOSES','LASER','SAILS','SHEET','STEER'],
           2:['HOSES','LASER','SAILS','SHEET','STEER'],
           3:['HOSES','LASER','SAILS','SHEET','STEER'],          
           4:['HEEL','HIKE','KEEL','KNOT','LINE'],
           5:['HEEL','HIKE','KEEL','KNOT','LINE'],
           6:['AFT','ALE','EEL','LEE','TIE'],         
           7:['AFT','ALE','EEL','LEE','TIE'],
           8:['HOSES','LASER','SAILS','SHEET','STEER']               
          }

length = {5:[1,2,3,8],4:[4,5],3:[6,7]}

dependencies={1:[2,3],2:[1,4,7,8],3:[1,4,7,8],4:[2,5,3],5:[4,7,8],6:[8],7:[2,5,3],8:[6,2,5,3]}

depend_pos1={1:{3:2,5:3},2:{1:1,3:4,4:7,5:8},3:{1:1,3:4,4:7,5:8},4:{2:2,3:5,4:3},
             5:{1:4,2:7,3:8},6:{2:8},7:{1:2,2:5,3:3},8:{1:6,3:2,4:5,5:3}
            }

depend_pos2={1:{2:1,3:1},2:{1:3,4:2,7:1,8:3},3:{1:5,4:4,7:3,8:5},4:{2:3,5:1,3:3},
             5:{4:3,7:2,8:4},6:{8:1},7:{2:4,5:2,3:4},8:{6:2,2:5,5:3,3:5}
            }
        
num = 1       
solution = {}
        
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
                                if (solution[dependent][dependent_starts_at-1]==i[dependent_dependent_at-1]):
                                        count+=1
                        else:
                                for s in words_dic[dependent]:
                                        if (s[dependent_starts_at-1]==i[dependent_dependent_at-1]):
                                                count+=1
                                                break
                
                if(count == len(dependencies[number])):
                        solution[number] = i
                        if(crossword(number+1)):
                                return True
                        else:
                                words_dic = copy.deepcopy(words_dic_copy)
                                del solution[number]
                                                                                                
                                
                else:
                        words_dic = copy.deepcopy(words_dic_copy)

                

        return False
                        
                               
                        
                        #check_dependency(number,dependent,dependent_dependent_at,dependent_starts_at)

if(crossword(num)):
        print (solution)

print("--- %s seconds ---" % (time.time() - start_time))


 





        

