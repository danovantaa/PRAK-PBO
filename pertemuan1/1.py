x = int(input("Batas Bawah : "))
y = int(input("Batas Atas : "))

sum =0
 
if x>=0 and y >=0 : 
    for i in range(x,y):
        if i%2 != 0 :
            sum+=i
            print(i)
    print(f"Total : {sum}")

else : 
    print("Batas atas dan batas bawah yang dimasukkan tidak boleh dibawah nol")


    
