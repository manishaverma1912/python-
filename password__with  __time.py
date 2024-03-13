
from time import sleep
while True:
        for i in range(1,4):
            password = input("enter your password: ")
            if password == "A13P":
                print("phone is unlocked")
                break
            else:
                print(3-i, "chance remaning")
            i+=1
        else:
            print("wait for 30sec")
            print("wait :")

            for i in range(30,0,-1):

                print(i)
                sleep(1)
            print("try again")


# # import time
# for x in range(1,15):
#     print(x)
#     time.sleep(2)


# from time import sleep
# for x in range(1,15):
#     print(x)
#     sleep(2)



import time
while True:
 print("hello")
 time.sleep(1)

