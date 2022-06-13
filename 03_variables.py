maasAli = 5000
maasAhmet = 4000
vergi = 0.27

print(maasAli - (maasAli * vergi))
print(maasAhmet - (maasAhmet * vergi))

# Değişken Tanımlama Kuralları

# Rakam ile başlayamaz
# Aynı değişken ismi bir kere tanımlanabilir ikincisinde sadece önceki değişkenin değer ataması yapılır
# Büyük küçük harf duyarlılığı vardır
# Türkçe karakter kullanılmaz
# Değişken isimleri arasında boşluk olamaz
# Birden fazla değişken tek satırda tanımlanabilir

# Uygulama

"""
    1- Bir Müşterinin aşağıdaki bilgileri için değişken oluşturunuz.

    Müşteri adı
    Müşteri soyadı
    Müşteri ad + soyad
    Müşteri cinsiyet
    Müşteri Tc Kimlik
    Müşteri doğum yılı
    Müşteri adres bilgileri
    Müşteri yaşı
"""

musteriAdi = "Selma"
musteriSoyadi = "Polat"
musteriAdiSoyadi = musteriAdi + " " + musteriSoyadi
musteriCinsiyet = False # => Kadın
musteriTcKimlik = "01020293094"
musteriDogumYili = 1996
musteriAdresi = "Yenimahalle Şentepe"
musteriYasi = 2022 - musteriDogumYili
print(musteriYasi)

"""
    2- Aşağıdaki siparişlerin toplam bilgisini hesaplayınız.

    Sipariş 1 => 110 TL
    Sipariş 2 => 1100.5 TL
    Sipariş 3 => 356.95 TL
"""

siparis1 = 110
siparis2 = 1100.5
siparis3 = 356.95
siparisToplam = siparis1 + siparis2 + siparis3
print("Sipariş Toplamı: ", siparisToplam)