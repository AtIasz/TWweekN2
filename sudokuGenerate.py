import random
lista=[[], [], [], [], [], [], [], [], []]
for i in range(len(lista)):
    lista[i]=[1,2,3,4,5,6,7,8,9]
random.shuffle(lista[0])


p=[1,2,3,4,5,6,7,8,9]
p.remove(lista[0][0])
p.remove(lista[0][1])
p.remove(lista[0][2])
random.shuffle(p)
lista[1][0]=p[0]
p.remove(p[0])
random.shuffle(p)
lista[1][1]=p[0]
p.remove(p[0])
random.shuffle(p)
lista[1][2]=p[0]
p.remove(p[0])
random.shuffle(p)
lista[2][0]=p[0]
p.remove(p[0])
random.shuffle(p)
lista[2][1]=p[0]
p.remove(p[0])
random.shuffle(p)
lista[2][2]=p[0]
p.remove(p[0])
#1. sor + 1. 3x3 rács




#2. 3x3 rács, alatta lévő:

p=[1,2,3,4,5,6,7,8,9]

p.remove(lista[0][0])
p.remove(lista[1][0])
p.remove(lista[2][0])

random.shuffle(p)
lista[3][0]=p[0]
p.remove(p[0])
random.shuffle(p)
lista[4][0]=p[0]
p.remove(p[0])
random.shuffle(p)
lista[5][0]=p[0]
p.remove(p[0])
random.shuffle(p)
#2. bal oldal
p=[1,2,3,4,5,6,7,8,9]
p.remove(lista[0][1])
p.remove(lista[1][1])
p.remove(lista[2][1])
mustuse=[]
#1.3x3 közepe kivéve
if lista[3][0] in p:
    p.remove(lista[3][0])
if lista[4][0] in p:
    p.remove(lista[4][0])
if lista[5][0] in p:
    p.remove(lista[5][0])
#1.3x3 bal kivéve ha
if lista[0][2] in p:
    mustuse.append(lista[0][2])
    p.remove(lista[0][2])
if lista[1][2] in p:
    mustuse.append(lista[1][2])
    p.remove(lista[1][2])
if lista[2][2] in p:
    mustuse.append(lista[2][2])
    p.remove(lista[2][2])
#1. 3x3 jobb kivéve HA van
while len(mustuse)!=3:
    random.shuffle(p)
    mustuse.append(p[0])
    p.remove(p[0])

#print(f"Mustuse:{mustuse}")
#2. 3x3 közepe
random.shuffle(mustuse)
lista[3][1]=mustuse[0]
mustuse.remove(mustuse[0])
random.shuffle(mustuse)
lista[4][1]=mustuse[0]
mustuse.remove(mustuse[0])
lista[5][1]=mustuse[0]
mustuse.remove(mustuse[0])



#2. 3x3 jobb oldala:
p=[1,2,3,4,5,6,7,8,9]
p.remove(lista[3][0])
p.remove(lista[4][0])
p.remove(lista[5][0])
p.remove(lista[3][1])
p.remove(lista[4][1])
p.remove(lista[5][1])

random.shuffle(p)
lista[3][2]=p[0]
p.remove(p[0])
random.shuffle(p)
lista[4][2]=p[0]
p.remove(p[0])
random.shuffle(p)
lista[5][2]=p[0]
p.remove(p[0])
#2 3x3 KÉSZ,bal felső 2

p=[1,2,3,4,5,6,7,8,9]
p.remove(lista[0][0])
p.remove(lista[1][0])
p.remove(lista[2][0])
p.remove(lista[3][0])
p.remove(lista[4][0])
p.remove(lista[5][0])
lista[6][0]=p[0]
p.remove(p[0])
random.shuffle(p)
lista[7][0]=p[0]
p.remove(p[0])
random.shuffle(p)
lista[8][0]=p[0]
p.remove(p[0])
#3. 3x3 bal oldala

p=[1,2,3,4,5,6,7,8,9]
p.remove(lista[0][1])
p.remove(lista[1][1])
p.remove(lista[2][1])
p.remove(lista[3][1])
p.remove(lista[4][1])
p.remove(lista[5][1])
random.shuffle(p)
lista[6][1]=p[0]
p.remove(p[0])
random.shuffle(p)
lista[7][1]=p[0]
p.remove(p[0])
random.shuffle(p)
lista[8][1]=p[0]
p.remove(p[0])
#3. rács [bal alsó] közepe

p=[1,2,3,4,5,6,7,8,9]
p.remove(lista[0][2])
p.remove(lista[1][2])
p.remove(lista[2][2])
p.remove(lista[3][2])
p.remove(lista[4][2])
p.remove(lista[5][2])
random.shuffle(p)
lista[6][2]=p[0]
p.remove(p[0])
random.shuffle(p)
lista[7][2]=p[0]
p.remove(p[0])
random.shuffle(p)
lista[8][2]=p[0]
p.remove(p[0])

