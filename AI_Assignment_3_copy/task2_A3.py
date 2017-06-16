import sys
import copy

across_down={'a':[1,4,7,8], 'd':[2,3,5,6]}

across_down2={1:'a',4:'a',7:'a',8:'a',2:'d',3:'d',5:'d',6:'d'}

words_dict={'a':{1:['HOSES','LASER','SAILS','SHEET','STEER'],
                 4:['HEEL','HIKE','KEEL','KNOT','LINE'],
                 7:['AFT','ALE','EEL','LEE','TIE'],
                 8:['HOSES','LASER','SAILS','SHEET','STEER']},
            'd':{2:['HOSES','LASER','SAILS','SHEET','STEER'],
                 3:['HOSES','LASER','SAILS','SHEET','STEER'],
                 5:['HEEL','HIKE','KEEL','KNOT','LINE'],
                 6:['AFT','ALE','EEL','LEE','TIE']}
            }

wordlist=['HOSES','LASER','SAILS','SHEET','STEER','HEEL','HIKE','KEEL','KNOT',
          'LINE','AFT','ALE','EEL','LEE','TIE']

def only_letters(words):
	for i in range(0,len(words)):
		for j in range(0,len(words[i])):
			sys.stdout.write(words[i][j])
			sys.stdout.write(' ')
		sys.stdout.write(',')

##print (only_letters('HOSES'))
##print (list('HOSES'))

words_dic={1:['HOSES','LASER','SAILS','SHEET','STEER'],
           2:['HOSES','LASER','SAILS','SHEET','STEER'],
           3:['HOSES','LASER','SAILS','SHEET','STEER'],          
           4:['HEEL','HIKE','KEEL','KNOT'],
           5:['HEEL','HIKE','KEEL','KNOT'],
           6:['AFT','ALE','LEE'],         
           7:['AFT','ALE','LEE'],
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

min_value = min(words_dic.values())             #['AFT', 'ALE', 'LEE']

result = [key for key, value in words_dic.iteritems() if value == min_value]  #[6, 7]
  
num = min(result)        
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
        print number
        if (number == 9):
                return True
        global words_dic
        print 'here'
        print words_dic
        words_dic_cop = copy.deepcopy(words_dic)
        for i in words_dic_cop[number]:
                print i
                depend_dict = {}
                depend_dict = depend_pos1[number]
                count = 0
                words_dic_copy = copy.deepcopy(words_dic)
                for x in length[len(i)]:
                        words_dic[x].remove(i) # removes hoses in task 1 (in 1st call to crossword)
                
                print words_dic
                
                words_dicy = copy.deepcopy(words_dic)
                
                for dependent in dependencies[number]:
                        #print ("dependencies")
                        print (dependent)
                        dependent_dependent_at = list(depend_dict.keys())[list(depend_dict.values()).index(dependent)]  #get key if we have value
                        #print ("dependent of "+ str(number)+ " at following position")
                        print (dependent_dependent_at)
                        #print ("dependency starts at")
                        dependent_starts_at = depend_pos2[number][dependent]
                        print (dependent_starts_at)

                        if dependent in solution:
                                print 'depen'
                                #print (dependent)
                                if (solution[dependent][dependent_starts_at-1]==i[dependent_dependent_at-1]):
                                        count+=1
                        else:
                                for s in words_dic[dependent]:
                                    if (s[dependent_starts_at-1]==i[dependent_dependent_at-1]):
                                        count+=1
                                        break
                                            
                #print ('count is ' + str(count))                                       
                if(count == len(dependencies[number])):
                        print 'hello'
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
                        

if(crossword(num)):
        print (solution)


        





        

