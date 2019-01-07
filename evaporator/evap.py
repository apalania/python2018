from __future__ import division
import numpy as np
#from pyXSteam.XSteam import XSteam
#steamTable=XSteam(XSteam.UNIT_SYSTEM_BARE)
class input_data:
    def __init__(self,F,Xf,X3,Tf,Tsat,T3,Cpf,U1,U2,U3,hfg3,Hs,hfg1=0,hfg2=0,T1=0,T2=0,A1=0,A2=0,A3=0,K=0,L=0):
        self.F=F
        self.Xf=Xf
        self.X3=X3
        self.Tf=Tf
        self.Tsat=Tsat
        self.T1=T1
        self.T2=T2
        self.T3=T3
        self.Cpf=Cpf
        self.U1=U1
        self.U2=U2
        self.U3=U3
        self.hfg1=hfg1
        self.hfg2=hfg2
        self.hfg3=hfg3
        self.Hs=Hs
        self.K=K
        self.L=L
    def find_constant(self):
        x=((1/self.U1)+(1/self.U2)+(1/self.U3))
        return (self.Tsat-self.T3)/x
    def find_temp(self):
        a=self.find_constant()
        self.T1=self.Tsat-((1/self.U1)*a)
        self.T2=self.T1-((1/self.U2)*a)
        print "T1=%d T2=%d"%(self.T1,self.T2)
    def get_tempenthal(self):
        self.find_temp()
        self.hfg1=float(raw_input("enter enthalpy for T1"))
        self.hfg2=float(raw_input("enter enthalpy for T2"))
        return self.hfg1,self.hfg2
    def find_P(self):
        P=((self.Xf)*(self.F))/(self.X3)
        b=(self.F)-P
        return b
    def solve_eqn(self):
        self.get_tempenthal()
        G=self.find_P()
        B=self.Hs/self.hfg1
        A=(self.F/self.hfg1)*(self.Cpf*(self.Tf-self.T1))
        C=self.Cpf*(self.Tf-self.T1)
        D=self.Cpf*(self.T1-self.T2)
        E=self.Cpf*(self.T2-self.T3)
        J=np.array([[B,1,1],[((B*D)-self.Hs),self.hfg2,0],[(B*E),(E+self.hfg2),self.hfg3]])
        H=np.array([(G-A),((self.F*D)-(A*D)+(self.F*C)),((self.F*E)-(A*E))])
        I=np.linalg.solve(J,H)
        self.K=list(I)
        self.L=(A+(B*self.K[0]))
        return self.K,self.L
    def determine_area(self):
        self.solve_eqn()
        self.A1=(self.K[0]*self.L)/(self.U1*(self.Tf-self.T1))
        self.A2=(self.K[1]*self.hfg2)/(self.U2*(self.T1-self.T2))
        self.A3=(self.K[2]*self.hfg3)/(self.U3*(self.T2-self.T3))
        return self.A1,self.A2,self.A3
    def find_new_area(self):
        avg=(self.A1+self.A2+self.A3)/3
        self.T1=self.Tsat+((self.A1/avg)*(self.Tsat-self.T1))
        self.T2=self.T1+((self.A2/avg)*(self.T2-self.T1))
        self.T3=self.T2+((self.A3/avg)*(self.T2-self.T3))
        return self.determine_area()
    def determine_error(self):
        self.determine_area()
        if (((self.A1-self.A2)/self.A1) and ((self.A2-self.A3)/self.A2) and ((self.A3-self.A1)/self.A3)<= .10):
            print 'Trial successful and the areas of each effect are A1=%d,A2=%d,A3=%d'%(self.A1,self.A2,self.A3)
        else:
            print 'Trial unsuccessful'
            return self.find_new_area()
    def __str__(self):
        return self.determine_error()
evap=input_data(5000,0.10,0.50,37.7,110,37,3.348,6246,3407,2271,2414,2230)
print evap
turtle.shape("turtle")
#help(turtle.color)
turtle.pencolor('red')
turtle.pensize(5)
screen=turtle.Screen()    
screen.setup(750,750)    
screen.bgcolor('black')
turtle.penup()
turtle.setpos(-125,-250)
turtle.pendown()
turtle.forward(250)
turtle.left(90)
turtle.forward(500)
turtle.left(90)
turtle.forward(250)
turtle.left(90)
turtle.forward(500)
turtle.left(90)
turtle.penup()
turtle.setpos(-200,200)
turtle.pendown()
turtle.forward(75)
turtle.penup()
turtle.setpos(-200,0)
turtle.pendown()
turtle.forward(75)
turtle.penup()
turtle.setpos(-125,25)
turtle.pendown()
turtle.forward(25)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(25)
turtle.penup()
turtle.setpos(-40,25)
turtle.pendown()
turtle.forward(25)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(25)
turtle.left(90)
turtle.forward(50)
turtle.penup()
turtle.setpos(-12,25)
turtle.pendown()
turtle.right(90)
turtle.forward(25)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(25)
turtle.right(90)
turtle.forward(50)
turtle.penup()
turtle.setpos(40,25)
turtle.pendown()
turtle.right(90)
turtle.forward(25)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(25)
turtle.right(90)
turtle.forward(50)
turtle.penup()
turtle.setpos(125,25)
turtle.pendown()
turtle.left(90)
turtle.forward(25)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(25)
turtle.penup()
turtle.setpos(125,-100)
turtle.pendown()
turtle.forward(75)
turtle.right(90)
turtle.forward(25)
turtle.penup()
turtle.setpos(0,250)
turtle.pendown()
turtle.right(90)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(75)
turtle.penup()
turtle.setpos(0,-250)
turtle.pendown()
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(75)
turtle.penup()
turtle.setpos(-275,185)
turtle.pendown()
turtle.write('FEED',font=("arial",16,"bold"))
turtle.penup()
turtle.setpos(-295,-15)
turtle.pendown()
turtle.write('STEAM',font=("arial",16,"bold"))
turtle.penup()
turtle.setpos(100,286)
turtle.pendown()
turtle.write('VAPOR',font=("arial",16,"bold"))
turtle.penup()
turtle.setpos(140,-170)
turtle.pendown()
turtle.write('STEAM CONDENSATE',font=("arial",16,"bold"))
turtle.penup()
turtle.setpos(100,-310)
turtle.pendown()
turtle.write('CONCENTRATED SOLN',font=("arial",16,"bold"))
turtle.ht()
turtle.exitonclick()

        
