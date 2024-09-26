import random

a = random.randint(1,100)

b = int(input("enter your guess: "))
c =1
while b!=a:
    
    if(b>a):
        print("your guess is high")
    elif (b<a):
        print("your guess is low")
    
    b = int(input("enter your guess agin: "))
    c+=1
    
    
print("you guessed correctly")
print(f"you guess in {c} chance")