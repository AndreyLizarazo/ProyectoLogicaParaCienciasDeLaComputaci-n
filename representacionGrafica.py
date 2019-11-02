import networkx as nx
import matplotlib.pyplot as plt




def Molino():
    G = nx.Graph()
    #crecion de nodos para grafo de ejemplo:
    G.add_node(1, pos = (20,60))
    G.add_node(2, pos = (40,60))
    G.add_node(3, pos =(60,60))

    G.add_node(4,pos =(30,50))
    G.add_node(5, pos =(40,50))
    G.add_node(6,pos=(50,50))

    G.add_node(7,pos=(20,40))
    G.add_node(8,pos=(30,40))
    G.add_node(9,pos=(50,40))
    G.add_node(10,pos=(60,40))

    G.add_node(11,pos=(30,30))
    G.add_node(12,pos=(40,30))
    G.add_node(13,pos=(50,30))

    G.add_node(14,pos=(20,20))
    G.add_node(15,pos=(40,20))
    G.add_node(16,pos=(60,20))
    #grafo ejemplo:
    G.add_edge(1,2)
    G.add_edge(2,5)
    G.add_edge(2,3)
    G.add_edge(3,10)
    G.add_edge(5,6)
    G.add_edge(5,4)
    G.add_edge(7,8)
    G.add_edge(9,6)
    G.add_edge(9,10)
    G.add_edge(8,11)
    G.add_edge(8,4)
    G.add_edge(10,16)
    G.add_edge(11,12)
    G.add_edge(12,13)
    G.add_edge(12,15)
    G.add_edge(13,9)
    G.add_edge(16,15)
    G.add_edge(15,16)
    G.add_edge(15,14)
    G.add_edge(14,7)
    G.add_edge(7,1)
    #Grafica posiciones:
    pos = nx.get_node_attributes(G, 'pos')
    nx.draw(G, pos, with_labels = True)
    plt.show()

#----SITUACÍON INICIAL----
 #  -letra minuscula para las fichas negras
 #  - letra mayuscula para las fichas blancas
