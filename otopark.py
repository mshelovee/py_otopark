#Bir otoparkta ücret tarifesi aşağıdaki gibidir.
#1-3 saate kadar 10 TL
#3-5 saate kadar 15 TL
#5 saatten fazla ise 30 TL 
#Klavyeden kullanıcının otoparkta kaldığı süre girilecek ve ödenmesi gereken 
#ücret ekranda gösterilecektir. Gerekli programı yapınız.

saat=int(input("Aracınızın otoparkta kaç saat kaldığını yazınız: "))
if saat<2:
   print("10 TL Ödenir.")
elif saat<6:
   print("15 TL Ödenir.")
else:
   print("30 TL Ödenir.")