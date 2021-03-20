"""
     ogrenciler= {
         "120": {
             "ad" : "Ali",
             "soyad" : "Yılmaz",
             "telefon" : "532 000 00 01"
         },
         "125": {
              "ad" : "Can",
             "soyad" : "Korkmaz",
             "telefon" : "532 000 00 02"
         },
         "128" : {
              "ad" : "Volkan",
             "soyad" : "Yukselen",
             "telefon" : "532 000 00 03"
         },
     }

     1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary 
     içinde saklayınız.

     2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.    
"""

ogrenciler = {}

number = input("ogrenci no: ")
name = input("ogrenci adi: ")
surname = input("ogrenci soyadi: ")
phone = input("ogrenci telefon: ")

# ogrenciler[number] = {
#     "ad" : name,
#     "soyad" : surname,
#     "telefon" : phone
# }
# aynı işlem :
ogrenciler.update({
    number:{
        "ad" : name,
        "soyad" : surname,
        "telefon" : phone  
}
})
#döngüleri görmediğimiz için 3 öğrenci için aynı işlemleri 3 kez yaparız
print("*"*50)

# 2. cevap

ogrNo = input("ogrenci no: ")
ogrenci = ogrenciler[ogrNo]
print(f"Aradiginiz {ogrNo} nolu ogrencinin adi {ogrenci['ad']} soyadi {ogrenci[ 'soyad' ]} ve telefon no {ogrenci[ 'telefon' ]}")