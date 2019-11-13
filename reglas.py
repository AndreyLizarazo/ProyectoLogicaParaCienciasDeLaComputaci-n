def Tseitin(A, letrasProposicionalesA):
    letrasProposicionalesB = [chr(x) for x in range(256, 300)]
    assert(not bool(set(letrasProposicionalesA) & set(letrasProposicionalesB)))
    L = []
    Pila = [] # Inicializamos pila
    i = -1 # Inicializamos contador de variables nuevas
    s = A[0] # Inicializamos sımbolo de trabajo
    while (len(A) > 0):
        if s in letrasProposicionalesA and Pila[-1] =='-':
            i += 1
            atomo = letrasProposicionalesB[i]
            Pila = Pila[:-1]
            Pila.append(atomo)
            L.append(atomo + '=' + '-' + s)
            A = A[0]
            s = A[0]
            if len(A) > 0:
                s = A[0]
        elif s == ')':
            w = Pila[-1]
            O = Pila[-2]
            v = Pila[-3]
            Pila = Pila[:len(Pila)-4]
            i += 1
            atomo = letrasProposicionalesB[i]
            L.append(atomo +"="+"(" + v + O + w + ")")
            s = atomo
        else:
            Pila.append(s)
            A = A[1:]
            if len(A) > 0:
                s = A[0]

    B = ""
    if i < 0:
        atomo = Pila[-1]
    else:
        atomo = letrasProposicionalesB[i]
    for x in L:
        y = enFNC(x)
        B += "Y" + y

    B = atomo + B
    return B


# Output: B (cadena), equivalente en FNC
def enFNC(A):
    assert(len(A)==4 or len(A)==7), u"Fórmula incorrecta!"
    B = ''
    p = A[0]
    # print('p', p)
    if "-" in A:
        q = A[-1]
        # print('q', q)
        B = "-"+p+"O-"+q+"Y"+p+"O"+q
    elif "Y" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"O-"+p+"Y"+r+"O-"+p+"Y-"+q+"O-"+r+"O"+p
    elif "O" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"O"+p+"Y-"+r+"O"+p+"Y"+q+"O"+r+"O-"+p
    elif ">" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"O"+p+"Y-"+r+"O"+p+"Y-"+q+"O"+r+"O-"+p
    else:
        print(u'Error enENC(): Fórmula incorrecta!')

    return B

# Algoritmo de transformacion de Tseitin
# Input: A (cadena) en notacion inorder
# Output: B (cadena), Tseitin
# def Tseitin(A, letrasProposicionalesA):
#     letrasProposicionalesB = [chr(x) for x in range(256, 300)]
#     assert(not bool(set(letrasProposicionalesA) & set(letrasProposicionalesB)))
#     l = []
#     pila = []
#     i = -1
#     s = A[0]
#     while len(A) > 0:
#         if s in letrasProposicionalesA and pila[-1] == '-':
#             i += 1
#             atomo = letrasProposicionalesB[i]
#             pila = pila[:-1]
#             pila.append(atomo)
#             l.append(atomo + '=-' + s)
#             A = A[1:]
#             s = A[0]
#             if len(A) > 0:
#                 s = A[0]
#         elif s == ')':
#             w = pila[-1]
#             o = pila[-2]
#             v = pila[-3]
#             pila = pila[:len(pila)-4]
#             i += 1
#             atomo = letrasProposicionalesB[i]
#             l.append(atomo + "=" + v + o + w)
#             s = atomo
#         else:
#             pila.append(s)
#             A = A[1:]
#             if len(A) > 0:
#                 s = A[0]
#
#     b = ''
#     if i < 0:
#         atomo = pila[-1]
#     else:
#         atomo = letrasProposicionalesB[i]
#     for x in l:
#         y = enFNC(x)
#         b += 'Y' + y
#     b = atomo + b
#
#     return "OK"

# Subrutina Clausula para obtener lista de literales
# Input: C (cadena) una clausula
# Output: L (lista), lista de literales
def Clausula(C):
    L=[]
    while len(C)>0:
        s=C[0]
        if s == "O":
            C=C[1:]
        elif s=="~":
            literal = s + C[1]
            L.append(literal)
            C = C[2:]
        else:
            L.append(s)
            C = C[1:]
    return L

# Algoritmo para obtencion de forma clausal
# Input: A (cadena) en notacion inorder en FNC
# Output: L (lista), lista de listas de literales
def formaClausal(A):
    L=[]
    i=0
    while len(A)>0:
        if A[i] == "O":
            L.append(Clausula(A[:i]))
            A = A[i+1:]
            i=0
        elif i<len(A):
            i+=1
        else:
            L.append(Clausula(A))
            A =[]

    return L


def r(l1,l2):
    lista = []
    r1 = "(" + l1 + "Y" + "-" + l2 + ")"
    r2 =  "(" + "-"+ l1 + "Y"  + l2 + ")"
    r3 =  "(" + "-"+ l1 + "Y"  + "-" + l2 + ")"
    r = "(" + r1 + "O" + r2 + "O" + r3 + ")" + "Y"
    return r


def regla1():
    letras = [("x","X"),("b","B"),("c","C"),("d","D"),("e","E"),("f","F"),("g","G"),("h","H"),("i","I"),("j","J"),("k","K"),("l","L"),("m","M"),("n","N"),("o","O"),("p","P")]
    regla = ""
    regla += "("
    for (x,y) in letras:
        regla += r(x,y)


    regla += ")"
    final = regla[0:len(regla)-2]
    final += ")"
    return final

e = "abcdefghijklmnop"
letras = []
for i in e:
    t = i.upper()
    letras.append(i)
    letras.append(t)
print(regla1())
print(Tseitin(regla1(),letras))
