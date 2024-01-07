import random
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
sifre_uzunluğu = int(input("Şifre uzunluğunu giriniz:"))
sifre = ""
for i in range(sifre_uzunluğu):
    sifre += random.choice(karakterler)
print(sifre)    
