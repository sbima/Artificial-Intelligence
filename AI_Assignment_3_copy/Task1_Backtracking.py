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

dependencies={1:[2,3],2:[1,4,7,8],3:[1,4,7,8],4:[2,5],5:[4,7,8],6:[8],7:[3,5],8:[6]}

depend_pos1={1:{3:2,5:3},2:{3:4,4:7,5:8},3:{1:1,3:4,4:7,5:8},4:{2:2,3:5},
             5:{1:4,2:7,3:8},6:{2:8},7:{3:3,2:5},8:{1:6}
            }

depend_pos2={1:{2:1,3:1},2:{4:2,7:1,8:3},3:{1:5,4:4,7:3,8:5},4:{2:3,5:1},
             5:{4:3,7:2,8:4},6:{8:1},7:{3:4,5:2},8:{6:2}
            }

wordlist=['HOSES','LASER','SAILS','SHEET','STEER','HEEL','HIKE','KEEL','KNOT',
          'LINE','AFT','ALE','EEL','LEE','TIE']

def only_letters(words):
	for i in range(0,len(words)):
		for j in range(0,len(words[i])):
			sys.stdout.write(words[i][j])
			sys.stdout.write(' ')
		sys.stdout.write(',')	

#only_letters(wordlist)
#print (letters)

##for i in depend_pos1:
##    for j in depend_pos1[i]:
##        #print (j)                     #3,5  3,4,5  ......
##        #print (depend_pos1[i][j])     #2,3  4,7,8  ......
##        var=depend_pos1[i][j]
##        #print (depend_pos2[i][var])   #1,1  2,1,3  ......
        
##for i in words_dic:
##    for j in words_dic[i]:
##        match=[j]
##        #print (match)                   #HOSES, LASER, ....      
##        for k in depend_pos1[i]:
##                #print (k)                  #3,5  3,4,5 ...#only key values of dictionary
##                dependency1=depend_pos1[i][k]
##                #print (dependency1)                     #2,3   4,7,8   1,4,7,8....
##                #print (depend_pos2[i][dependency1])      #1,1   2,1,3.....
##                dependency2=depend_pos2[i][dependency1]
##    #print (dependency2)
##                #print (j)
##        #print ()


for i in range(1,2):
        #print (words_dic[i])                   #['HOSES', 'LASER', 'SAILS', 'SHEET', 'STEER']
        for j in range(0,1):
                #print (words_dic[i][j])        #HOSES
                firstword = words_dic[i][j]          #  first word *****
                chars = []
                for singleletter in words_dic[i][j]:
                        chars.extend(singleletter)
                #print (chars)                  #['H', 'O', 'S', 'E', 'S']
                #print (words_dic[2])           #['HOSES', 'LASER', 'SAILS', 'SHEET', 'STEER']
                midanswer2=[]
                for some in words_dic[2]:
                        #print (some)            #HOSES, LASER, SAILS, SHEET, STEER
                        if (chars[2] == some[0]):
                                #print (chars[2])        # S
                                #print (some)            # SAILS, SHEET, STEER
                                midanswer2.append(some)
                #print (midanswer2)                       # ['SAILS', 'SHEET', 'STEER']
                                
                                #midanswer2 is second word possibilities **********
                secondword = midanswer2[0]     #SAILS
                second = list(secondword)      #['S', 'A', 'I', 'L', 'S']
                
                newdic3 = copy.copy(words_dic[3])
                newdic3.remove(firstword)
                newdic3.remove(secondword)
                #print (newdic3)                #['LASER', 'SHEET', 'STEER']
                #print (words_dic[3])            #['HOSES', 'LASER', 'SAILS', 'SHEET', 'STEER']
                #print (chars[2])               #S
                midanswer3=[]
                for some in newdic3:
                        if (chars[2] == some[0]):
                                midanswer3.append(some)
                #print (midanswer3)              #['SHEET', 'STEER'] excluding hoses & sails

                                #midanswer3 is third word possibilities **********
                thirdword=midanswer3[1]       #STEER
                third = list(thirdword)       #['S', 'T', 'E', 'E', 'R']

                #print (words_dic[4])            #['HEEL', 'HIKE', 'KEEL', 'KNOT', 'LINE']
                midanswer4=[]
                for some in words_dic[4]:
                        if (second[2] == some[1] and third[2] == some[3]):
                                midanswer4.append(some)
                #print (midanswer4)              #['HIKE', 'LINE']

                                #midanswer4 is fourth word possibilities **********
                fourthword = midanswer4[0]
                fourth = list(fourthword)       #['H', 'I', 'K', 'E']
                
                newdic5 = copy.copy(words_dic[5])
                newdic5.remove(fourthword)      #['HEEL', 'KEEL', 'KNOT', 'LINE']
                midanswer5=[]
                for some in newdic5:
                        if (fourth[2] == some[0]):
                                midanswer5.append(some)
                #print (midanswer5)             #['KEEL', 'KNOT']

                                #midanswer5 is fifth word possibilities **********
                fifthword = midanswer5[0]
                print (list(fifthword))         #['K', 'E', 'E', 'L']

                newdic
                

                
                                
                                
                
                        
                        
                        

                

                

                
                                
                                
                                
                                
                                
                                
                        
                
                
                
                        
                
        
                

        
        

