numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a', 'g', 's', 'b', 'y', 'a', 's']

print(min(numbers))
print(max(numbers))
print(max(letters))
print(min(letters))
print(numbers[3:6])
print(numbers[:3])
print(numbers[4:])
numbers[4]=40
print(numbers)
numbers.append(49)
print(numbers)
numbers.insert(3, 78)
print(numbers)
numbers.insert(-1, 52)
print(numbers)
numbers.pop()
print(numbers)
numbers.pop(1)
print(numbers)
numbers.remove(9)
print(numbers)
numbers.sort()
print(numbers)
letters.sort()
letters.reverse()
print(letters)
print(len(numbers))
print(len(letters))
print(numbers.count(10))
print(letters.count('a'))
numbers.clear()
print(numbers)

#Uygulama

names = ['Ali', 'Yağmur', 'Hakan', 'Deniz']
years = [1998, 2000, 1998, 1987]

#1 - "Cenk" ismini listenin sonuna ekleyiniz.
names.append("Cenk")

#2 - "Sena" değerini listenin başına ekleyiniz.
names.insert(0, "Sena")

#3 - "Deniz" isminin indeksi nedir?
print(names.index("Deniz"))

#4 - "Deniz" ismini listeden siliniz.
names.remove("Deniz")

#5 - "Ali" listenin bir elemanı mıdır?
print("Ali" in names)
print(names.index("Ali"))

#6 - Liste elemanlarını ters çevirin.
names.reverse()
years.reverse()

#7 - Liste elemanlarını alfabetik olarak sıralayınız.
names.sort()

#8 - years listesini rakamsal büyüklüğe göre sıralayınız.
years.sort()

#9 - str = "Chevrolet, Dacia" karakter dizisini listeye çeviriniz.
str = "Chevrolet, Dacia"
otomobiller = str.split(",")
print(otomobiller)

#10 - years dizisinin en büyük ve en küçük elemanı nedir?
min(years)
max(years)

#11 - years dizisinde kaç tane 1998 değeri vardır?
print(years.count(1998))

#12 - years dizisinin tüm elemanlarını siliniz.
years.clear()

#13 - kullanıcıdan alacaağınız 3 tane marka bilgisini bir listede saklayınız.
marka1 = input("Birinci markayı giriniz: ")
marka2 = input("İkinci markayı giriniz: ")
marka3 = input("Üçüncü markayı giriniz: ")
markalar = [marka1, marka2, marka3]
print(markalar)