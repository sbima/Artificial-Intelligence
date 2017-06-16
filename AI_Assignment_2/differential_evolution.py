import math
import random
import copy

np=20     #population size is 10 times the number of parameters(dimensions)
nc=100    #number of cycles- last 100 steps
F=0.8     #recommended differential weight
cr=0.1    #crossover probability
for i in range(100):
    X=Xnew=[]
    Y=Ynew=[]
    Z=[]

    def ackley(x,y):
        f=(-20)*math.exp((-0.2)*math.sqrt(0.5*((x**2)+(y**2))))-math.exp(0.5*(math.cos(2*math.pi*x)+math.cos(2*math.pi*y)))
        return f
        
    for i in range(np):
        x=random.uniform(-5,5)
        X.append(x)
        y=random.uniform(-5,5)
        Y.append(y)
    #print (X)
    #print (Y)

    for k in range(0,nc):
        Xnew=copy.copy(X)
        Ynew=copy.copy(Y)
        for i in range(0,np):
            ran_index=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
            old=random.choice(ran_index)
            h=[old]
            ran_index.remove(old)
            for j in range(2):
                new=random.choice(ran_index)
                ran_index.remove(new)
                h.append(new)
            #print (h)

            Vx=Xnew[h[0]]+F*(Xnew[h[1]]-Xnew[h[2]])
            Vy=Ynew[h[0]]+F*(Ynew[h[1]]-Ynew[h[2]])

            
            u=random.uniform(0,1)
            if u < cr:
                Ux=Vx
            else:
                #print("i is ", i)
                Ux=Xnew[i]

            u=random.uniform(0,1)
            if u < cr:
                Uy=Vy
            else:
                Uy=Ynew[i]

            Uf=ackley(Ux,Uy)
            Xf=ackley(Xnew[i],Ynew[i])

            if Uf < Xf:
                X[i]=Ux
                Y[i]=Uy
            else:
                X[i]=Xnew[i]
                Y[i]=Ynew[i]

    #print (X)
    #print (Y)

    for i in range(20):
        result=ackley(X[i],Y[i])
        #print (result)
        Z.append(result)

    resultant=min(Z)
    print (resultant)

