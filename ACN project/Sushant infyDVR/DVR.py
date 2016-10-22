from copy import deepcopy,copy
import random 
import time
from graphviz import Graph
dot = Graph(comment='The Round Table',format='png')


count =0
fo = open("rgraph.txt", "r")
data = []
for line in fo:
    number_strings = line.split() # Split the line on runs of whitespace
    numbers = [str(n) for n in number_strings] # Convert to integers
    data.append(numbers) # Add the "row" to your list.
print(data)


length=len(data)
print(length)
x=length


Matrix = [[0 for i in range(x)] for j in range(x)] 
for i in range(x): 
    for j in range(x):
        Matrix[i][j] = int(data[i][j])
        
        
                
for i in range(x):
    for j in range(x):
        if(Matrix[i][j]>0 and i>j): 
            count=count+1 

edge=[[0 for k in range(3)]for l in range(count)] 
n=0
for i in range(x): 
    for j in range(x): 
        if(Matrix[i][j]>0 and i>j):
            edge[n][0]=Matrix[i][j]
            edge[n][1]=i
            edge[n][2]=j
            n+=1


for i in range(count):
    for j in range(3):
        print (edge[i][j],)


nodes=n 
##IMPLEMENTING DVR(START)

Matrix_new = [[0 for i in range(x)] for j in range(x)]
via = [[0 for i in range(x)] for j in range(x)]

Matrix_new = deepcopy(Matrix)

nodes=x
for i in range (nodes) :
    for j in range (nodes):
        if(Matrix[i][j] == 0 and i!=j):
            Matrix_new[i][j] =9999

for i in range (nodes) :
    for j in range (nodes):
        if(Matrix[i][j] != 0): 
            for k in range (nodes):
                if((Matrix_new[i][j] + Matrix_new[j][k]) < Matrix_new[i][k]):
                    Matrix_new[i][k] = Matrix_new[i][j] + Matrix_new[j][k]
                    via[i][k] = j 
                    via[k][i] = j        

##IMPLEMENTING DVR(END)

##OUTPUT OF DVR TABLES (START)
print('FIRST TIME IMPLEMENTATION OF DVR')
for i in range (x):
    print(str(chr(i+65))+'s table',end=' ')
    for j in range (x):
        print(Matrix_new[i][j],end=' ')
    print()
    print()
##OUTPUT OF DVR TABLES (END)

##OUTPUT IN FORM OF GRAPH (START)
dot
for i in range(x):
    dot.node(str(i+x), label=str(chr(i+65)))
for i in range(x):
    for j in range(x):
        if(Matrix[i][j]==0):
            continue
        else:
            if(i<j and Matrix[i][j]>0):
                dot.edge(str(i+x),str(j+x),label=str(Matrix[i][j]))
dot.render('test-output/DVR.png', view=True)
##OUTPUT IN FORM OF GRAPH (END)

##REMOVING A NODE (START)
rem=0
print("Enter the node to be removed eg:input 0 if A ,1 if B....&so on") #removing a node 
rem = int(input().strip())
for i in range (x):
    if(Matrix[rem][i]==1):#removed node table 
        Matrix_new[i][rem]=9999
        Matrix_new[rem][i]=9999
    Matrix[rem][i]=0     
for i in range (x):
    Matrix[i][rem]=0 
    Matrix_new[rem][i]=9999
print('DVR TABLES AFTER REMOVING A NODE')    
for i in range (x):
    print(str(chr(i+65))+'s table',end=' ')
    for j in range (x):
        if(Matrix_new[i][j]>=9999):
            print('INF',end=' ')
        else:
            print(Matrix_new[i][j],end=' ')
    print()
    print()


edge_n=[[0 for k in range(3)]for l in range(count)]

m=0   
for i in range(x):
    for j in range(x): 
        if(Matrix[i][j]>0 and i>j):
            edge_n[m][0]=Matrix[i][j]
            edge_n[m][1]=i
            edge_n[m][2]=j
            m+=1


for i in range(x):
    dot.node(str(i), label=str(chr(i+65)))

