obs1 = raw_input("")

obs=list(obs1)
#get initial probability values from user
initproblist=raw_input("enter the initial probabilities")
initproblist1=initproblist.split()
initproblist2=[]
for x in initproblist1:
   initproblist2.append(float(x))
#print initproblist2
#get transition probability values from user
transproblist=raw_input("enter the transition probabilities")
transproblist1=transproblist.split()
transproblist2=[]
for x in transproblist1:
   transproblist2.append(float(x))
#print initproblist2
emisproblist=raw_input("enter the emission probabilities")
emisproblist1=emisproblist.split()
emisproblist2=[]
for x in emisproblist1:
   emisproblist2.append(float(x))
states = ('AT-rich', 'GC-rich')
start_p = {'AT-rich': initproblist2[0], 'GC-rich': initproblist2[1]}
trans_p = {
   'AT-rich' : {'AT-rich': transproblist2[0], 'GC-rich': transproblist2[1]},
   'GC-rich' : {'AT-rich': transproblist2[2], 'GC-rich': transproblist2[3]}
   }
emit_p = {
   'GC-rich' : {'A': emisproblist2[0], 'T': emisproblist2[1], 'G': emisproblist2[2],'C':emisproblist2[3]},
   'AT-rich' : {'A': emisproblist2[4], 'T': emisproblist2[5], 'G': emisproblist2[6],'C':emisproblist2[7]}
   }
#print trans_p
#print emit_p
def viterbi(obs, states, start_p, trans_p, emit_p):

    V = [{}]

    for st in states:

        V[0][st] = {"prob": start_p[st] * emit_p[st][obs[0]], "prev": None}

    # Run Viterbi when t > 0

    for t in range(1, len(obs)):

        V.append({})

        for st in states:

            max_tr_prob = max(V[t-1][prev_st]["prob"]*trans_p[prev_st][st] for prev_st in states)

            for prev_st in states:

                if V[t-1][prev_st]["prob"] * trans_p[prev_st][st] == max_tr_prob:

                    max_prob = max_tr_prob * emit_p[st][obs[t]]

                    V[t][st] = {"prob": max_prob, "prev": prev_st}

                    break

    for line in dptable(V):

        print line

    opt = []

    # The highest probability

    max_prob = max(value["prob"] for value in V[-1].values())

    previous = None

    # Get most probable state and its backtrack

    for st, data in V[-1].items():

        if data["prob"] == max_prob:

            opt.append(st)

            previous = st

            break

    # Follow the backtrack till the first observation

    for t in range(len(V) - 2, -1, -1):

        opt.insert(0, V[t + 1][previous]["prev"])

        previous = V[t + 1][previous]["prev"]


    print 'The hidden states are ' + ' '.join(opt) 
def dptable(V):

    # Print a table of steps from dictionary

    yield " ".join(("%12d" % i) for i in range(len(V)))

    for state in V[0]:

        yield "%.7s: " % state + " ".join("%.7s" % ("%f" % v[state]["prob"]) for v in V)
viterbi(obs,
        states,
        start_p,
        trans_p,
        emit_p)
