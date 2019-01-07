from pyDOE import pbdesign
import math
 
#for arranging F values in increasing order
def BubbleSort(Fval):
    sort=Fval
    n = len(sort)
    #corresponding to every element in the array
    for i in range(n):
        for j in range(0, n-i-1):
            if (sort[j] > sort[j+1]): # swapping if the element is greater than next element
                sort[j]= sort[j+1]
                sort[j+1]=sort[j]
    return sort       

n=int(raw_input("Enter the number of parameters:"))
matrix=pbdesign(n)
print "Each column corresponds to a parameter ranging from A to Z, and then A1 to Z1 and so on"
print matrix
print "Enter the number of dummy variables:"
dum_num=int(raw_input())
dum_pos=[]
num=0
for j in range(0,dum_num):
    print "Enter the position of dummy variable:"
    num=int(raw_input())
    dum_pos.append(num-1)

#accept the response values corresponding to each experimental trial
res=[]
for i in range(0,n+1):
    print "The yield for the",i+1,"th trial:"
    val=float(raw_input())
    res.append(val)

#list of all differences for each parameter
difference=[] 
for column in range(0,n):
    sum=0.0
    for row in range(0,n+1):
        sum+=(matrix[row][column])*res[row]
    difference.append(sum)

print "Difference b/w high and low values:",difference

#variance
Mean_sqr=[]  
for val in difference:
    MS=(math.pow(val,2))/(n+1)
    Mean_sqr.append(MS)
MSE=0.0
Mean=0.0
#determination of mean square error
for i in range(0,dum_num):
    Mean+=Mean_sqr[dum_pos[i]]
MSE=Mean/len(dum_pos)

print "Variance:",Mean_sqr
print "Mean square error:",MSE

#F test value for each parameter
F_value=[]
for i in range(0,n):
    F_value.append(Mean_sqr[i]/MSE)  
print "F value for the given set of parameters:",F_value

dict={}
for char,val in [A-Z],F_value:  #corresponding to the given parameters
    dict={char:val}

print dict  #dictionary mapping the varibales to their corresponding F values
    

print "Order of significance of the parameter on the system:",BubbleSort(dict.values())


        




                
    


