website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python programlama Rehberiniz (40 saat)"

# 1- "course" karakter dizisinde kaç karakter bulunmaktadır?
print(len(course))

# 2- "website" içinden www karakterlerini alın.

print(website[7:10])

# 3- "website" içinden com karakterlerini alın

print(website[-3:])

# 4- "course" içinden ilk 15 ve son 15 karakter dizilerini alın

print(course[:15] + " " + course[-15:])

# 5- "course" ifadesindeki karakterleri tersten yazdırın

print("Tersten yazılışı: ", course[::-1])  # *** ÖNEMLİ: tersten yazdırmak için kullandığımız kod

name, surname, age, job = "Busra", "Yalinkilic", 21, "ogrenci"

# 6- "benim adım büşra yalınkılıç, yaşım 21 ve mesleğim öğrenci." ifadesini yazdır.

print(f"Benim adım {name} {surname}, yaşım {age} ve mesleğim {job}")

# 7- "Hello world" ifadesindeki w harfini "W" ile değiştirin
x= "Hello world" #w ifadesi 6. index
x= x[0:6] + "W" + x[-4:]
print(x)

#kolay yolu:
#x.replace("w","W")


#"abc" ifadesini yan yana 3 kere yazdırın.
s="abc " * 3
print(s)