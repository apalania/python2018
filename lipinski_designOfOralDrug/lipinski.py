# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 01:13:08 2018

@author: Nave
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 10:42:26 2018

@author: Nave
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 10:35:14 2018

@author: Nave
"""
import webbrowser
import easygui
import pubchempy as pcp

features = []
l = []
cid = []
count = 0
values = []

com = easygui.enterbox(msg="Enter the name of the compound to get the pubchem CID:")


#get the compounds for the same name
results = pcp.get_compounds(com, 'name')
for result in results:
    cid.append(str(result)[9:13])
for c in cid:
    
    easygui.msgbox("Displaying all the compounds for the given name...")
    webbrowser.open('https://pubchem.ncbi.nlm.nih.gov/compound/' + c)
    if easygui.ccbox(msg="Do you want to enter the compound ID"):
                    
        count=0 
        chosen_id = easygui.enterbox(msg="Enter the PubChemID: (Your ID options are:- "+str(cid))
        features.append(chosen_id)
        c = pcp.Compound.from_cid(chosen_id)
        features.append(c.molecular_weight)
        features.append(c.h_bond_donor_count)
        features.append(c.h_bond_acceptor_count)
        features.append(c.xlogp)
        l.append(features)
        if features[1] <=500:
        	count+=1
        if features[2] <=5:
        	count+=1
        if features[3]<=10:
        	count+=1
        if features[4] <=5:
        	count+=1
        if count==4:
        	    easygui.msgbox("Lipinski's rule of 5 is satisfied by Compound " + str(features[0]))
        else:
                easygui.msgbox("Lipinski's rule of 5 is NOT satisfied by Compound " + str(features[0]))
    else:
        break
  