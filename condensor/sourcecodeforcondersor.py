from __future__ import division
import math
import  turtle 
'''global maxval
global minval'''
y=[0]*2                                                                         
def getud(hf,cf):
        '''ud values from table'''
        f=open("htc_df.txt","r") 
        hf=hf.lower()
        cf=cf.lower()
        for line in f.readlines():
            line=line.lower()
            if line.startswith(hf):
                    if cf in line[46:]:
                        
                         minval=int(line[79:82])
                         maxval=int(line[83:86])
                         y[0]=int(minval)
                         y[1]=int(maxval)
        return y
def getDirtfactorGiven(hf,cf):
        """Gets the dirt factor from the table """
        f=open("htc_df.txt","r")
        for line in f.readlines():
            line=line.lower()
            if line.startswith(hf.lower()):
                    if cf.lower() in line[46::]:
                            df=float(line[94:100])
                            return df


hf=raw_input("HOT:")
cf=raw_input("COLD:")
x=[]
x=getud(hf,cf)
print x
y=getDirtfactorGiven(hf,cf)
print y
def frange(start,stop,step):
        """Generates float values within the given range """ 
        listf=[]
        start=int(start//step)
        stop=int(stop//step)
        for i in range (start,stop):
           listf.append(round((i*step),2))
        return listf
class parameters :
        def __init__(self,fluid,intemp,Mh):
                self.fluid=fluid.lower()
                self.intemp=intemp
                self.Mh=Mh
                if self.fluid=="Water":
                        self.getprop_water()
                else:
                        self.getprops()

        def getprops(self):
                """get all the properties at bulk temperature from user"""
                self.density=float(raw_input("Enter density in kg/m3"))
                self.dyn_vis=float(raw_input("Enter viscosity in kg/ms"))
                self.cp=float(raw_input("Enter specific heat capacity in J/kg K"))
                self.k=float(raw_input("Enter thermal conductivity in W/m K"))

        def getprop_water():
                "Assume the properties"
                self.density=995
                self.dyn_vis=0.8
                self.cp=4.2
                self.k=0.59
        def findNusseltNumber(self,dia,velocity):
                self.Nre=self.density*velocity*dia/self.dyn_vis
                self.Pr=self.cp*self.dyn_vis/self.k
                self.Nu=0.023*(self.Nre**0.8)*(self.Pr**0.33)

Mh=float(raw_input("Enter mass flow rate in kg/s"))
intemp=float(raw_input("Enter inlet temperature in celcius"))
lamb=float(raw_input("Enter the latent heat of vapourisation LAMDA"))

Mc=float(raw_input("Enter mass flow rate(COLD FLUID) in kg/s"))
cintemp=float(raw_input("Enter inlet temperature(COLD FLUID) in celcius"))


hfluid=parameters(hf,intemp,Mh)

Q=Mh*lamb
print Q
g=Q/(Mc*4.187)
print g

couttemp=cintemp + g
print couttemp

cfluid=parameters(cf,cintemp,Mc)
'''def calcLMTD(Th,tco,tci):
        q=(Th-tci)
        r=(Th-tco)
        p=r-q
        m=int((Th-tco)/(Th-tci))
        n=math.log(m)
        lmtd=(p)/(n)
        return lmtd

LMTDc=calcLMTD(hfluid.intemp,cfluid.intemp,couttemp)
print LMTDc'''

               #multiplying by 0.1761 for unit conversion


"""Heat transfer in tube side """
outerdia=0.019
length=4
innerdia=0.0157
a=5.6783
pi=3.14
LMTDc=float(raw_input("ENTER LMTD TEMP VALUE :"))
print "LMTD Temp is :" , LMTDc
pie=3.14/4

for Ud in range(x[0],x[1],2):     #calculating tube side velocity
        HTArea=Q/(Ud*5.6783*LMTDc)#Heat transfer Area , multiplying Ud by 5.6783 for unit conversion 
        print "heat transfer area"
        print HTArea
        Nt=HTArea/(pi*outerdia*length)              #Number of tubes  
        print "NO.OF.TUBES REQUIRED"
        print Nt
        ts_flow_area=(pie)*(innerdia**2)*(Nt/2)    #Tube side flow Aarea 
        ts_velocity= Mc/(cfluid.density*ts_flow_area) 
        if ts_velocity <=3 and ts_velocity >=4 :
                break
hfluid.findNusseltNumber(innerdia,ts_velocity) #Nusselt number calculation
f=(hfluid.Nu*hfluid.k)
hi=f/innerdia

"""Shell side"""
vap_den=float(raw_input("Enter the vapour density:"))

bundledia=outerdia*((Nt/0.249)**(1/2.207))        #bundle diameter for triangular pitch
"shelldia=findShellDia(bundledia)"
shelldia=0.016
pt=1.25*outerdia


for i in frange(0.2,1.1,0.1):
        Bs=i*shelldia
        ss_flow_area=(pt-outerdia)*shelldia*Bs/pt
        ss_velocity=hfluid.Mh/(hfluid.density*ss_flow_area)
        if ss_velocity <=1 and ss_velocity >=0.3 :
                break
tou=Mh/(4*Nt)
Nr=0.66*(Bs/pt)
de=1.1*((pt**2) - (0.907*outerdia**2)) #calculation of equivalent diameter(assuming triangular pitch)
cfluid.findNusseltNumber(de,ss_velocity)
xa=0.95*cfluid.k
xb=cfluid.density-vap_den
xc=cfluid.dyn_vis*tou
xe=cfluid.density*(xb)*9.81
xf=float(xe/xc)
xd=xf**(1./3.)
print xd
xg=Nr**(1./3.)
yb=float(1/xg)

ho=xa*xd*yb


xw=(outerdia-innerdia)/2

Uc=(ho**-1)+(hi**-1)*(outerdia/innerdia)+(xw/50) #thermal conductivity of stainless steel=50 W/mK
uc=float(1./Uc)
dirt_factor_cal=(Ud**-1)-(uc**-1)
print "CALC dirt factor :", dirt_factor_cal
if y>dirt_factor_cal:
        print "Design can't be done for the given duty"
else:
                print("Design of stainless steel shell and tube heat exchanger:")
                print ("Pitch : Triangular pitch")
                print ("Configuration : 1 shell pass and 2 tube passes")
                print ("Shell diameter : %s m \n Baffle spacing : %s m"%(shelldia,Bs))
                print("Bundle diameter : %s m \n "%(bundledia))
                print ("Number of tubes : %s \n Length of tubes : %s m"%(Nt,length))
                print("Diameter of tubes : %s m\n Dirt factor : %s sq.m K/W"%(outerdia,dirt_factor_cal))

        




                        

