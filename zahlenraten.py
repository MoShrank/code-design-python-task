goal_number = 100

def check_number(x):
    if x == goal_number:
        print("congratulations. You won, Your number is right")
    elif goal_number < x:
         print("the number is lower")
    else:
        print("the number is higher")

inp = input("guess the number: ")
inp = int(inp)
check_number(inp)
