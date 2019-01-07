#columns are 		PROTEINCODE ,P(a) ,P(b) ,P(turn), f(i), f(i+1), f(i+2), f(i+3)
AA_DIC = {}
AA_DIC['Alanine']       = ['A', 142,   83,   66,   0.06,   0.076,  0.035,  0.058]
AA_DIC['Arginine']      = ['R',  98,   93,   95,   0.070,  0.106,  0.099,  0.085]
AA_DIC['Aspartic Acid'] = ['N', 101,   54,  146,   0.147,  0.110,  0.179,  0.081]
AA_DIC['Asparagine']    = ['D',  67,   89,  156,   0.161,  0.083,  0.191,  0.091]
AA_DIC['Cysteine']      = ['C',  70,  119,  119,   0.149,  0.050,  0.117,  0.128]
AA_DIC['Glutamic Acid'] = ['E', 151,   37,   74,   0.056,  0.060,  0.077,  0.064]
AA_DIC['Glutamine']     = ['Q', 111,  110,   98,   0.074,  0.098,  0.037,  0.098]
AA_DIC['Glycine']       = ['G',  57,   75,  156,   0.102,  0.085,  0.190,  0.152]
AA_DIC['Histidine']     = ['H', 100,   87,   95,   0.140,  0.047,  0.093,  0.054]
AA_DIC['Isoleucine']    = ['I', 108,  160,   47,   0.043,  0.034,  0.013,  0.056]
AA_DIC['Leucine']       = ['L', 121,  130,   59,   0.061,  0.025,  0.036,  0.070]
AA_DIC['Lysine']        = ['K', 114,   74,  101,   0.055,  0.115,  0.072,  0.095]
AA_DIC['Methionine']    = ['M', 145,  105,   60,   0.068,  0.082,  0.014,  0.055]
AA_DIC['Phenylalanine'] = ['F', 113,  138,   60,   0.059,  0.041,  0.065,  0.065]
AA_DIC['Proline']       = ['P',  57,   55,  152,   0.102,  0.301,  0.034,  0.068]
AA_DIC['Serine']        = ['S',  77,   75,  143,   0.120,  0.139,  0.125,  0.106]
AA_DIC['Threonine']     = ['T',  83,  119,   96,   0.086,  0.108,  0.065,  0.079]
AA_DIC['Tryptophan']    = ['W', 108,  137,   96,   0.077,  0.013,  0.064,  0.167]
AA_DIC['Tyrosine']      = ['Y',  69,  147,  114,   0.082,  0.065,  0.114,  0.125]
AA_DIC['Valine']        = ['V', 106,  170,   50,   0.062,  0.048,  0.028,  0.053]

AA = ['Alanine', 'Arginine', 'Asparagine', 'Aspartic Acid',
            'Cysteine', 'Glutamic Acid', 'Glutamine', 'Glycine',
            'Histidine', 'Isoleucine', 'Leucine', 'Lysine',
            'Methionine', 'Phenylalanine', 'Proline', 'Serine',
            'Threonine', 'Tryptophan', 'Tyrosine', 'Valine']

Pa = { }
Pb = { }
Pturn = { }
F0 = { }
F1 = { }
F2 = { }
F3 = { }

for aa in AA:
    Pa[AA_DIC[aa][0]] = AA_DIC[aa][1]
    Pb[AA_DIC[aa][0]] = AA_DIC[aa][2]
    Pturn[AA_DIC[aa][0]] = AA_DIC[aa][3]
    F0[AA_DIC[aa][0]] = AA_DIC[aa][4]
    F1[AA_DIC[aa][0]] = AA_DIC[aa][5]
    F2[AA_DIC[aa][0]] = AA_DIC[aa][6]
    F3[AA_DIC[aa][0]] = AA_DIC[aa][7]
seq=raw_input("enter:")



def CF_find_alpha(seq):
    
    start = 0
    results = []
    
    while (start + 6 < len(seq)):
        numgood = 0
        for i in range(start, start+6):
            if (Pa[seq[i]] > 100):
                numgood = numgood + 1
        if (numgood >= 4):
            [estart,end] = CF_extend_alpha(seq, start, start+6)
            if [estart,end] not in results:
                results.append([estart,end])
    
        start = start + 1
    return results

