import csv
f1=open("of1.txt","a")
##It reads the quality score line from the file##
class qscore:
    def __init__(self, file):
            self.file = file
    def create_master_list(self):
      with(open(self.file,'r')) as f:
                for line in f.read().split("\n")[3::4]:
                    f1.write(line)
c=qscore(input("enter ur filename"))
c.create_master_list()
f2=open("of2.txt","a")
map={"!":"0",'"':"1","#":"2","$":"3","%":"4","&":"5","'":"6","(":"7",")":"8","*":"9","+":"10",",":"11","-":"12",".":"13","/":"14","0":"15","1":"16","2":"17","3":"18","4":"19","5":"20","6":"21","7":"22","8":"23","9":"24",":":"25",";":"26","<":"27","=":"28",">":"29","?":"30","@":"31","A":"32","B":"33","C":"34","D":"35","E":"36","F":"37","G":"38","H":"39","I":"40"}
##it calculates the quality score value##
class score(object):
  def __init__(self, file):
    self.file = file
  def create_master_list(self):
    with(open(self.file,'r')) as f:
                        for line in f.read():
                            a=map[line].split("\n")
                            f2.writelines(a)

c1 = score('of1.txt')
c1.create_master_list()
##it calculates the quality score range##
class minmax(object):
  def __init__(self, file):
    self.file = file
  def create_master_list(self):
    with(open(self.file,'r')) as f:
      line = f.readlines()
      print min(line)
      print max(line)
c2 = minmax('output1n.txt')
c2.create_master_list()
f3=open('of3.txt','a')
##it calculates the atgc percentage in the sequence file##
class perbaseseqcontent(object):
  def __init__(self, file):
    self.file = file
  def create_master_list(self):
    with(open("sra.fastq",'r')) as f:
      for line in f.read().split("\n")[1::4]:
        f3.write(line)
    with open(self.file, "r") as f:
      line=f.read()
      a=[]
      t=[]
      g=[]
      c=[]
      ct=[]
      i=len(line)
      ctr=0
      while ctr<i:
          seq=line[ctr:ctr+10]
          total=len(seq)
          aa=seq.count("A")
          tt=seq.count("T")
          gg=seq.count("G")
          cc=seq.count("c")
          a_cont=(float(aa)/total)*100
          t_cont=(float(tt)/total)*100
          g_cont=(float(gg)/total)*100
          c_cont=(float(cc)/total)*100
          ctr+=10
          a.append(int(a_cont))
          t.append(int(t_cont))
          g.append(int(g_cont))
          c.append(int(c_cont))
          ct.append(ctr)
          with open('o4.csv', 'w') as f:
              writer = csv.writer(f, delimiter='\t')
              writer.writerows(zip(a,t,g,c))
c3=perbaseseqcontent("pbsc.txt")
c3.create_master_list()
##Generating plots##
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv('C:/Python27/newtext.csv')
ax = plt.gca()
df.plot(kind='line',x='ct',y='a',ax=ax)
df.plot(kind='line',x='ct',y='t', color='red', ax=ax)
df.plot(kind='line',x='ct',y='g', color='green', ax=ax)
df.plot(kind='line',x='ct',y='c', color='brown', ax=ax)
plt.show()
##it calculates the gc percentage of the sequence in file##
class gc(object):
  def __init__(self, file):
    self.file = file
  def create_master_list(self):
    with open(self.file, "r") as f:
      line=f.read()
      gc=[]
      ct=[]
      i=len(line)
      ctr=0
      while ctr<i:
          seq=line[ctr:ctr+10]
          total=len(seq)
          gg=seq.count("G")
          cc=seq.count("c")
          gcc=gg+cc
          gc_cont=(float(gcc)/total)*100
          ctr+=10
          gc.append(int(gc_cont))
          ct.append(ctr)
          with open('o5.csv', 'w') as f:
              writer = csv.writer(f, delimiter='\t')
              writer.writerows(zip(gc,ct))

c3=gc("pbsc.txt")
c3.create_master_list()
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv('C:/Python27/gc.csv')
ax = plt.gca()
df.plot(kind='line',x='ct',y='gc',ax=ax)
plt.show()
##it calculates the n base percentage of the sequence in file##
class nbase(object):
  def __init__(self, file):
    self.file = file
  def create_master_list(self):
    with open(self.file, "r") as f:
      line=f.read()
      n=[]
      ct=[]
      i=len(line)
      ctr=0
      while ctr<i:
          seq=line[ctr:ctr+10]
          total=len(seq)
          nn=seq.count("N")
          n_cont=(float(nn)/total)*100
          ctr+=10
          n.append(int(n_cont))
          ct.append(ctr)
          with open('o5.csv', 'w') as f:
              writer = csv.writer(f, delimiter='\t')
              writer.writerows(zip(n,ct))

c3=nbase("pbsc.txt")
a1 = c3.create_master_list()
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv('C:/Python27/n.csv')
ax = plt.gca()
df.plot(kind='line',x='ct',y='n',ax=ax)
plt.show()
