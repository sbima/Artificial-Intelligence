#encoding = utfs
import math
import random
file = open("newfile.txt", "w")

for i in range(0,100):
    x=random.uniform(-5,5)
    y=random.uniform(-5,5)
    #print (x,y)
    new_f=(-20)*math.exp((-0.2)*math.sqrt(0.5*((x**2)+(y**2))))-math.exp(0.5*(math.cos(2*math.pi*x)+math.cos(2*math.pi*y)))
    for i in range(0,100):
        f=new_f
        bakup_x=x
        bakup_y=y
        new_x=(random.uniform(0,1)-0.5)*0.1+x
        new_y=(random.uniform(0,1)-0.5)*0.1+y
        x=new_x
        y=new_y
        new_f=(-20)*math.exp((-0.2)*math.sqrt(0.5*((x**2)+(y**2))))-math.exp(0.5*(math.cos(2*math.pi*x)+math.cos(2*math.pi*y)))
        #print (new_x, new_y)
        if new_f > f:
            #print (i)
            file.write(str(f))
            file.write("\t")
            file.write(str(bakup_x))
            file.write("\t")
            file.write(str(bakup_y))
            file.write("\n")
            break

file.close()