for i in range(n):
    if(edge_n[i][0]>0):
        dot.edge(str(edge_n[i][1]),str(edge_n[i][2]),label=str(edge_n[i][0]))
    
dot.render('test-output/DVR.png', view=True)
           

##REMOVING A NODE (END)

##SHOWING COUNT TO INFINITY(START)
print('DVR TABLES SHOWING COUNT TO INFINITY PROBLEM')    
Matrix_new_1 = [[0 for i in range(x)] for j in range(x)]
Matrix_new_2 = [[9999 for i in range(x)] for j in range(x)]
Matrix_new_1 = deepcopy(Matrix_new)
Matrix_new_2 = deepcopy(Matrix_new)
Matrix_new_3 = [[0 for i in range(x)] for j in range(x)]
Matrix_new_3 = deepcopy(Matrix_new)
via_1 = [[0 for i in range(x)] for j in range(x)]
via_1 =deepcopy(via)
via_2 = [[0 for i in range(x)] for j in range(x)]
via_2 =deepcopy(via)
via_3 = [[0 for i in range(x)] for j in range(x)]
via_3 =deepcopy(via)

for l in range(0,15):  
    for i in range(x):
        
        for j in range (x):
            
            if(Matrix[i][j]==1): 
                print(str(chr(j+65))+'s table',end=' ')
                for k in range (x):
                    
                    
                    if(((Matrix_new_1[i][j] + Matrix_new_1[i][k]) < Matrix_new_1[j][k])):
                        Matrix_new_1[j][k] = Matrix_new_1[i][j] + Matrix_new_1[i][k]
                    else:
                        if((via_1[i][k]==j or via_1[j][k]==i) and k==rem and Matrix_new_1[i][k]<9999):
                            Matrix_new_1[j][k] = Matrix_new_1[i][j] + Matrix_new_1[i][k] 
                    via_1[j][k]=i
                    via_1[k][j]=i
                    if(Matrix_new_1[j][k]>=9999):
                        print('INF',end=' ')
                    else:
                        print(Matrix_new_1[j][k],end=' ') 
                print()
                print()   
#COUNT TO INFINITY FINISHED
          
#USING SPLIT HORIZON METHOD
print('DVR TABLES USING SPLIT HORIZON METHOD')    
for l in range(0,15):  
    for i in range(x):
        
        for j in range (x):
            
            if(Matrix[i][j]==1): 
                print(str(chr(j+65))+'s table',end=' ')
                for k in range (x): 
                    
                    if(( via_2[j][k]==i or via_2[i][k]==j )):
                        counter=0
                    else:
                        if(((Matrix_new_2[i][j] + Matrix_new_2[i][k]) < Matrix_new_2[j][k])): 
                            Matrix_new_2[j][k] = Matrix_new_2[i][j] + Matrix_new_2[i][k] 
                    
                    via_2[j][k]=i
                    via_2[k][j]=i
                    if(Matrix_new_2[j][k]>=9999):
                        print('INF',end=' ')
                    else:
                        print(Matrix_new_2[j][k],end=' ') 
                print()
                print()   
#USING SPLIT HORIZON METHOD WITH POISSON REVERSE    
print('DVR TABLES USING SPLIT HORIZON WITH POISSON REVERSE')    
for l in range(0,15):  
    for i in range(x):
        
        for j in range (x):
            
            if(Matrix[i][j]==1): 
                print(str(chr(j+65))+'s table',end=' ')
                for k in range (x):
                    
                    if(( via_2[j][k]==i and Matrix_new_3[j][k]==9999 )or (via_2[i][k]==j and Matrix_new_3[i][k]==9999)):
                        Matrix_new_3[j][k]=9999
                    else:
                        if( k==rem and Matrix_new_1[i][k]<9999):
                            Matrix_new_1[j][k] = Matrix_new_1[i][j] + Matrix_new_1[i][k] 
                    via_3[j][k]=i
                    via_3[k][j]=i
                    if(Matrix_new_3[j][k]>=9999):
                        print('INF',end=' ')
                    else:
                        print(Matrix_new_3[j][k],end=' ') 
                print()
                print()   