#3. rács [bal alsó] jobb oldala, 3 3x3 kész.
'''
#3 db 3x3 bal oldali nyomtetve
for i in range(1,9):
    print("[",end="")
    for j in range(3):
        print(str(lista[i][j])+",",end=" ")
    print()
    if i==2 or i==5:
        print()
'''
#4. 3x3 teteje:
p=[1,2,3,4,5,6,7,8,9]
p.remove(lista[0][0])
p.remove(lista[0][1])
p.remove(lista[0][2])


random.shuffle(p)
lista[0][3]=p[0]
p.remove(p[0])
random.shuffle(p)
lista[0][4]=p[0]
p.remove(p[0])
random.shuffle(p)
lista[0][5]=p[0]
p.remove(p[0])
#jo

p=[1,2,3,4,5,6,7,8,9]
p.remove(lista[0][3])
p.remove(lista[0][4])
p.remove(lista[0][5])
if lista[2][0] in p:
    mustuse.append(lista[2][0])
    p.remove(lista[2][0])
if lista[2][1] in p:
    p.remove(lista[2][1])
    mustuse.append(lista[2][1])
if lista[2][2] in p:
    p.remove(lista[2][2])
    mustuse.append(lista[2][2])
if lista[1][0] in p:
    p.remove(lista[1][0])
if lista[1][1] in p:
    p.remove(lista[1][1])
if lista[1][2] in p:
    p.remove(lista[1][2])

while len(mustuse)<3:
    random.shuffle(p)
    mustuse.append(p[0])
    p.remove(p[0])

random.shuffle(mustuse)
lista[1][3]=mustuse[0]
mustuse.remove(mustuse[0])
random.shuffle(mustuse)
lista[1][4]=mustuse[0]
mustuse.remove(mustuse[0])
#1 elem van hátra, értelmetlen a shuffle
lista[1][5]=mustuse[0]
mustuse.remove(mustuse[0])
#középső legfelső 3x3 közepe


#chin up



#középső legfelső 3x3 alsó sor:
p=[1,2,3,4,5,6,7,8,9]

if lista[0][3] in p:
    p.remove(lista[0][3])
if lista[0][4] in p:
    p.remove(lista[0][4])
if lista[0][5] in p:
    p.remove(lista[0][5])
if lista[1][3] in p:
    p.remove(lista[1][3])
if lista[1][4] in p:
    p.remove(lista[1][4])
if lista[1][5] in p:
    p.remove(lista[1][5])
    

random.shuffle(p)
lista[2][3]=p[0]
p.remove(p[0])
random.shuffle(p)
lista[2][4]=p[0]
p.remove(p[0])
random.shuffle(p)
lista[2][5]=p[0]
p.remove(p[0])
#stimm 22:57

#középső sor középső 3x3(5.) kezdet:
p=[1,2,3,4,5,6,7,8,9]
p.remove(lista[3][0])
p.remove(lista[3][1])
p.remove(lista[3][2])
if lista[0][3] in p:
    p.remove(lista[0][3])
if lista[1][3] in p:
    p.remove(lista[1][3])
if lista[2][3] in p:
    p.remove(lista[2][3])
random.shuffle(p)
lista[3][3]=p[0]
p.remove(p[0])
#[3][3] elem

p=[1,2,3,4,5,6,7,8,9]
p.remove(lista[4][0])
p.remove(lista[4][1])
p.remove(lista[4][2])
if lista[0][3] in p:
    p.remove(lista[0][3])
if lista[1][3] in p:
    p.remove(lista[1][3])
if lista[2][3] in p:
    p.remove(lista[2][3])
if lista[3][3] in p:
    p.remove(lista[3][3])
random.shuffle(p)
lista[4][3]=p[0]
p.remove(p[0])
#[4][3] elem

p=[1,2,3,4,5,6,7,8,9]
p.remove(lista[5][0])
p.remove(lista[5][1])
p.remove(lista[5][2])
if lista[0][3] in p:
    p.remove(lista[0][3])
if lista[1][3] in p:
    p.remove(lista[1][3])
if lista[2][3] in p:
    p.remove(lista[2][3])
if lista[3][3] in p:
    p.remove(lista[3][3])
if lista[4][3] in p:
    p.remove(lista[4][3])
random.shuffle(p)
lista[5][3]=p[0]
p.remove(p[0])
#[5][3] elem

p=[1,2,3,4,5,6,7,8,9]
p.remove(lista[3][0])
p.remove(lista[3][1])
p.remove(lista[3][2])
p.remove(lista[3][3])

