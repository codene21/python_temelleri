'''
    x = input('1. sayı: ')
    y = input('2. sayi: ')
    print(type(x))
    print(type(y))
    toplam = int(x) + int(y)
    print(type(x))
    print(type(y))
    print(toplam)
'''

x = 5 
y = 2.5 
name= "Çınar"
isOnline = True

# print(type(x))
# print(type(y))
# print(type(name))
# print(type(isOnline))

# Type Conversion

# int to float
# x = float(x)
# print(x)
# print(type(x))

# float to int
# y = int(y)
# print(y)
# print(type(y))

# result = str(x) + str(y)
# print(result)
# print(type(result))

# bool to str
# isOnline = str(isOnline)
# print(isOnline)
# print(type(isOnline))

# bool to int
# isOnline = int(isOnline)
# print(isOnline)
# print(type(isOnline))

"""
    Daire alanı : pir^2
    Daire Çevre : 2pir

    * Yarı Çapı verilen bir dairenin alan ve çevresini hesaplayınız. (pi : 3.14)
"""

pi = 3.14
yariCap = float(input("Yarı çapı giriniz: "))

alan = pi * (yariCap ** 2)
cevre = 2 * pi * yariCap

print("Alan: " + str(alan) + " Çevre: " + str(cevre))