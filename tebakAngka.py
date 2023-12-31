# import library
import random
import math

# Buat inputan angka nya
lower = int(input("Masukan angka terendah: "))
upper = int(input("Masukan angka tertinggi: "))

# ini buat bikin angka acak dari si lower sama upper nya
x = random.randint(lower, upper)
print("\n\tKamu cuman punya ", 
    round(math.log(upper - lower + 1,2 )), 
    " Kesempatan buat nebak ini!\n")

count = 0 

while count < math.log(upper - lower + 1,2 ):
    count += 1 

    guess = int(input("Masukan angka tebakan mu: "))
    
    if guess == x:
        print("Selamat kamu berhasil nebak! ", count)
        break
    elif guess > x:
        print("Tebakan kamu ketinggian!")
    elif guess < x: 
        print("Tebakan kamu kekecilan!")

if guess >= math.log(upper - lower + 1,2):
    print("\nAngka nya adalah %d" % x )
    print("\tSemoga beruntung dilain waktu!")