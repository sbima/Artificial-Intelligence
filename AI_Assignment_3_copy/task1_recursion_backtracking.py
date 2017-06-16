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

words_dic={1:['HOSES','LASER','SAILS','SHEET','STEER'],
           2:['HOSES','LASER','SAILS','SHEET','STEER'],
           3:['HOSES','LASER','SAILS','SHEET','STEER'],          
           4:['HEEL','HIKE','KEEL','KNOT','LINE'],
           5:['HEEL','HIKE','KEEL','KNOT','LINE'],
           6:['AFT','ALE','EEL','LEE','TIE'],         
           7:['AFT','ALE','EEL','LEE','TIE'],
           8:['HOSES','LASER','SAILS','SHEET','STEER']               
          }

dependencies={1:[2,3],2:[1,4,7,8],3:[1,4,7,8],4:[2,5,3],5:[4,7,8],6:[8],7:[2,5,3],8:[6,2,5,3]}

depend_pos1={1:{3:2,5:3},2:{1:1,3:4,4:7,5:8},3:{1:1,3:4,4:7,5:8},4:{2:2,3:5,4:3},
             5:{1:4,2:7,3:8},6:{2:8},7:{1:2,2:5,3:3},8:{1:6,3:2,4:5,5:3}
            }

depend_pos2={1:{2:1,3:1},2:{1:3,4:2,7:1,8:3},3:{1:5,4:4,7:3,8:5},4:{2:3,5:1,3:3},
             5:{4:3,7:2,8:4},6:{8:1},7:{2:4,5:2,3:4},8:{6:2,2:5,5:3,3:5}
            }

wordlist=['HOSES','LASER','SAILS','SHEET','STEER','HEEL','HIKE','KEEL','KNOT',
          'LINE','AFT','ALE','EEL','LEE','TIE']

def only_letters(words):
	for i in range(0,len(words)):
		for j in range(0,len(words[i])):
			sys.stdout.write(words[i][j])
			sys.stdout.write(' ')
		sys.stdout.write(',')

#print (only_letters(words_dic[1][0]))
#print (list(words_dic[1][0]))

grid = [[1,0,2,0,3],
        ['-','-',0,'-',0],
        ['-',4,0,5,0],
        [6,'-',7,0,0],
        [8,0,0,0,0],
        [0,'-','-',0,'-']]

def find_dependency(number):
        depend_dict = {}
        depend_dict = depend_pos1[number]
        for pos in dependencies[number]:
                print ("dependencies")
                print (pos)
                pos_dependent_at = list(depend_dict.keys())[list(depend_dict.values()).index(pos)]  #get key if we have value
                print ("dependent of "+ str(number)+ " at following position")
                print (pos_dependent_at)
                print ("dependency starts at")
                pos_starts_at = depend_pos2[number][pos]
                print (pos_starts_at)

                
                
        return pos, pos_dependent_at, pos_starts_at
            


def check_dependency(number,word):
        

        
def crossword(wordsdic):
        match = []
        solution = {}
        for i in wordsdic:       #1
                for j in wordsdic[i]:
                        #print (j)               #HOSES
                        find_dependency(i)
                        check_dependency(i,j)

##            if (find_dependency(i,j)):
##                match.append(j)
##                print (match)
                    
                

#crossword(words_dic)
find_dependency(1)

        





        

