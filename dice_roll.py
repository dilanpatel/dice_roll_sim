import random 

def dice_roll(die_sides):
    sum = 0
    dice_list = list()
    if (die_sides == 2):
        coin_flips= int (input ("Enter how many coins do you want to use?\n"))

        while coin_flips != 0:
            number = random.randint(1,2)
            coin_flips -= 1
            if number == 1:
                dice_list.insert("heads",coin_flips)
                print("heads\n")
            else:
                dice_list.insert("tails",coin_flips)
                print("tails\n")
        print(dice_list)
    else:
        dice_multiple = int (input ("Enter how many dice do you want to use?\n"))
        while dice_multiple != 0:
            number = random.randint(1,die_sides)
            dice_multiple -= 1
            print("dice#"+str(dice_multiple)+" rolled "+str(number))
            sum += number
        print("sum of dice is "+str(sum))

def dice():
    while True:
        print(''' 1. roll dice          2. exit     ''')
        user = int (input("what do you want to do?"))
        if (user == 1):
            print(''' Choose which # sided dice to roll? \n     1.      2/flip a coin\n     2.      4 sided dice\n     3.      6 sided dice\n     4.      8 sided dice\n     5.      10 sided dice\n     6.      12 sided dice\n     7.      20 sided dice\n     8.      100 sided dice/percentile dice\n''')
            user = int (input("CHOOSE YOUR OPTION?"))
            if (user == 1):
                dice_roll(2)
            elif(user == 2):
                dice_roll(4)
            elif(user == 3):
                dice_roll(6)
            elif(user == 4):
                dice_roll(8)
            elif(user == 5):
                dice_roll(10)
            elif(user == 6):
                dice_roll(12)
            elif(user == 7):
                dice_roll(20)
            elif(user == 8):
                dice_roll(100)
        else:
            break
        

while True: 
    dice()
