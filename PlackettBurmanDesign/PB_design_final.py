#Subhashree Bharathan
#Shwetha S
#Rachita K Kumar
from pyDOE import pbdesign
import math
import string

'''
To use the Plackett Burman design for the given input variables and find
the most influential variable.
'''

n=int(raw_input("Enter the number of parameters:"))
                
dummy_matrix=pbdesign(n)

if((len(dummy_matrix)-n)==1):
    n=n+4
    dum_num=4
else:
    dum_num=len(dummy_matrix)-n-1 #make up the number of parameters to one less than multiple of Four
    n=len(dummy_matrix)-1
matrix=pbdesign(n)

print matrix,"\n"

#accept the response values corresponding to each experimental trial
res=[]
for i in range(0,len(matrix)):
    print "The yield for the",i+1,"th trial:"
    val=float(raw_input())
    res.append(val)

#list of all differences for each parameter
difference=[] 
for column in range(0,n):
    sum=0.0
    for row in range(0,n+1):
        sum+=(matrix[row][column])*res[row]
    difference.append(round(sum,3))

print "Difference b/w high and low values:",difference,"\n"

#variance
Mean_sqr=[]  
for val in difference:
    MS=(math.pow(val,2))/(n+1)
    Mean_sqr.append(round(MS,3))
MSE=0.0
Mean=0.0
flag=0
#determination of mean square error
for i in range(0,dum_num):
    for j in range(dum_num,n):
        flag+=1
        Mean+=Mean_sqr[j]
    MSE=Mean/flag

print "Variance:",Mean_sqr,"\n"
print "Mean square error:",MSE,"\n"

#F test value for each parameter
F_value=[]
for i in range(0,n):
    fvalue=round(Mean_sqr[i]/MSE,3)
    F_value.append(fvalue)
print "F value for the given set of parameters:","\n"
final_list=zip(string.ascii_uppercase[:n],F_value)

#print "Each column corresponds to a parameter ranging from A,B,C,D and so on"
print final_list         

for para in final_list:
    if(para[1]==max(F_value)):
            print "Most significant parameter for the system is:",para,"\n"



        




                
    


