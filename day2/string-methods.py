message = " Hello there. My name is Busra Yalinkilic"
#message= message.upper()    #tüm karakterleri büyük harfe çevirir
# message= message.lower()     #küçük harfe çevirir
#message= message.title()   #her kelimenin baş harfi büyük olur
#message= message.capitalize()  #sadece ilk harf büyük oldu


#message= message.strip() #başlangıçta eğer bir boşluk karakteri varsa ki ben şuan ekledim, onu yok etmek için kullanılır
message= message.split()  #cümleyi parçalara ayırdı. Çıktı:['Hello', 'there.', 'My', 'name', 'is', 'Busra', 'Yalinkilic']
#message= message.split('.') #noktadan itibaren ayıracak. Çıktı: [' Hello there', ' My name is Busra Yalinkilic']

message= " ".join(message) #ayrı olarak gelen bilgileri tekrar birleştirmek istiyoruz.


print(message)
#print(message[2]) #split komutu ile birlikte kullanıldığında 2. tırnak içinde ki ifadeyi alır yani my