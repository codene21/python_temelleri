message = "Hello there. My name is Darth Vader."

print(message)

#Tüm harfler büyük
print(message.upper())

#Tüm harfler küçük
print(message.lower())

#Her Kelimenin baş harfi büyük
print(message.title())

#Sadece ilk harf büyük
print(message.capitalize())

password = " password"
#Baş ve sondaki boşluk karakterini siler (sağdan rstrip(), soldan lstrip())
print(message.strip())

#Boşluk karakterlerinden parçalayıp her bir parçayı bir diziye ekler
print(message.split())

#Belirtilen karakterden ayırıp her parçayı bir diziye ekler
print(message.split('.'))

#Diziyi tek bir string haline getirir.
print("**".join(message.split()))

#String değişkeni içinde değer arayarak indexi bulur
print(message.find("Darth"))

#String değişkenin başlangıç değerini sorgular
print(message.startswith("H"))

#String değişkenin son değerini sorgular
print(message.endswith("r"))

#String değişkenin içinde bulunan değeri değitirir
print(message.replace("Darth Vader", "Obi-Wan Kenobi"))
print(message.replace(" ","*").replace(".",""))

#String değişkeni belirtilen karakter sayısına eşitlenir ve değer ortalanır
print(message.center(100))
print(message.center(100,"*"))

#Uygulama

website = "http://www.darthvader.com"
course = "Star Wars Tarihi: Baştan Sona Star Wars Hikayeleri"

# 1 - ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
print(" Hello World ".strip())

# 2 - 'www.darthvader.com' içindeki darthvader haricindeki her karakteri silin
print("www.darthvader.com".replace("www.","").replace(".com",""))
print("www.darthwader.com".strip("w.com"))

# 3 - 'course' karakter dizisinin tüm karakterlerini büyük harf yapın
print(course.upper())

# 4 - 'website' içinde kaç tane a karakteri var bulun
print(website.count('a'))
print(website.count("a",0,16)) #arama için aralık berlirtilebilir

# 5 - 'website' www ile başlayıp com ile bitiyor mu
print(website.startswith("www"), website.endswith("com"))

# 6 - 'website' içinde .com ifadesi var mı
print(website.find(".com"))
print(website.index(".com"))
print(website.find(".com",0,10)) # belirtilen aralıkta arama yapar

# 7 - 'course' içindeki karakterlerin hepsi alfabetik mi?
print(course.replace(" ","").replace(":","").isalpha(), course.isdigit())

# 8 - 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz
print("Contents".center(50,"*"))
print("Contents".ljust(50,"*")) # sola yaslar
print("Contents".rjust(50,"*")) # sağa yaslar

# 9 - 'course' karakter dizisindeki tüm boşluk karakterleri '-' ile değiştirin
print(course.replace(" ","-"))
print(course.replace(" ","-",3)) # kaç karakteri değiştireceğimizi seçebiliriz

# 10 - 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin
print("Hello World".replace("World", "There"))

# 11 - 'course' karakter dizisini boşluk karakterlerinden ayırın
print(course.split())