import random


grade = random.randint(1, 5)
print("Érdemjegy:", grade)

if grade == 1:
    print("Elégtelen")
else:
    if grade == 2:
        print("Elégséges")
    else:
        if grade == 3:
            print("Közepes")
        else:
            if grade == 4:
                print("Jó")
            else:
                print("Jeles")


temp = random.randint(-50, 150)
print("Hőmérséklet:", temp, "°C")

if temp <= 0:
    print("Szilárd (jég)")
else:
    if temp < 100:
        print("Folyékony")
    else:
        print("Gáz (gőz)")


a = random.randint(1, 30)
b = random.randint(1, 30)
c = random.randint(1, 30)
print("Oldalak:", a, b, c)

if a + b > c:
    if a + c > b:
        if b + c > a:
            print("Szerkeszthető háromszög")
        else:
            print("Nem szerkeszthető")
    else:
        print("Nem szerkeszthető")
else:
    print("Nem szerkeszthető")

fahrenheit = random.randint(-40, 212)
celsius = (fahrenheit - 32) * 5 / 9
print(f"{fahrenheit} °F = {celsius:.2f} °C")

celsius2 = random.randint(-30, 100)
fahrenheit2 = (celsius2 * 9 / 5) + 32
print(f"{celsius2} °C = {fahrenheit2:.2f} °F")

total_seconds = input("Írd be az időt másodpercben: ")

try:
    total_seconds = int(total_seconds)
    if total_seconds < 0:
        print("Kérlek adj meg egy pozitív számot!")
    else:
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        print(f"{hours} óra, {minutes} perc, {seconds} másodperc")
except ValueError:
    print("Kérlek számot adj meg!")
