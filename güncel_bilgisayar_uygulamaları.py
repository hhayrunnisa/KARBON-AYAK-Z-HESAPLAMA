# -*- coding: utf-8 -*-
"""güncel bilgisayar uygulamaları

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hcXMk0hntPjjzp-LoiPxXmqFOC_DzC-E
"""

x=input("Merhabalar karbon ayak izinizi öğrenmek ister misiniz?: ")
if x=="evet":
  isim=str(input("Adınız nedir?: "))
  yas=int(input("Kaç yaşındasınız?: "))
  print("Tamam başlayabiliriz.")
print("1) Bir günde üç öğün yemek yenirse karbon ayakizi ne olur? ")
a=(input("Et ve et ürünü tükettiniz mi?: "))
if a =="evet":
 b=float(input("Kaç porsiyon?: "))
 ayakizi1=(b*100)*2.2
else:
  ayakizi1=0
  print("Tamam")
c=(input("Sebze ve Meyve tükettiniz mi?: "))
if c == "evet":
  d=float(input("Kaç porsiyon?: "))
  ayakizi2=(d*80)*0.5
else:
  ayakizi2=0
  print("Tamam")
e=(input("Süt ve süt ürünü tükettiniz mi?: "))
if e == "evet":
  f=float(input("Kaç porsiyon?: "))
  ayakizi3=(f*50)*1.8
else:
  ayakizi3=0
  print("Tamam")
h=(input("Tahıl ve baklagil tükettiniz mi?: "))
if h == "evet":
  k=float(input("Kaç porsiyon?: "))
  ayakizi4=(k*100)*0.2
else:
  ayakizi4=0
  print("Tamam")
  KAİ1a=(ayakizi1 + ayakizi2 + ayakizi3 + ayakizi4)/1000
  print("Bir günde üç öğün yemekle karbon ayak iziniz:",KAİ1a," kg CO2 ")

print("2) Sınıfça derste bilgisayar kullanılırsa karbon ayak izi ne olur?")
a=str(input("Derste masaüstü bilgisayar mı kullanırsınız?: "))
if a== "evet":
  b=int(input("Sınıf mevcudunuz kaçtır?: "))
  c=int(input("Kaç saat kullanıyorsunuz?: "))
  KAİ3a=175*c*b*0.48
  print("karbon ayak iziniz:",KAİ3a," kg CO2 ")
if a=="hayır":
  KAİ3a=0
  print("karbon ayak iziniz:",KAİ3a, "kg CO2")


print("3) Araba ile şehirler arası yolculukta karbon ayak izi ne olur?")
x=int(input("Özel araç ile istanbul'dan Ankara'ya kaç arkadaş gidersiniz?: "))
KAİ2a=32.43*2.9/x
print("karbon ayak iziniz:",KAİ2a," kg CO2")

print("4) Temizlik için elektirikli süpürge kullanılırsa karbon ayak izi ne olur? ")
a=int(input("Bir günde evi temizlemek için kaç dakika evi süpürürsünüz?: "))
b=int(input("Eviniz kaç metrekare?: "))
KAİ3b=((a*b*0.48)/600)
print("karbon ayak iziniz:",KAİ3b," kg CO2 ")

print ("5) Tüketilen kahvenin karbon ayak izi nedir?")
a=str(input("Hergün kahve tüketir misiniz? "))
if a=="evet":
  b=int(input("Bir günde kaç fincan tüketiyorsunuz?: "))
  KAİ1b=(7*b*56)/1000
  print("Karbon ayak iziniz:", KAİ1b ," kg CO2")
else:
  c=int(input("Haftanın kaç günü tüketiyorsunuz?: " ))
  d=int(input("Bir günde kaç fincan tüketiyorsunuz?: "))
  KAİ1b=(c*d*56)/1000
  print("karbon ayak iziniz:",KAİ1b," kg CO2 ")

print("6) Yakılan mangalda pişen kırmızı ve beyaz etin karbon ayak izi nedir? ")
a=float(input("Kaç kg kırmızı et pişirirsiniz?: "))
c=float(input("kaç kg kırmızı et yersiniz?: "))
KAİ1c=a*33.1/c
b=float(input("Kaç kg beyaz et pişirirsiniz?: "))
n=float(input("kaç kilogram beyaz et yersiniz?: "))
KAİ1c1=b*6.9/n
print("karbon ayak iziniz:",KAİ1c+KAİ1c1," kg CO2")

print("7) Kömürden dolayı oluşan karbon ayak izi nedir?")
d=float(input("Mangal yakmak için kaç kg kömür kullanırsınız?: "))
KAİ5a=d*2.870
print("karbon ayak iziniz:",KAİ5a," kg CO2")

print("8) Odun ateşinin karbon ayak izi nedir?")
w=float(input("Kampta ateş etrafında sabaha kadar oturmanız için kaç kg odun gereklidir?:"))
KAİ5b=w*0
print("karbon ayak iziniz:",KAİ5b," kg CO2")

print("9) Alınan duşta oluşan karbon ayak izi nedir?")
a=float(input("Bir günde kaç dakika duş alırsınız?: "))
KAİ3c=float((a*(a*4)*0.2)/1000)
print( "karbon ayak iziniz:",KAİ3c," kg CO2 ")

print("10) Telefonu sarj etmenin karbon ayakizi nedir? ")
a=int(input("Bir günde telefonunuzu kaç saat şarj edersiniz?: "))
KAİ3d=0.004*a*0.48
print("karbon ayak iziniz:",KAİ3d," kg CO2 ")

print("11) Ev-okul arası metrobüs ile yolculukta karbon ayak izi nedir?")
y=float(input("Eviniz ile okul arası kaç km'dir? : "))
KAİ2b=(40*y/100)*2.77
print("karbon ayak iziniz:",KAİ2b," kg CO2")

