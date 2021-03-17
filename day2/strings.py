name = "Busra"  #ister tek tırnak ister çift tırnak içinde tanımlayabiliriz
surname = "Yalinkilic"
age= "21" # bu şekilde yazarsam direk + age şeklinde kullanabilirim
#age= 21 # bu şekilde yazarsam print içinde ki age ifadesini str(age) şeklinde tanımlamam lazım


#print("My name is " + name + " " + surname + " and \nI am " + age + " years old.")

greeting= "My name is " + name + " " + surname + " and \nI am " + age + " years old." 
#greetin=selamlama biraz da english

length = len(greeting) #en başta uzunluğu hesaplayıp bir değişkene atadık
 
# #print(greeting)
# print(greeting[11]) #string ifadade ki 11. karakteri yazdırır
# #print(len(greeting)) # greeting ifadesinin kaç karakterli olduğunu görmemizi sağlayan komut
# print(greeting[length-1]) #-1 deme nedenimiz saymaya sıfırdan başlıyor olmamız.

# #son karakteri bulmaya alternatif olarak:
# print(greeting[-1])

#print(greeting[2:5]) #2. indexten başla 5. indexe kadar git manasında kullanılır.
#  : şaretinden sonra bir bitiş noktası koymazsak sona kadar yazar. ya da öncesinde ifade koymayıp bitiş ifadesi koyabiliriz


print(greeting[2:40:2]) # 2 den 40a kadar gider ama ikişer ikişer ilerler 