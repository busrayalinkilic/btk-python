# x = input('1. sayi: ')
# y = input('2. sayi ')

# print(type(x))
# print(type(y))
# toplam= int(x) + int(y)
# print(toplam)


x= 5     #int
y = 2.5    #float
name= 'Busra'   #string
isOnline= True    #bool

# print(type(x))
# print(type(y))
# print(type(name))
# print(type(isOnline))


# tip dönüştürme
# 1- int to float

# x=float(x)
# print(x)
# print(type(x))

#2- float to int 
# y=int(y)
# print(y)


# result= x+y
# print(result)
# print(type(result))        #işlem içine girenlerden en azından biri float olduğun için sonucunda tipi floattır.

# result= str(x)+ str(y)
# print(result)
# print(type(result))              # sonuç= 52.5 type str


#bool to str

# isOnline = str(isOnline)
# print(isOnline)
# print(type(isOnline))  

#bool to int
isOnline = int(isOnline)
print(isOnline)
print(type(isOnline))       #sonuç=1, eğer isOnlineı false yaparsak sonuç 0 olacaktı.