def CF_extend_alpha(seq, start, end):
    

    
    while ( float(sum([Pa[x] for x in seq[end-3:end+1]])) / float(4) ) > 100 and end < len(seq)-1:
        end += 1
    
    while ( float(sum([Pa[x] for x in seq[start:start+4]])) / float(4) ) > 100 and start > 0:
        start -= 1

    return [start,end]



def CF_find_beta(seq):
   
    start = 0
    results = []
   
    while (start + 5 < len(seq)):
       
        numgood = 0
        for i in range(start, start+5):
            if (Pb[seq[i]] > 100):
                numgood = numgood + 1
        if (numgood >= 3):
            [estart,end] = CF_extend_beta(seq, start, start+5)
           
            if [estart,end] not in results:
                results.append([estart,end])
      
        start = start + 1
    return results

def CF_extend_beta(seq, start, end):
    

    
    while ( float(sum([Pb[x] for x in seq[end-3:end+1]])) / float(4) ) > 100 and end < len(seq)-1:
        end += 1
 
    while ( float(sum([Pb[x] for x in seq[start:start+4]])) / float(4) ) > 100 and start > 0:
        start -= 1
    return [start,end]


def CF_find_turns(seq):
    
    result = []
    for i in range(len(seq)-3):
    # CONDITION 1
        c1 = F0[seq[i]]*F1[seq[i+1]]*F2[seq[i+2]]*F3[seq[i+3]] > 0.000075
    # CONDITION 2
        c2 = ( float(sum([Pturn[x] for x in seq[i:i+4]])) / float(4) ) > 100
    # CONDITION 3
        c3 = sum([Pturn[x] for x in seq[i:i+4]]) > max(sum([Pa[x] for x in seq[i:i+4]]),sum([Pb[x] for x in seq[i:i+4]]))
        if c1 and c2 and c3:
            result.append(i)
    return result

   





alphas = CF_find_alpha(seq)
print "Alphas = " + str(alphas)
betas = CF_find_beta(seq)
print "Betas = " + str(betas)
turns = CF_find_turns(seq)
print "Turns = " + str(turns)



z1=[]
z1=list()
z1.extend(seq)




def molwt():
   mol_wt={'A':89,'R':174,'N':132,'D':133,'C':121,'Q':147,'E':147,'G':75,'H':155,'I':131,'L':131,'K':146,'M':149,'F':165,'S':105,'T':119,'Y':204,'Y':204,'V':117,'P':115}
   print len(mol_wt)

   n = {}
   a = 0
   for k,v in mol_wt.items():
      for i in z1:
         if i==k:
            n[k] = v
            a+=n[k]
   print "THE MOLECULAR WEIGHT OF AMINO ACIDS:  "+str(a)

def aminofreq():
   from collections import Counter

   counts = Counter(z1)
   length = len(z1)
   dictionary = dict(counts)
   amino_acids = list(dictionary)
   freq = dictionary.values()
   percentage = []
   for item in freq:
      percentage.append(((item)/float(length))*100)
   print "The percentage of each amino acid in the provided sequence are shown below:"
   print str(zip(amino_acids, percentage))

def gravy():

   gravy={'A':1.8,'R':-4.5,'N':-3.5,'D':-3.5,'C':2.5,'E':-3.5,'Q':-3.5,'G':-0.4,'H':-3.2,'I':4.5,'L':3.8,'K':-3.9,'M':1.9,'F':2.8,'P':-1.6,'S':-0.8,'T':-0.7,'W':-0.9,'Y':-1.3,'V':4.2}

   q=0
   

   n = {}
   a = 0
   for k,v in gravy.items():
       for i in z1:
           if i==k:
               n[k] = v
               q+=n[k]
   print "GRAVY value is: "+str(q/len(z1))

def ext():

   c=0
   y=0
   w=0

   for i in z1:
      if i=='C':
         c+=1
      if i=='Y':
         y+=1
      if i=='W':
         w+=1
   ext=y*1490+w*5500+c*125
   print "The extension coefficient:  "+str(ext)




ext()
gravy()
aminofreq()
molwt()
 