print("12) Bir günde izlenen televizyonun karbon ayak izi nedir?")
a=float(input("Kaç dakika televizyon izlersiniz?: "))
KAİ3e=(a*1.66)*0.0005
print("karbon ayak iziniz:",KAİ3e," kg CO2")

print("13) Pet şişe ile su kullanımında karbon ayakizi ne kadar olur? ")
a=float(input("Kaç litrelik pet şişe su kullanırsınız?: "))
b=int(input("Günde kaç adet pet şişe su kullanırsınız?: "))
KAİ4a=b*(a/0.5)*0.5*83
print("karbon ayak iziniz:",KAİ4a," kg CO2 ")

print("14) İstanbul-Eskişehir arası 409 kişi kapasiteli tren ile yolculuk yapıldığında karbon ayak izi ne olur? ")
b=int(input("Günü birlik Eskişehir yolculuğunda tren içerisinde sizce kaç yolcu vardır?: "))
KAİ2c=299*0.064/b
print("karbon ayak iziniz:",KAİ2c," kg CO2")

print("15) Saç kurutma makinesi kullanılırsa karbon ayakizi ne kadar olur? ")
a=float(input("Kaç dakika boyunca saç kurutma makinesini kullanırsınız?: "))
KAİ3f=(a*0.005*0.48)
print( "karbon ayak iziniz:",KAİ3f,"kg CO2")

print("16) Poğaça tüketiminde karbon ayak izi nedir?")
a=str(input("Genelde sabahları poğaça tüketir misiniz?: "))
if a=="evet":
 b=int(input("Kaç adet?: "))
 KAİ1d=(70*b*0.2)/1000
 print("karbon ayak iziniz:",KAİ1d ," kg CO2")
else:
  KAİ1d=0
print("Karbon ayak iziniz:",KAİ1d," kg CO2")

print("17) Bisiklet ile evden en yakın oyun parkına giderken karbon ayak izi ne olur?")
f=float(input("Eviniz ile en yakın oyun parkı arası kaç km'dir?: "))
KAİ2d=f*0
print("karbon ayak iziniz:",KAİ2d," kg CO2")

print("18) Ortalama kullanım ile yaktığım doğalgaz ne kadar karbon ayak izi olur? ")
a=float(input("Günde kaç saat doğal gaz yakarsınız?: "))
KAİ5c=(a*0.625*0.25)
print( "karbon ayak iziniz:",KAİ5c," kg CO2")

print("19) Bir günde tüketilen yoğurdun karbon ayak izi nedir?")
c=float(input("kaç kase yoğurt tüketirsiniz?: "))
KAİ1e=((c*150*1.8)/1000)
print("karbon ayak iziniz:",KAİ1e," kg CO2")

print("20) Bir kişinin bir günde uçak ile yaptığı karbon ayak izi nedir? ")
a=float(input("Uçak ile memleketinize gitseniz kaç saat yolculuk yapmış olursunuz? : "))
KAİ2e=a*182/329
print("karbon ayak iziniz:",KAİ2e," kg CO2")

print("21) Bir günde çalıştırılan çamaşır makinesinin karbon ayak izi nedir? ")
dt=float(input("Çamaşır makinesini bir günde kaç saat çalıştırırsını?: "))
KAİ3g=(0.275*dt*0.48)
print("karbon ayak iziniz:",KAİ3g," kg CO2")

print("22) Sabah tüketilen peynirin karbon ayak izi nedir?")
d=float(input("Sabahları kaç gram peynir tüketirsiniz?: "))
KAİ1f=((d*1.8)/1000)
print("karbon ayak iziniz:",KAİ1f," kg CO2")

print("23) Taksi ile yolculukta oluşan karbon ayak izi nedir?")
t=float(input("Teknoloji Fuarı için okuldan İstanbul Fuar Merkezine giden taksiye kaç arkadaşınızı alırsınız?: "))
KAİ2f=1.1096 *3/(t+2)
print("karbon ayak iziniz:",KAİ2f," kg CO2")

print("24) Gün içerisinde tüketilen sütün karbon ayak izi nedir?: ")
c=float(input("Günde kaç bardak süt tüketirsiniz?: "))
KAİ1g=((c*240*1.8)/1000)
print("karbon ayak iziniz:",KAİ1g," kg CO2")

print("25) Alışverişte plastik poşet kullanılırsa karbon ayak izi ne olur?")
a=input("Marketlerde alışveriş yaparken plastik poşet kullanır mısınız?: ")
if a=="evet":
 b=float(input("Kaç adet kullanırsınız?: "))
 KAİ4b=7.6*(10**-6)*b*3328.4
else:
  KAİ=0
print("karbon ayak iziniz:",KAİ4b," kg CO2")

import matplotlib.pyplot as plt
liste=[(KAİ1a+KAİ1b+(KAİ1c+KAİ1c1)+KAİ1d+KAİ1e+KAİ1f+KAİ1g),(KAİ2a+KAİ2b+KAİ2c+KAİ2d+KAİ2e+KAİ2f),(KAİ3a+KAİ3b+KAİ3c+KAİ3d+KAİ3e+KAİ3f+KAİ3g),(KAİ4a+KAİ4b),(KAİ5a+KAİ5b+KAİ5c)]
renkler=["orange","red","purple","green","blue"]
etiketler=["yiyecek ve içecek","taşıt kullanımı","elektirikli alet kullanımı","plastik kullanımı","ısınma"]
exp=[0,0.2,0,0,0.2]
plt.pie(liste, colors = renkler, labels = etiketler, explode = exp ,autopct='%.1f%%' )
plt.title('KARBON AYAK İZİ DAİRE GRAFİĞİ')