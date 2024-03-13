import random
chars ="mnbvcxzlkjhgfdsapoiuytrewqZXCVBNMLKJHGFDSAPOIUYTREWQ1234567890!@#$%^&*()"
length=int(input(" Enter the length of password:"))
password=""

for i in range(length):
    password_char=random.choice(chars)
    password= password + password_char
    print(" your password :",password)
