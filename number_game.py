import random
com_num=random.randrange(1,100)
counter=0
try:
    while counter<=5:
        num=int(input("enter number\n"))
        counter=counter+1
        if num==com_num:
            print(f" the num is {com_num} you win {counter} num of trys")
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

