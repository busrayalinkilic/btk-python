# x = 5
# y = 10
# z = 20
#  #ya da;

x, y, z = 5, 16 ,20

# x, y = y, x #x'in içerisine y, y'nin içerisine x yazılır
 #x'in var olan değeri ile 5 toplanır ve x'e yazılır. yani x artık 10
x += 5   # x = x + 5 
x -= 5   # x = x - 5 
x -= 5   # x = x - 5 
x *= 5   # x = x * 5 
x /= 5   # x = x / 5 
x %= 5   # x = x % 5 
y //= 5   # y = y // 5 
y **= 5   # y = y ** 5 
y **= z  # y = y ** z


# values = 1, 2, 3 
# print(values)
# print(type(values)) #<class 'tuple'>

# x, y, z = values
# print(x, y, z) #çıktı =1 2 3
# #eğer z yi burada yazıp 3 değerini silersek yani 2 atanacek değer 3 değişken kalırsa hata alınır
# #eğer fazla aranacak değer yani values=1, 2, 3, 4, 5 vs olsa yine hata alınır şöyle olursa;

values = 1, 2, 3, 4, 5
print(values)
print(type(values)) #<class 'tuple'>

x, y, *z = values
print(x, y, z)   #başına * ekleyince çıktı: 1 2 [3, 4, 5]
#z için bir liste oluşturulmuş olunur