if lista[0][4] in p:
    p.remove(lista[0][4])
if lista[1][4] in p:
    p.remove(lista[1][4])
if lista[2][4] in p:
    p.remove(lista[2][4])
if lista[4][3] in p:
    p.remove(lista[4][3])
if lista[5][3] in p:
    p.remove(lista[5][3])
random.shuffle(p)
lista[3][4]=p[0]
p.remove(p[0])
#[3][4] elem

p=[1,2,3,4,5,6,7,8,9]
p.remove(lista[4][0])
p.remove(lista[4][1])
p.remove(lista[4][2])
p.remove(lista[4][3])

if lista[0][4] in p:
    p.remove(lista[0][4])
if lista[1][4] in p:
    p.remove(lista[1][4])
if lista[2][4] in p:
    p.remove(lista[2][4])
if lista[3][4] in p:
    p.remove(lista[3][4])
if lista[5][3] in p:
    p.remove(lista[5][3])
random.shuffle(p)
lista[4][4]=p[0]
p.remove(p[0])
#[4][4] elem

p=[1,2,3,4,5,6,7,8,9]
'''
p.remove(lista[5][1])
p.remove(lista[5][2])
p.remove(lista[5][3])
'''


for i in range(9):
    for j in range(6):
        print(str(lista[i][j])+", ",end="")
        if j==2 or j==5:
            print(" ",end="")
    if i==2 or i==5:
        print()
    print()


if lista[5][0] in p:
    p.remove(lista[5][0])
if lista[5][1] in p:
    p.remove(lista[5][1])
if lista[5][2] in p:
    p.remove(lista[5][2])
if lista[5][3] in p:
    p.remove(lista[5][3])
if lista[0][4] in p:
    p.remove(lista[0][4])
if lista[1][4] in p:
    p.remove(lista[1][4])
if lista[2][4] in p:
    p.remove(lista[2][4])
if lista[3][4] in p:
    p.remove(lista[3][4])
if lista[4][4] in p:
    p.remove(lista[4][4])
if lista[3][3] in p:
    p.remove(lista[3][3])
if lista[4][3] in p:
    p.remove(lista[4][3])
print(p)
lista[5][4]=p[0]            #
#[5][4] elem
'''
p=[1,2,3,4,5,6,7,8,9]
p.remove(lista[0][3])
p.remove(lista[0][4])
p.remove(lista[0][5])
p.remove(lista[1][3])
p.remove(lista[1][4])
p.remove(lista[1][5])
print(p)
if lista[2][0] in p:
    p.remove(lista[2][0])
if lista[2][1] in p:
    p.remove(lista[2][1])
if lista[2][2] in p:
    p.remove(lista[2][2])
print(p)
random.shuffle(p)
lista[2][3]=p[0]
p.remove(p[0])
random.shuffle(p)
lista[2][4]=p[0]
p.remove(p[0])
random.shuffle(p)
lista[2][5]=p[0]
p.remove(p[0])


print(f"Mustuse:{mustuse}")
random.shuffle(mustuse)
lista[2][3]=mustuse[0]
mustuse.remove(mustuse[0])
random.shuffle(mustuse)
lista[2][4]=mustuse[0]
mustuse.remove(mustuse[0])
lista[2][5]=mustuse[0]
mustuse.remove(mustuse[0])
'''
#4db 3x3: bal oszlop + középső oszlop felső.


'''

'''












































































for i in range(9):
    for j in range(6):
        print(str(lista[i][j])+", ",end="")
        if j==2 or j==5:
            print(" ",end="")
    if i==2 or i==5:
        print()
    print()





