list = [1, 2, 3]

tuple = (1, "İki", 3)

print(type(list))
print(type(tuple))

print(list[2])
print(tuple[2])

print(len(list))
print(len(tuple))

list = ["ali", "veli"]
tuple = ("damla", "ayşe")

print(list)
print(tuple)

list[0] = "ahmet"
#tuple nesnesinin değerlerine sonradan silme, ekleme, güncelleme işlemi yapılamaz sadece tamamı silinip yeni bir liste eklenebilir
#tuple[0] = "deniz"

print(list)
print(tuple)

print(tuple.count("ayşe"))
print(tuple.index("ayşe"))

names = ("demet", "emel", "ayşe") + tuple
print(names)