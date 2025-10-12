# Kérjen be egy egész számot és döntse el hogy páros vagy páratlan

# szam = int (input ("Adj megy egy egész számot")

# kérjen be a felhasználótol egy számot és mondja meg hogy 10-zel osztható e? ha nem osztható 10-zel írja ki az utolsó számjegyét

#pl be:10 ki: tízzel osztható
# pl. be: 12 ki: tízzel nem oszthaó utolsó számjegy 2

import math
import random

szam = int(input("Adjon megy egy számot :"))

if(szam % 10 == 0):
     print ("Osztható")
else:
     print ("Nem Osztható")
     print ("az utolsó számjegy: " + str (szam % 10))

# Kérjen be egy másik számot és irassa ki a 2 szám reciprokának összegét
szam2 = int(input("Adjon meg egy másik számot :"))
if(szam != 0):
     if(szam2 != 0):
          rec = 1/szam
          rec2 = 1/szam2
          print (rec+rec2)
     else:
          print("a második számnak nincs reciproka")
else:
     print("Az első számnak nincs reciproka")     

# Adja meg a 2 számnak a gyökét
if (szam + szam2 >=0):
     print (math.sqrt(szam+szam2))
else:
     print("A 2 szám összege negatív")
     
# and , or, xor,!(not)
if (szam != 0 and szam2 !=0):
          rec = 1/szam
          rec2 = 1/szam2
          print (rec+rec2)
else:
     print("A két szám valamelyike nulla!")
# HF bool algebra
# kérjen be a felhasználótol 3 darab számot lehet tört is ez a 3 szám egy 3 szög 3 oldala 
# 1. derékszög e a háromszög 
# 2. egyenlő szárú e a háromszög
# 3. szabályos e a háromszög
# Három oldal bekérése
a = int(input("Add meg az első oldalt: "))
b = int(input("Add meg a második oldalt: "))
c = int(input("Add meg a harmadik oldalt: "))

if a + b > c and a + c > b and b + c > a:
    print("Ez egy érvényes háromszög.")

    if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
        print("Derékszögű háromszög.")
    else:
        print("Nem derékszögű háromszög.")
    if a == b or a == c or b == c:
        print("Egyenlő szárú háromszög.")
    else:
        print("Nem egyenlő szárú háromszög.")
    if a == b and b == c:
        print("Szabályos háromszög.")
    else:
        print("Nem szabályos háromszög.")

# hf python ciklusoknak utanna nézése

# generáljon ki 3  háromjegyű véletlenszerű számot amelyek 13-al oszthatók
# adja meg az átlagukat
#állytsa ezeket sorrendbe 
#van e köztük 4-el végződő

szam1 = random.randint(100, 999)
szam2 = random.randint(100, 999)
szam3 = random.randint(100, 999)

szamok = [szam1, szam2, szam3]

for i in range(3):
    if szamok[i] % 13 != 0:
        print(f"A(z) {szamok[i]} szám nem osztható 13-mal.")
    else:
        print(f"A(z) {szamok[i]} szám osztható 13-mal.")

atlag = sum(szamok) / 3
print("A számok átlaga:", atlag)

szamok.sort()
print("Sorrendbe állítva:", szamok)

van_4 = False
for sz in szamok:
    if sz % 10 == 4:
        van_4 = True
        break

if van_4:
    print("Van köztük 4-re végződő szám.")
else:
    print("Nincs köztük 4-re végződő szám.")
