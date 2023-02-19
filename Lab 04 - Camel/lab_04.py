import time
import random

def main():
    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    native_distance = -20
    canteen_level = 3
    native_zero = 0
    yes_no = 0
    done = False
    Died = False
    squig = "~~~~~~~~~~~~"
    long_squig = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    rl_squig = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

    print(rl_squig)
    print(rl_squig)
    print("  - - - - - Welcome to OG Camel click adventure!!! - - - - -\n")
    print("     - - - - - - - - - COPYRIGHT 2nn2.LLC - - - - - - - -")
    print(rl_squig)
    print(rl_squig)
    #time.sleep(2)
    print("You have stolen a camel to make your way across the great Mobi desert!\n")
    print("    The natives want their camel back and are chasing you foo!\n")
    print("           Hit the feet through the desert, and survive!")
    print(long_squig)

    MEEP = ("\nA.Drink from your canteen\nB.Ahead moderate speed\nC.Ahead full speed\nD.Stop for the night\nE.Status check\nQ.Quit\n")




    while(not done):

        print(MEEP)
        user_choice = input("What is your choice? ")

        if user_choice.upper() == "199":
            miles_traveled = 199

        if user_choice.upper() == "A":
            print(f"You had {canteen_level} drinks in your canteen")
            canteen_level -= 1
            thirst = 0
            print(f"You now have {canteen_level}")
            print(f"your thirst level is: {thirst}")
            if canteen_level == 0:
                print("")
                print("~oh no!~")
                print("~Yeen got no mo fam~")



            #print(canteen_level)
            #time.sleep(3)

        if user_choice.upper() == "B":
            rand_om = random.randint(5, 12)
            miles_traveled += rand_om
            thirst += 1
            camel_tiredness += 1
            print(f"You travelled {rand_om} miles")
            native_zero += random.randint(7, 14)
            native_distance = abs((miles_traveled + 20) - native_zero)
            print(f"The natives are {native_distance} miles behind you")
            oasis = 10
            if oasis == (0, 21):
                print("~you have found an oasis!!!~")
                Thirst = 0
                canteen_level = 3
                camel_tiredness = 0


        if user_choice.upper() == "C":
                rand_om = random.randint(10, 20)
                miles_traveled += rand_om
                print(f"You travelled {rand_om} miles")
                native_zero += random.randint(7, 14)
                native_distance = ((miles_traveled + 20) - native_zero)
                #abs             ^
                print(f"The natives are {native_distance} miles behind you")
                camel_tiredness += random.randint(1, 3)
                thirst += 1
                oasis = 10
                if oasis == (0, 21):
                    print("~you have found an oasis!!!~")
                    Thirst = 0
                    canteen_level = 3
                    camel_tiredness = 0


        if user_choice.upper() == "D":
            user_choice = input("Are you sure? Y/N\n")

            if user_choice.upper() == "Y":
                print("")
                print("...LOADING...")
                camel_tiredness = 0
                print("your camel is happy and rested")
                native_zero += random.randint(7, 14)
                #time.sleep(2)
            if user_choice.upper() == "N":
                print(rl_squig)
                print("cmon mane....")
                print(rl_squig)
                #break



        if user_choice.upper() == "E":
            print("~~STATUS~~")
            print(f"THIRST: ~{thirst}~")
            print(f"Camel Tiredness: ~{camel_tiredness}~")
            print(f"MILES TRAVELED: ~{miles_traveled}~")
            print(f"The natives are ~{abs(native_distance)}~ miles behind you~")

        if user_choice.upper() == "Q":
            user_choice = input("see end stats? Y/N ")
            if user_choice.upper() == "Y":
                print()
                print(f"Miles travelled: {miles_traveled}")
                print(f"Drinks in canteen: {canteen_level}")
                print(f"The natives are {abs(native_distance)} miles behind you")
                print("---------------")
                done = True
                break

            elif user_choice.upper() == "N":
                done = True
                break

                #print("you are thirsty")


        if thirst == 4:
            print("~~~you are thirsty~~~")

        if thirst == 6:
            print("~~~DRINK NOW OR ELSE~~~")

        if thirst == (7):
            print("~~~you are slowly fading from dehydration~~~")
            done = True

        if camel_tiredness >= (5):
            print("~~~Camel looks terrible, you should let it rest~~~")

        if camel_tiredness >= (8):
            print("~~~cmon, I told you too ease off it... now its dead~~~")
            done = True

        if miles_traveled >= (200):
            print("WOOOOOOO!!!! WE MADE IT...")
            time.sleep(2)
            print("They cant chase us anymore,\n")
            time.sleep(2)
            print("Why?... [CLASSIFIED]... but that's the way it is. ")
            time.sleep(2)
            print("~~CONGRATULATIONS~~")
            time.sleep(2)
            print("~~~YOU~~~~~~~~~WIN~~~")
            done = True

        #CHEATCODESSSS!!!!!!!! aka dev checkpoints
        #enter at anytime thru the run!!!
        #199- set mileage to 199
        #




    if done:
        print("")
        print("---------------")
        print("We will meet again... friend")
        print("---------------")


main()
