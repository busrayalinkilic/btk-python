# 1- value types => string, number(int,float)
x = 5
y = 25

x = y
y = 10

print(x,y)  #atama yaptıktan sonra y'nin değerinin güncellenmesi x'i etkilemez

# 2- references types => list, class
a= ["apple", "banana"]
b= ["apple", "banana"]

a = b
b[0] = "grape" #yaptığımız değişiklik a'yı da etkiledi
print(a,b)  # çıktı: ['grape', 'banana'] ['grape', 'banana']