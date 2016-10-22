import random
import time



x = int(input("Enter the number of nodes: "))
print ("no of nodes   ", x)
Matrix = [[0 for i in range(x)] for j in range(x)]
for i in range(x):
    for j in range(x):
        if(i==j):
            Matrix[i][j]=0
        else:
            if(i>j):
                m = int(random.randint(0,1))
                Matrix[i][j]=m
                Matrix[j][i]=m
                
fo = open("rgraph.txt", "w")
for i in range(x):
    for j in range(x):
        fo.write(str(Matrix[i][j]))
        fo.write(" ")
    fo.write("\n")