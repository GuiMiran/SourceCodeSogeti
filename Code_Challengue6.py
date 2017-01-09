import random
import itertools as its

def leer():
    print("ingrese numero")
    x=int(input())
    print(x)
    return (x+1)

def cargaCarta():
    #2-10, J, Q, K, A y los
    #palos C (tréboles), D (rombos), S (picas), H (corazones). 
    palo=random.choice(["C", "D", "S", "H"])
    n=list(range(2,10)) 
    num=random.choice(n+["J","Q","K","A"])
    
    return (num,palo)

def reparteBaraja():
    palo=["C", "D", "S", "H"]
    baraja=[]
    n=list(range(2,11))
    num=["A"]+n+["J","Q","K"]
    for i in its.product(num,palo):
        baraja.append(i)
    
    return baraja
def encontrarCarta(baraj,carta):
    encontrada=False
    for x in baraj:
        if (x==carta):
            encontrada=True
            break
    return encontrada

def barajar(baraj):
    baraj2=[]
    while len(baraj)>0:
        for i in baraj:
            if (i in baraj):
                #if (encontrarCarta(baraj,i)):
                baraj2.append(i)
                baraj.remove(i)
    return baraj2
#Rocky juega a las cartas con tres compañeros:
#    Lil (su pareja de juego), Shady y Danny
def repartirBaraja(baraj):
    Rocky=[]
    Lil=[]
    Shady=[]
    Danny=[]
    for x in range (4):
        Rocky.append(baraj[random.randint(0,51)])
        Lil.append(baraj[random.randint(0,51)])
        Shady.append(baraj[random.randint(0,51)])
        Danny.append(baraj[random.randint(0,51)])
    return Rocky+Lil+Shady+Danny

#print(cargaCarta())
b=reparteBaraja()
print(b)
print("despues de barajar")
b2=barajar(b)
print(b2)
print(repartirBaraja(b2))

