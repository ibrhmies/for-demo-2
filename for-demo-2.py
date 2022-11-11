urunler = [
    {'name':'iphone 8', 'price': '4000'},
    {'name':'iphone 8 Plus', 'price': '5000'},
    {'name':'iphone X', 'price': '6000'},
    {'name':'iphone XR', 'price': '7000'},
    {'name':'iphone 11(kaçak)', 'price': '8000'},
    {'name':'samsung s10', 'price': '6000'},
]

#1-> tüm ürün bilgilerini listeleyiniz.

for i in urunler:
    print(i)


#2-> ürünlerin fiyatları toplamı nedir
top = 0
for i in urunler:
    top=top + int(i['price']) #i değeri içindeki hangi kısmı almak istiyorsak[] içine yazıyoruz dictionary liste türü için geçerli
print(top)   # burda str bi veriyi int cevirmek için başına int yazdık yoksa işlemi yapamazdık


#3->ürünlerin fiyatı en az 6000 olanları gösteriniz.

for i in urunler:
    if(int(i['price'])>= 6000):
        print(i)

#4-> kullanıcıdan alınan anahtar kelimeyi içeren ürünü gösteriniz.

name = input("telefon ismini giriniz: ")

for i in urunler:
    if (name == i['name']):
        print(i)


