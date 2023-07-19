import random

com_num=random.randrange(1,100)
a=0
try:
    while a<=5:
        num=int(input("enter number\n"))
        a=a+1
        if num==com_num:
            print(f" the num is {com_num} you win {a} num of trys")
        elif num>com_num:
            print("your num is bigger")
        elif num<com_num:
            print("your number is smaller")
    else:
        if num!=com_num:
            print(f"\nyou loose number is {com_num}")
except Exception as e:
    print(e)
finally:
    print("\nplease start again")

