import random
while True:
    user_choice = int(input("\n1.Rock\n2.Paper\n3.Scissor  \n enter the number we want to choose: "))
    computer_choice = random.randint(1,3)
    print(f"Computer Choose: ", computer_choice)
    if user_choice >= 4 or user_choice < 1:
        print("you choose an invalid number")
    elif user_choice == 1 and computer_choice == 2:
        print("user win this game ")
    elif user_choice == 1 and computer_choice == 3:
        print("user win this game ")
    elif user_choice == 3 and computer_choice == 2:
        print("user win this game ")

    elif user_choice == 2 and computer_choice == 3:
        print("computer win this game ")
    elif user_choice == 2 and computer_choice == 1:
        print("computer win this game ")
    elif user_choice == 3 and computer_choice == 1:
        print("computer win this game ")
    elif computer_choice == user_choice:
        print("now its draw")

user_choice += 1