dict ={'a':1, 'A':0, 'b':1,'B':0,'c':1,'C':0,'d':1,'D':0,'e':1,'E':0,'f':1, 'F':0,'g':0, 'G':1,'h':0, 'H':1,'i':0, 'I':1,'j':0, 'J':1,'k':0, 'K':1,'l':0, 'L':1,'m':0,'M':0,'n':0,'N':0,'o':0,'O':0,'p':0,'P':0}
H = nx.Graph()
#reglas:
def create_situation(dict):
    H = nx.Graph()
    #-CREACION DE LETRAS PARA LA REPRESENTACÍON GRAFICA:
    a = dict.get('a')
    A = dict.get('A')
    b = dict.get('b')
    B =  dict.get('B')
    c = dict.get('c')
    C =  dict.get('C')
    D = dict.get('D')
    d =  dict.get('d')
    E = dict.get('E')
    F =  dict.get('F')
    G = dict.get('G')
    Z =  dict.get('H')
    I = dict.get('I')
    J =  dict.get('J')
    K = dict.get('K')
    L =  dict.get('L')
    M = dict.get('M')
    N =  dict.get('N')
    O = dict.get('O')
    P =  dict.get('P')
    e = dict.get('e')
    f = dict.get('f')
    g = dict.get('g')
    h = dict.get('h')
    i = dict.get('i')
    j = dict.get('j')
    k = dict.get('k')
    l = dict.get('l')
    m = dict.get('m')
    n = dict.get('n')
    o = dict.get('o')
    p = dict.get('p')
    z = dict.get('h')
    char = ''


    #AGREGA
    #ILERAS DEL GRAFO:
        #-fichas a,A:
    if a == 1 and A == 0:
        H.add_node('a',pos = (20,60))
    if a == 0 and A == 1:
        H.add_node('A',pos = (20,60))
    if a == 0 and A == 0:
        H.add_node(char,pos =(20,60))
        char += ' '
    if a == 1 and A == 1:
        print("No puede haber dos fihas en un mismo nodo")
        #-fichas b,B:
    if b == 1 and B == 0:
        H.add_node('b',pos = (40,60))
    if b == 0 and b == 1:
        H.add_node('B',pos = (40,60))
    if b == 0 and B == 0:
        H.add_node(char,pos =(40,60))
        char += ' '
    if b == 1 and B == 1:
        print("No puede haber dos fihas en un mismo nodo")
        #- fichas c,C:
    if c == 1 and C == 0:
        H.add_node('c',pos = (60,60))
    if c == 0 and C == 1:
        H.add_node('C',pos = (60,60))
    if c == 0 and C == 0:
        H.add_node(char,pos =(60,60))
        char += ' '
    if c == 1 and C == 1:
        print("No puede haber dos fihas en un mismo nodo")
         #- fichas d,D:
    if d == 1 and D == 0:
        H.add_node('d',pos = (30,50))
    if d == 0 and D == 1:
        H.add_node('D',pos = (30,50))
    if d == 0 and D == 0:
        H.add_node(char,pos =(30,50))
        char += ' '
    if d == 1 and D == 1:
        print("No puede haber dos fihas en un mismo nodo")
        #-fichas e,E:
    if e == 1 and E == 0:
        H.add_node('e',pos = (40,50))
    if e == 0 and E == 1:
        H.add_node('E',pos = (40,50))
    if e == 0 and E == 0:
        H.add_node(char,pos =(40,50))
        char += ' '
    if e == 1 and E == 1:
        print("No puede haber dos fihas en un mismo nodo")
        #-fichas f,F:
    if f == 1 and F == 0:
        H.add_node('f',pos = (50,50))
    if f == 0 and F == 1:
        H.add_node('F',pos = (50,50))
    if f == 0 and F == 0:
        H.add_node(char,pos =(50,50))
        char += ' '
    if f == 1 and F == 1:
        print("No puede haber dos fihas en un mismo nodo")
        #-fichas g,G:
    if g == 1 and G == 0:
        H.add_node('g',pos = (20,40))
    if g == 0 and G == 1:
        H.add_node('G',pos = (20,40))
    if g == 0 and G == 0:
        H.add_node(char,pos =(20,40))
        char += ' '
    if g == 1 and G == 1:
        print("No puede haber dos fihas en un mismo nodo")
        #-fichas h,H:
    if z == 1 and Z == 0:
        H.add_node('h',pos = (30,40))
    if z == 0 and Z == 1:
        H.add_node('H',pos = (30,40))
    if z == 0 and Z == 0:
        H.add_node(char,pos =(30,40))
        char += ' '
    if z == 1 and Z == 1:
        print("No puede haber dos fihas en un mismo nodo")
        #-fichas i,I:
    if i == 1 and I == 0:
        H.add_node('i',pos = (50,40))
    if i == 0 and I == 1:
        H.add_node('I',pos = (50,40))
    if i == 0 and I == 0:
        H.add_node(char,pos =(50,40))
        char += ' '
    if i == 1 and I == 1:
        print("No puede haber dos fihas en un mismo nodo")
        #-fichas j,J:
    if j == 1 and J == 0:
        H.add_node('j',pos = (60,40))
    if j == 0 and J == 1:
        H.add_node('J',pos = (60,40))
    if j == 0 and J == 0:
        H.add_node(char,pos =(60,40))
        char += ' '
    if j == 1 and J == 1:
        print("No puede haber dos fihas en un mismo nodo")
        #-fichas k,K:
    if k == 1 and K == 0:
        H.add_node('k',pos = (30,30))
    if k == 0 and K == 1:
        H.add_node('K',pos = (30,30))
    if k == 0 and K == 0:
        H.add_node(char,pos =(30,30))
        char += ' '
    if k == 1 and K == 1:
        print("No puede haber dos fihas en un mismo nodo")
        #-fichas l,L:
    if l == 1 and L == 0:
        H.add_node('l',pos = (40,30))
    if l == 0 and L == 1:
        H.add_node('L',pos = (40,30))
    if l == 0 and L == 0:
        H.add_node(char,pos =(40,30))
        char += ' '
    if l == 1 and L == 1:
        print("No puede haber dos fihas en un mismo nodo")
        #fichas m,M:
    if m == 1 and M == 0:
        H.add_node('m',pos = (50,30))
    if m == 0 and M == 1:
        H.add_node('M',pos = (50,30))
    if m == 0 and M == 0:
        H.add_node(char,pos =(50,30))
        char += ' '
    if m == 1 and M == 1:
        print("No puede haber dos fihas en un mismo nodo")
        #fichas n,N:
    if n == 1 and N == 0:
        H.add_node('n',pos = (20,20))
    if n == 0 and N == 1:
        H.add_node('N',pos = (20,20))
    if n == 0 and N == 0:
        H.add_node(char,pos =(20,20))
        char += ' '
    if n == 1 and N == 1:
        print("No puede haber dos fihas en un mismo nodo")
        #fichas o,O:
    if o == 1 and O == 0:
        H.add_node('o',pos = (40,20))
    if o == 0 and O == 1:
        H.add_node('O',pos = (40,20))
    if o == 0 and O == 0:
        H.add_node(char,pos =(40,20))
        char += ' '
    if o == 1 and O == 1:
        print("No puede haber dos fihas en un mismo nodo")
        #fichas p,P:
    if p == 1 and P == 0:
        H.add_node('p',pos = (60,20))
    if p == 0 and P == 1:
        H.add_node('P',pos = (60,20))
    if p == 0 and P == 0:
        H.add_node(char,pos =(60,20))
        char += ' '
    if p == 1 and P == 1:
        print("No puede haber dos fihas en un mismo nodo")
    pos = nx.get_node_attributes(H, 'pos')
    n = H.nodes()
    lista = []
    for i in n:
        lista.append(i)
    H.add_edge(lista[0],lista[1])
    H.add_edge(lista[1],lista[2])
    H.add_edge(lista[0],lista[6])
    H.add_edge(lista[6],lista[13])
    H.add_edge(lista[13],lista[14])
    H.add_edge(lista[15],lista[9])
    H.add_edge(lista[9],lista[2])
    H.add_edge(lista[8],lista[5])
    H.add_edge(lista[9],lista[8])
    H.add_edge(lista[8],lista[12])
    H.add_edge(lista[11],lista[10])
    H.add_edge(lista[11],lista[12])
    H.add_edge(lista[10],lista[7])
    H.add_edge(lista[7],lista[6])
    H.add_edge(lista[1],lista[4])
    H.add_edge(lista[3],lista[4])
    H.add_edge(lista[4],lista[5])
    H.add_edge(lista[14],lista[15])
    H.add_edge(lista[14],lista[11])
    H.add_edge(lista[6],lista[7])
    H.add_edge(lista[3],lista[7])
    nx.draw(H,pos, with_labels = True)
    plt.show()
def exposicion():
    a = int(input("Ingrese el numero 1 si quiere ver el grafo de ejemplo, ingrese el numero 2 si quiere ver la situacion inicial:"))
    if a == 1:
        Molino()
    if a == 2:
        create_situation(dict)

exposicion()
