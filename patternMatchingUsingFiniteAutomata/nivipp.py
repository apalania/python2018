class Pattern:
    def __init__(self,pat,txt):
        self.pat=pat
        self.txt=txt
    
    def getNextState(self, M, state, x): 
        
        if state < M and x == ord(self.pat[state]): 
            return state+1
      
        i=0
       
        for ns in range(state,0,-1): 
            if ord(pat[ns-1]) == x: 
                while(i<ns-1): 
                    if self.pat[i] != self.pat[state-ns+1+i]: 
                        break
                    i+=1
                if i == ns-1: 
                    return ns  
        return 0
      
    def computeTF(self, M): 
       
        NO_OF_CHARS=250
      
        TF = [[0 for i in range(NO_OF_CHARS)] 
              for _ in range(M+1)] 
      
        for state in range(M+1): 
            for x in range(NO_OF_CHARS): 
                z = Pattern.getNextState(self, M, state, x) 
                TF[state][x] = z 
      
        return TF 
      
    def search(self): 
        
        NO_OF_CHARS=250
        M = len(self.pat) 
        N = len(self.txt) 
        TF=Pattern.computeTF(self, M)     
      
        # Process txt over FA. 
        state=0
        for i in range(N): 
            state = TF[state][ord(self.txt[i])] 
            if state == M: 
                print("Pattern found at index: {}". 
                       format(i-M+1)) 
  
            
txt = raw_input("Enter a Text:") 
pat = raw_input("Enter a Pattern:")
ob=Pattern(pat,txt)
print(ob.search)
ob.search()

