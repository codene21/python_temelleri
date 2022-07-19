plakalar = {'kocaeli': 41, 'istanbul' : 34}
print(plakalar['istanbul'])
plakalar ['ankara'] = 6
print(plakalar)

users = {
    'mehmetşimşek' : {'age': 36, 'roles': ['user'], 'email': 'mehmet@simsek.com', 'address': 'kocaeli', 'phone': '1234124234'},
    'kadirturan' : {'age': 20, 'roles': ['admin', 'user'], 'email': 'kadir@turan.com', 'address': 'istanbul', 'phone': '0980980980'}
}
print(users['mehmetşimşek'])
print(users['mehmetşimşek']['email'])
print(users['kadirturan']['roles'])

#Uygulama
'''
ogrenciler = {
    '120': {
        'ad': 'Ali',
        'soyad': 'Yılmaz',
        'telefon': '500 000 00 01'
    },
    '125': {
        'ad': 'Can',
        'soyad': 'Korkmaz',
        'telefon': '500 000 00 02'
    },
    '128': {
        'ad': 'Volkan',
        'soyad': 'Yükselen',
        'telefon': '500 000 00 03'
    }
}
'''

# 1 - Bilgileri verilen öğrencileri kullanıcıdan adlığınız bilgilerle dictionary içinde saklayınız.

ogrenciler = {}

number = input("Öğrenci numarasını giriniz: ")
name = input("Öğrenci adını giriniz: ")
surname = input("Öğrenci soyadını giriniz: ")
phone = input("Öğrenci telefon numarasını giriniz: ")

# ogrenciler[number] = {'ad': name, 'soyad': surname, 'telefon': phone}

ogrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon': phone
    }
})
number = input("Öğrenci numarasını giriniz: ")
name = input("Öğrenci adını giriniz: ")
surname = input("Öğrenci soyadını giriniz: ")
phone = input("Öğrenci telefon numarasını giriniz: ")

ogrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon': phone
    }
})
number = input("Öğrenci numarasını giriniz: ")
name = input("Öğrenci adını giriniz: ")
surname = input("Öğrenci soyadını giriniz: ")
phone = input("Öğrenci telefon numarasını giriniz: ")

ogrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon': phone
    }
})

print(ogrenciler)
print('*'*50)

# 2 - Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.

ogrNo = input("Öğrenci numasını giriniz.")
ogrenci = ogrenciler[ogrNo]

print(f"Aradığınız {ogrNo} nolu öğrencinin adı: {ogrenci['ad']}, soyadı: {ogrenci['soyad']} ve telefonu  ise {ogrenci['telefon']}")