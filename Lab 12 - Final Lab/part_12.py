import time
import arcade


def main():

    shiv = 0
    done = False
    long_squig = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    rl_squig = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    arcade.load_sound("BL.wav")
    arcade.load_texture("M475.png")
    print(rl_squig)
    print(rl_squig)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Kinda Opaque~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~2777~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~COPYRIGHT 2nn2.LLC~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~2023~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(rl_squig)
    print(rl_squig)
    print("If you do not enter a name... the characters will be nameless.... "
          "which is fine\nJust press enter to skip.\nIf you want\n")
    print()
    #U
    name = input("ENTER YOUR NAME...!\n")
    print(f"~Had a cousin named {name}...\n")
    print("you should probably stay out the west sector...\n")

    #Male
    am = input("ENTER name for Air Marshal... DEFAULT NAME: Johns\n")
    print(f"~hope you do not know {am} in real life...~\n")
    print(f"~You may have to do things....\n")
    iw = input("ENTER name for the Imam, an Islamic prayer leader... DEFAULT NAME: Imam\n")
    print(f"Hope {iw} can handle this\n")
    gg = input(f"ENTER name for Co-Captain... DEFAULT NAME: Greg")
    print(f"nice person I think but I just dont know {gg} all that well...\n")

    #Female
    lb = input("ENTER name for Lil Homie... DEFAULT NAME: Jack")
    print(f"Nice... {lb}...is that european?\n")
    nv = input("ENTER name for Navigator... DEFAULT NAME: Caroline")
    print(f"You're almost done, {nv}\n")
    sz = input(f"ENTER name for Rich girl... DEFAULT NAME: Shaz")
    print(f"If you dont want {sz} then i'll take her...\n")

    '''music = input(f"Would you like some prologue music...?(Y/N)\n")
    if music == "Y":
        print("Great! We will get that set up for you right now...\n")
        arcade.open_window(300, 300, 'Missile 47.5', True, True)
        arcade.load_texture("150, 150, 'M475.png', 1, 0, 255")
        time.sleep(10)
        arcade.play_sound('BL.wav')'''

    print()
    print()
    print("~~~~~~~LOADING~~~~~~~~")
    #time.sleep(4)
    print(rl_squig)
    print(rl_squig)
    print(f"DATE: 2/22/2223                                                                              {name}\n")
    print("You are awoken by turbulence and alarms, everything is a daze... you hear 2 distinct thuds\n")
    #time.sleep(2)
    print("*Thud noises*...\n")
    #time.sleep(2)
    print("W-why did we f-all out?")
    #time.sleep(2)
    print("`He's dead, the captains dead, I was looking right at him!\n")
    #time.sleep(2)
    print("...\n~~THIS IS AN EMERGENCY DIS-DISPATCH FROM "
          "MERCHANT VESSEL ALPHA BRAVO~~\n"
          "~~WE HAVE BEEN KNOCKED...PING LANE, OUR COORDINATES ARE...~~\n")
    print("You fade out\n...\n")
    print("When you wake, you over hear two people talking,\n...")
    #time.sleep(2)
    print("`They just escaped from a maximum prison...`\n")
    #time.sleep(2)

    print("`Sooo do we just keep them locked up forever?`\n")
    #time.sleep(2)
    print("`welll that would be my choice...`\n")
    #time.sleep(2)
    print("`are they really that dangerous?`\n")
    #time.sleep(1)
    print("`Who them!? noooooooo....\n")
    #time.sleep(3)
    print(rl_squig)
    print(rl_squig)
    print()
    print("You have a thin black cloth over your eyes,\n but you can still see a bit... \nYou notice the beam you are "
          "cuffed to has\n taken some damage in the crash... its a \nbit high and youll have to dislocate your\n "
          "shoulders to bring your arms through... \nwhile everyone is distracted...\n")

    while not done:

        print("....")
        user_choice = input(f"So {name}... figure now the best time for escape?(Y/N):\n")
        if user_choice.upper() == "Y":
            print("You go through the usual motions\nYou have to stand up, stretch your arms back and up, "
                  "then rotate those shou-\n*Various crunching noises*...\n")
            #time.sleep(4)
            print("...well its about time to go is it not?... Just remember\n")
            print("You ARE on an unknown planet... so its not wise to stray too far, you want to stay out of sight "
                  "but still keep an eye out...\n")
            #time.sleep(4)
        elif user_choice.upper() == "N":
            print("uhh... ok then\n")
            # time.sleep(4)
            print()
            print(
                "Wakey Wakey... Seeing as you were good and didn't escape... "
                "the gang figured it would be better to have an extra set of hands...\n")
            print("Nah im good fam...")
            print("*Weapon drawn* I dont think I asked for your opinion...")
            print("Yea yea... tough guy with a gun... just let me out... ")
            print("*Tapping your head with the gun* Just remember how this could have gone but didn't...")
            print()
            print(":)")
            print("You proceed to turn around and grab the gun... placing it under the marshals chin... ")
            print("Buddy is sweating bullets... no pun intended")
            print("like a movie star you say, 'Remember how this could have gone...'\n"
                  "with a slight grin...")
            #time.sleep(4)

        print()
        user_choice = input("you've been running for a while and see a large skeleton in "
                            "the distance....\nDo you want to check it out?Y/N:  \n")

        if user_choice.upper() == "Y":
            print()
            print("Investigating the skeleton, you find a ~bone shard~")
            shiv += 1
            print(f"You now have {shiv} shiv\n")
            print("...")
            print("~Time passes~")
            print()
            print(rl_squig)
            print(
                f"~~~IN A UNDISCLOSED LOCATION~~~\nAS you are aware six months ago, the merchant vessel carrying escaped"
                f" convict, {name}, went down in the Topanga district...\n weather or not they survived the crash is "
                "unknown...\n"
                "since that is your jurisdiction, we thought the best course of action... would be to give "
                "the case to you.\n"
                f"DO BE ADVISED, if {name} is not caught...\nyou and you alone will suffer the consequences"
                "~~~END TRANSMISSION~~~\n")
            print(rl_squig)
            print("This planet has four suns.... you have no clue what time it is")
            print("Not that you really care, a hat would be nice though")
            print("Hold on.... is someone screaming!?")
            print()

        elif user_choice.upper() == "N":
        print()
        print("'_'... I worked hard on this")
        # time.sleep(3)
        # time.sleep(2)
        print("~Time passes~")
        print()
        print(rl_squig)
        print(
            "~~~IN A UNDISCLOSED LOCATION~~~\nAS you are aware six months ago, the merchant vessel carrying escaped"
            " convict, 5-5-5, went down in the Topanga district...\n weather or not they survived the crash is "
            "unknown...\n"
            "since that is your jurisdiction, we thought the best course of action... would be to give "
            "the case to you.\n"
            "DO BE ADVISED, if ~555~ is not caught...\nyou and you alone will suffer the consequences"
            "~~~END TRANSMISSION~~~\n")
        print(rl_squig)
        print("This planet has four suns.... you have no clue what time it is")
        print("Hold on.... is someone screaming!?")
        print()

        user_choice = input("Do you want to investigate?(Y/N):\n")
        if user_choice.upper() == "Y":
            print(
                "You sprint towards the cries for help\n")
            #time.sleep(3)
            print("As you are getting closer... you see some tubular structures in the distance...\n")
            #time.sleep(3)
            print("Arriving at the tubes you see one has a makeshift canopy attached to it...")
            print("Since the canopy is the only thing you see that's man made, you check underneath...")
            print("*Squelching*")
            print("You find one of the crew people... stuck halfway into the hole")
            print()
            print("whats that noise...")
        #time.sleep(3)
        elif user_choice.upper() == "N":
            print("~Eh fagettabout em~\n")
            print("Spoken like a true space italian...")

        elif user_choice.upper() == "N":
            print()
            print("'_'... I worked hard on this")
            #time.sleep(3)
            #time.sleep(2)
            print("~Time passes~")
            print()
            print(rl_squig)
            print(
                "~~~IN A UNDISCLOSED LOCATION~~~\nAS you are aware six months ago, the merchant vessel carrying escaped"
                " convict, 5-5-5, went down in the Topanga district...\n weather or not they survived the crash is "
                "unknown...\n"
                "since that is your jurisdiction, we thought the best course of action... would be to give "
                "the case to you.\n"
                "DO BE ADVISED, if ~555~ is not caught...\nyou and you alone will suffer the consequences"
                "~~~END TRANSMISSION~~~\n")
            print(rl_squig)
            print("This planet has four suns.... you have no clue what time it is")
            print("Hold on.... is someone screaming!?")
            print()
            user_choice = input("Do you want to investigate?(Y/N):\n")
            if user_choice.upper() == "Y":
                print(
                    "You sprint towards the cries for help\n")
                #time.sleep(3)
                print("As you are getting closer... you see some tubular structures in the distance...\n")
                #time.sleep(3)
                print("Arriving at the tubes you see one has a makeshift canopy attached to it...")
                print("Since the canopy is the only thing you see that's man made, you check underneath...")
                print("*Squelching*")
                print("You find one of the crew people... stuck halfway into the hole")
                print()
                print("whats that noise...")
                user_choice = input("Do you want to pull them out?(Y/N)")
                if user_choice.upper() == "Y":
                    print("You grab them by the legs and give a sturdy pull... *POP*...\n"
                          "The look of disdain on your face says it all... not being ironic but all that was left was "
                          "below the waist... Hmph")
                    print("~OH ****! Watch out!!!!~\nA creature scrawls out of the hole...\nYou hear "
                          "'OooOOOooooOOo' over and over and over...\n")
                    print("Hi, narrarator/creator here!!!\n")
                    print("Lil Bro had to be absolutely plastered... I dont know if it knows but, "
                          "we dont play that noisy ****")
                    user_choice = input("Forget this nonsensical behavior... You want to kick it?... "
                                        "no skateboard(Y/N)\n")
                    if user_choice.upper() == "Y":
                        print("No questions asked, you kick the literal alien sh-"
                              "well we really dont know what it was... could have been spit or blood or whatever...\n")
                        print("Reguardless, it seems that you've made a mistake... you misjudged the defensive "
                              "capablilities of the alien species")
                        if shiv == 1:
                            print(f"*IT LUNGES AT YOU... you have {shiv} shiv")
                            user_choice = input("Would you like to use it?!(Y/N)")
                            if user_choice.upper() == "Y":
                                print("You shiv lil homie above the mouth... where its face is supposed to be...\n"
                                      "a mere stun... it was enough to make it retreat... not without "
                                      "its bounty though.\n")
                                #time.sleep(3)
                                print()
                                print("...LOADING")
                                print()
                                #time.sleep(3)
                                print("Not even a minute after your encounter, the rest of the little rascals "
                                      "decide to make an apperance...")
                                print("Being that you are a extremely dangerous criminal.... they assume "
                                      "you were the cause of the screaming...")
                                #time.sleep(3)
                                print("...")
                                print()
                                print("~~Back to lockup~~\n")
                                print()
                                print("...")

        if user_choice.upper() == "N":
            print("uhh... ok then")
            #time.sleep(2)
            print("Marshal: Wakey Wakey... Seeing as you were good and didnt escape... "
                  "the gang figured it would be better to have an extra set of hands...\n")
            print("You: Nah im good fam...")
            print("Marshal: *Weapon drawn* I dont think I asked for your opinion...")
            print("You: Yea yea... tough guy with a gun... just let me out... ")
            print("Marshal: *Tapping your head with the gun*Just remember how this could have gone but didn't...")
            print()
            print("you:)")
            print("You proceed to turn around and grab the gun... placing it under the marshals chin... ")
            print("Buddy is sweating bullets... no pun intended")
            print("like a movie star you say, 'Remember how this could have gone...'\n"
                  "with a slight grin...")
            #time.sleep(2)
            print(long_squig)
            print(long_squig)
            print(
                "~~~IN A UNDISCLOSED LOCATION~~~\nAS you are aware six months ago, the merchant vessel carrying escaped"
                " convict, 5-5-5, went down in the Topanga district...\n weather or not they survived the crash is "
                "unknown...\n"
                "since that is your jurisdiction, we thought the best course of action... would be to give "
                "the case to you.\n"
                "DO BE ADVISED, if ~555~ is not caught...\nyou and you alone will suffer the consequences"
                "~~~END TRANSMISSION~~~\n")
            print(rl_squig)
            print()
            print("This planet has four suns.... you have no clue what time it is")
            print()

            print("As you are out 'doing' tasks for the hindrances\n You hear someone screaming...\n"
                  "You dont really care but its nothing else better to do...")
            user_choice = input("Do you check it out?(Y/N)")
            print()
            if user_choice.upper() == "Y":
                print(
                    "You sprint towards the cries for help\n")
                #time.sleep(3)
                print("As you are getting closer... you see some tubular structures in the distance...\n")
                #time.sleep(3)
                print("Arriving at the tubes you see one has a makeshift canopy attached to it...")
                print("Since the canopy is the only thing you see that's man made, you check underneath...")
                print("*Squelching*")
                print("You find one of the crew people... stuck halfway into the hole")
                print()
                print("whats that noise...")

            if user_choice.upper() == "N":
                print("Nahh forget em")

                done = True

        if done:
            print("")
            print("---------------")
            print("We will meet again... friend")
            print("---------------")


main()
