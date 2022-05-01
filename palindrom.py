#palindrom kelime olup olmadığını kontrol eden uygulama

wordss = input("lütfen bir yazı giriniz : ")

for i in range(len(wordss)):
    re_word=wordss[::-1]

print(re_word)
if(wordss==re_word) :
    print("Palindrom kelimedir.")
else : 
    print("Palindrom kelime değildir.")

