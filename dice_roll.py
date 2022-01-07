import random 
import array as arr

def dice_roll(die_sides):
    sum = 0
    dice_multiple = int (input ("how many dice do you want to use?\n"))
    if (die_sides == 2):
        while dice_multiple != 0:
            number = random.randint(1,2)
            dice_multiple -= 1
            if number == 1:
                print("heads\n")
            else:
                print("tails\n")
            
    else:
        while dice_multiple != 0:
            number = random.randint(1,die_sides)
            dice_multiple -= 1
            print("dice#"+str(dice_multiple)+" rolled "+str(number))
            sum += number
        return sum

while True: 
    print('''1. roll the dice           2.exit    ''')
    user = int (input("what do you want to do?\n"))
    if user == 1:
        dice_num = int (input("what kind of dice do you want to use? 2,4,6,8,10,12,20,100\n"))
        if dice_num == 2:
            dice_roll(2)
        elif dice_num == (4 or 6 or 8 or 10 or 12 or 20 or 100): 
            print("sum of dice is "+str(dice_roll(dice_num)))
    else:
        break   


