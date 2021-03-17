'''
 daire alanı : πr^2
 daire çevresi : 2πr

 Soru: Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız (r=3.14)
 '''
pi = 3.14

r= float(input("yarı cap: "))

alan= pi * (r**2)
cevre=2 * pi * r

print("alan: "+ str(alan) + " cevre: " + str(cevre))
#print("cevre:", cevre)