'''





x= lista[0][1]
if x in p:
    p.remove(x)

x= lista[1][1]
if x in p:
    p.remove(x)

x= lista[2][1]
if x in p:
    p.remove(x)




p=[1,2,3,4,5,6,7,8,9]
p.remove(lista[6][0])
p.remove(lista[7][0])
p.remove(lista[8][0])

random.shuffle(p)
lista[6][2]=p[0]
p.remove(p[0])
random.shuffle(p)
lista[7][2]=p[0]
p.remove(p[0])
random.shuffle(p)
lista[8][2]=p[0]
p.remove(p[0])
#3(3x3) rács


p=[1,2,3,4,5,6,7,8,9]
p.remove(lista[3][0])
p.remove(lista[3][1])
p.remove(lista[3][2])
p.remove(lista[3][3])
p.remove(lista[3][4])

if lista[0][4] in p:
    p.remove(lista[0][4])
if lista[1][4] in p:
    p.remove(lista[1][4])
if lista[2][4] in p:
    p.remove(lista[2][4])
random.shuffle(p)
lista[3][4]=p[0]
p.remove(p[0])
#[1][2] elem



for i in range(len(lista)):
    for j in range(len(lista)):
        print(lista[i][j],end=" ")
    print()
    

LEGUTOLSÓ:

p=[1,2,3,4,5,6,7,8,9]
p.remove(lista[3][0])
p.remove(lista[3][1])
p.remove(lista[3][2])
p.remove(lista[3][3])
p.remove(lista[3][4])

if lista[0][5] in p:
    p.remove(lista[0][5])
if lista[1][5] in p:
    p.remove(lista[1][5])
if lista[2][5] in p:
    p.remove(lista[2][5])
if lista[4][3] in p:
    p.remove(lista[4][3])
if lista[5][3] in p:
    p.remove(lista[5][3])
if lista[4][4] in p:
    p.remove(lista[4][4])
if lista[5][4] in p:
    p.remove(lista[5][4])
random.shuffle(p)
lista[3][5]=p[0]
p.remove(p[0])
#[3][5] elem

p=[1,2,3,4,5,6,7,8,9]
p.remove(lista[4][0])
p.remove(lista[4][1])
p.remove(lista[4][2])
p.remove(lista[4][3])
p.remove(lista[4][4])

if lista[0][5] in p:
    p.remove(lista[0][5])
if lista[1][5] in p:
    p.remove(lista[1][5])
if lista[2][5] in p:
    p.remove(lista[2][5])
if lista[3][5] in p:
    p.remove(lista[3][5])
if lista[3][3] in p:
    p.remove(lista[3][3])
if lista[5][3] in p:
    p.remove(lista[5][3])
if lista[3][4] in p:
    p.remove(lista[3][4])
if lista[5][4] in p:
    p.remove(lista[5][4])
random.shuffle(p)
lista[4][5]=p[0]
p.remove(p[0])
#[4][5] elem



p=[1,2,3,4,5,6,7,8,9]
p.remove(lista[5][0])
p.remove(lista[5][1])
p.remove(lista[5][2])
p.remove(lista[5][3])
p.remove(lista[5][4])

if lista[0][5] in p:
    p.remove(lista[0][5])
if lista[1][5] in p:
    p.remove(lista[1][5])
if lista[2][5] in p:
    p.remove(lista[2][5])
if lista[3][5] in p:
    p.remove(lista[3][5])
if lista[4][5] in p:
    p.remove(lista[4][5])
if lista[3][3] in p:
    p.remove(lista[3][3])
if lista[3][4] in p:
    p.remove(lista[3][4])
if lista[4][3] in p:
    p.remove(lista[4][3])   
if lista[4][4] in p:
    p.remove(lista[4][4])
random.shuffle(p)
lista[5][5]=p[0]
p.remove(p[0])
#[5][5] elem
#ezzel bezárólag 5 3x3 : bal oldal, középső oszlop felső 2

#YOU CAN DO IT

p=[1,2,3,4,5,6,7,8,9]
p.remove(lista[0][3])
p.remove(lista[1][3])
p.remove(lista[2][3])
p.remove(lista[3][3])
p.remove(lista[4][3])
p.remove(lista[5][3])

if lista[6][0] in p:
    p.remove(lista[6][0])
if lista[6][1] in p:
    p.remove(lista[6][1])
if lista[6][2] in p:
    p.remove(lista[6][2])
random.shuffle(p)
lista[6][3]=p[0]
p.remove(p[0])
#[6][3] elem


p=[1,2,3,4,5,6,7,8,9]
p.remove(lista[0][3])
p.remove(lista[1][3])
p.remove(lista[2][3])
p.remove(lista[3][3])
p.remove(lista[4][3])
p.remove(lista[5][3])
p.remove(lista[6][3])

if lista[7][0] in p:
    p.remove(lista[7][0])
if lista[7][1] in p:
    p.remove(lista[7][1])
if lista[7][2] in p:
    p.remove(lista[7][2])
random.shuffle(p)
lista[7][3]=p[0]
p.remove(p[0])
#[7][3] elem

p=[1,2,3,4,5,6,7,8,9]
p.remove(lista[0][3])
p.remove(lista[1][3])
p.remove(lista[2][3])
p.remove(lista[3][3])
p.remove(lista[4][3])
p.remove(lista[5][3])
p.remove(lista[6][3])
p.remove(lista[7][3])
if lista[8][0] in p:
    p.remove(lista[8][0])
if lista[8][1] in p:
    p.remove(lista[8][1])
if lista[8][2] in p:
    p.remove(lista[8][2])
random.shuffle(p)
lista[8][3]=p[0]
p.remove(p[0])
#[8][3] elem










'''