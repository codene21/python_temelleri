my_list = [1,2,3]
print(my_list)
my_list = ['bir', 2, True, 5.6]
print(my_list)

list1 = ['one', 'two', 'three']
list2 = ['four', 'five', 'six']
numbers = list1 + list2
print(numbers)
print(len(numbers))
print(numbers[2])

userA = ['Thor', 1500]
userB = ['Captain America', 125]
users = [userA, userB]
print(users[1][0])

#Listeler uygulama
# 1 - "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz
cars = ['Bmw', 'Mercedes', 'Opel', 'Mazda']

# 2 - Liste kaç elemanlıdır
print(len(cars))

# 3 - Listenin ilk ve son elemanı nedir
print(cars[0], cars[len(cars)-1])

# 4 - Mazda değerini Toyota ile değiştirin
cars[-1] = "Toyota"
print(cars)

# 5 - Mercedes listenin bir elemanı mıdır
print("Mercedes" in cars)

# 6 - Listenin -2 indeksindeki değer nedir
print(cars[-2])

# 7 - Listenin ilk üç elemanını alın
print(cars[:3])

# 8 - Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin
cars[-2:] = ["Toyota", "Renault"]
print(cars)

# 9 - Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin
print(cars + ["Audi", "Nissan"])

# 10 - Listenin son elemanını silin
del cars[-1]
print(cars)

# 11 - Liste elemanlarını tersten yazdırınız
print(cars[::-1])

# 12 - Aşağıdaki verileri bir liste içinde saklayınız
studentA = ["Yiğit", "Bilgi", 2010, [70,60,70]]
studentB = ["Sena", "Turan", 1999, [80,80,70]]
studentC = ["Ahmet", "Turan", 1998, [80,70,90]]

# 13 - Liste elemanlarını ekrana yazdırınız
print(studentA[0])
print(studentB[2])
print(studentC[3])
print(studentC[3][1])

result = f"{studentA[0]} {studentA[1]} {2022 - studentA[2]} yaşında ve not ortalamsı {(studentA[3][0]+studentA[3][1]+studentA[3][2])/3}"
print(result)