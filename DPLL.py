#S,conjunto de clausulas -> retorna clausulas
#I, interpretacion parcial -> retorna una inter pretacion parcial
LetrasProposicionales = [["-p"],["p"],["-p","-q"],["-q","r","s"],["u","-s","r"],["r","t"],["p","s","-t"],["-r","-u"]]
S = LetrasProposicionales
I = {}
def r1(S):
    for i in S:
        if len(i) == 1:
            return True
    return False
def r2(S,I):
    l = ""
    temp = ""
    I2 = I.keys()
    for i in S:
        for j in i:
            if len(j) != 1:
                temp = j[1]
            else:
                temp = j
            if temp not in I2:
                l = j
                print(l)
                for x in S:
                    if l in x:
                        print(x)
                        S.remove(x)

                if '-' not in l:
                    I[l] = 1
                    lc = '-' + l
                    for e in S:
                        if lc in e:
                            e.remove(lc)
                if '-' in l:
                    I[l[1]] = 0
                    lc = l[1]
                    for y in S:
                        if lc in y:
                            y.remove(lc)
                break
        
    return S,I


def unitPropagate(S,I):
    while(r1(S)==True):
        l = ""
        for x in S:
            if len(x) == 1:
                l = x[0]
                #print(l,x)
                S.remove(x)
                break

        if '-' in l:
            I[l[1]] = 0
            lc = l[1]
            for j in S:
                if l in j:
                    S.remove(j)
                if lc in j:
                    j.remove(lc)

        if '-' not in l:
            I[l] = 1
            lc = '-' + l
            for i in S:
                if l in i:
                    S.remove(i)
                if lc in i:
                    i.remove(lc)

        unitPropagate(S,I)


    return S,I


def DPLL(S,I):
    if r1(S):
        unitPropagate(S,I)


    if len(S)==1:
        x = S[0]
        for i in x:
            if i not in I.keys():
                l = i
                if '-' not in l:
                    I[l] = 1
                    S.remove(x)
                    break
                if '-' in l:
                    I[l[1]] = 0
                    S.remove(x)
                    break


    if [] in S:
        return "Insatisfacible", I
    if len(S) == 0:
        return "Satisfacible", I
    else:
        r2(S,I)
    return DPLL(S,I)













t = [["p","-q","r"],["-p","q","-r"],["-p","-q","r"],["-p","-q","-r"]]
y = {}
p = [["p"],["-p","q"],["-q","r","s"]]
print(t,y)
print(r2(t,y))

print(DPLL(t,y))
