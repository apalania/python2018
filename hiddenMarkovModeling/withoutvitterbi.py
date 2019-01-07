
#import numpy as num
from random import *
file=open("x.txt","w")

emmat=raw_input("enter values of emission matrix :AT RICH ROW")

file.write(emmat)
file=open("x.txt","r")
c=file.read()
cl=c.split()
ik=[] 

for i in range(4):
   ik.append(float(cl[i]))
print ik

   

emmat=raw_input("enter values of emission matrix :GC RICH ROW")
file=open("y.txt","w")
file.write(emmat)
file=open("y.txt","r")
c=file.read()
cl=c.split()
ib=[] 

for i in range(4):
   ib.append(float(cl[i]))
print ib

trmat=raw_input("enter values of transition matrix 1st row")
file=open("o.txt","w")
file.write(trmat)
file=open("o.txt","r")
c=file.read()
cl=c.split()
tb=[] 
for i in range(2):
   tb.append(float(cl[i]))
print tb

trmat=raw_input("enter values of transition matrix 2nd row")
file=open("g.txt","w")
file.write(trmat)
file=open("g.txt","r")
c=file.read()
cl=c.split()
tb2=[] 
for i in range(2):
   tb2.append(float(cl[i]))
print tb2

#option=raw_input("enter 'a' for 1st emission matrix and 'b' for second")
seq=[]
initprob=raw_input("enter initial probabilities probability of 1st nucleotide to be ACrich/GCrich")
initprob2=initprob.split()
initprob3=[]
for x in initprob2:
   initprob3.append(float(x))

y=random()
if y<initprob3[0]:
   state="AT-rich"
if y>initprob3[0] and y<initprob3[0]+initprob3[1]:
   state="GC-rich"
x=random()

if state=="AT-rich":  
   if x<ik[0]:
      seq.append('A')
   if x>ik[0] and x<(ik[0]+ik[1]):
      seq.append('T')
   if x>(ik[0]+ik[1]) and x<(ik[0]+ik[1]+ik[2]):
      seq.append('G')
   if x>(ik[0]+ik[1]+ik[2]) and x<(ik[0]+ik[1]+ik[2]+ik[3]):
      seq.append('C')
if state=="GC-rich":  
   if x<ib[0]:
      seq.append('A')
   if x>ib[0] and x<(ib[0]+ib[1]):
      seq.append('T')
   if x>(ib[0]+ib[1]) and x<(ib[0]+ib[1]+ib[2]):
      seq.append('G')
   if x>(ib[0]+ib[1]+ib[2]) and x<(ib[0]+ib[1]+ib[2]+ib[3]):
      seq.append('C')
   
   
for i in range(100):
       
   x=random()
   y=random()
   #choose current state ATrich/GCrich from previous state
   if state=="AT-rich": 
     if y<tb[0]:
         state="AT-rich"
     if y<(tb[0]+tb[1]):
         state="GC-rich"   
   if state=="GC-rich": 
     if y<tb2[0]:
         state="AT-rich"
     if y<(tb2[0]+tb[1]):
         state="GC-rich"            
      
   if state=="AT-rich":
     if x<ik[0]:
         seq.append('A')
     if x>ik[0] and x<(ik[0]+ik[1]):
         seq.append('T')
     if x>(ik[0]+ik[1]) and x<(ik[0]+ik[1]+ik[2]):
         seq.append('G')
     if x>(ik[0]+ik[1]+ik[2]) and x<(ik[0]+ik[1]+ik[2]+ik[3]):
         seq.append('C')       
   if state=="GC-rich":  
     if x<ib[0]:
         seq.append('A')
     if x>ib[0] and x<(ib[0]+ib[1]):
         seq.append('T')
     if x>(ib[0]+ib[1]) and x<(ib[0]+ib[1]+ib[2]):
         seq.append('G')
     if x>(ib[0]+ib[1]+ib[2]) and x<(ib[0]+ib[1]+ib[2]+ib[3]):
         seq.append('C') 

print seq

