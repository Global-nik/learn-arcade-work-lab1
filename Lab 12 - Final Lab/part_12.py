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
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Kinda Opaque~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~2777~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~COPYRIGHT 2nn2.LLC~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~2023~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(rl_squig)
    print(rl_squig)
    print("If you do not enter a name... the characters will be nameless.... "
          "which is fine but I did take the time \nto include this so why not name em?")
    print()
    #User
    print(long_squig)
    name = input("ENTER YOUR NAME...\n")
    print(f"~Had a cousin named {name}...")
    print("~you should probably stay out the west sector...~")
    planet = input("Whats your ideal planet... like if you had to choose?\n")
    print(f"What... {planet}? no way...! That's a terrible choice, why would you want to go there...?")
    print(long_squig)

    #Male
    pp = input("ENTER name for Rich Fella... DEFAULT NAME: Paris\n")
    print(f"{pp} has the cheese to buy what he needs...")
    cm = input("ENTER name for Crew Mate[m]... DEFAULT NAME: Zeke\n")
    print(f"~did you know about {cm}'s~ nickname?... half pint? lol~")
    print(long_squig)
    am = input("ENTER name for Air Marshal... DEFAULT NAME: Johns\n")
    print(f"~hope you do not know {am} in real life...~\n")
    print(f"~You may have to do things....~")
    print(long_squig)
    iw = input("ENTER name for the Imam, an Islamic prayer leader... DEFAULT NAME: Imam\n")
    print(f"Hope {iw} can handle this")
    print(long_squig)
    has = input("ENTER name for Imam follower 1... DEFAULT NAME: Hassan\n")
    ali = input("ENTER name for Imam follower 2... DEFAULT NAME: Ali\n")
    print(f"{has} and {ali}.... just kids following {iw} in their search for new holy land")
    print(long_squig)
    cc = input(f"ENTER name for Co-Captain... DEFAULT NAME: Greg\n")
    print(f"nice person I think but I just dont know {cc} all that well...")
    print(long_squig)
    #Female
    lb = input("ENTER name for clingy teen... DEFAULT NAME: Jack\n")
    print(f"Nice... {lb}...is that european?")
    print(long_squig)
    nv = input("ENTER name for Navigator... DEFAULT NAME: Caroline\n")
    print(f"You're almost done {name}, {nv} is a smart woman... keep her on your side")
    print(long_squig)
    sz = input(f"ENTER name for Rich girl... DEFAULT NAME: Shaz\n")
    print(f"If you dont want {sz} then i'll take her...")
    print(long_squig)

    '''music = input(f"Would you like some prologue music...?(Y/N)\n")
    if music == "Y":
        print("Great! We will get that set up for you right now...\n")
        arcade.open_window(300, 300, 'Missile 47.5', True, True)
        arcade.load_texture("150, 150, 'M475.png', 1, 0, 255")
        time.sleep(10)
        arcade.play_sound('BL.wav')'''

    print()
    print()
    time.sleep(4)
    print(rl_squig)
    print("~~~~~~~Chapter 1~~~~~~~\n~~~~~~~Rough Times~~~~~~~")
    print(rl_squig)
    time.sleep(4)
    print()
    print()
    print(f"DATE: 2/22/2223                                                                                   {name}\n")
    print("*Meteor strike.....small one*")
    print("You are awoken by turbulence and alarms, everything is a daze... you hear 2 distinct thuds\n")
    time.sleep(2)
    print(f"{cc},{nv}\n*Thud noises*...\n")
    time.sleep(2)
    print(f"{cc}\nW-why did we f-all out?\n")
    time.sleep(2)
    print(f"{nv}\nHe's dead, the captains dead, I was looking right at him!\n")
    print(f"{cc}\nThe chronograph says we still have 22 weeks left!\nGravity is not supposed to kick in until week 19"
          f"... Why did we fall out?!")
    print(f"{nv}\nI just told you THE CAPTAIN IS DEAD!!!\n")
    time.sleep(2)
    print(f"{cc}\n~~THIS IS AN EMERGENCY DIS-DISPATCH FROM "
          "MERCHANT VESSEL ALPHA BRAVO~~\n"
          "~~WE HAVE BEEN KNOCKED...PING LANE, OUR COORDINATES ARE...~~\n")
    print("You fade out...\n\n")
    print("When you wake, you over hear two people talking,\n...")
    time.sleep(2)
    print(f"{am}\n`They just escaped from a maximum prison...`\n")
    time.sleep(2)

    print(f"{nv}\n`Sooo do we just keep them locked up forever?`\n")
    time.sleep(2)
    print(f"{am}\n`well... that would be my choice...`\n")
    time.sleep(2)
    print(f"{nv}\n`are they really that dangerous?`\n")
    time.sleep(1)
    print(f"{am}\n`Who {name}?\nYou mean the person who is currently bound at the ankles and wrists to a metal "
          f"beam?\n")
    time.sleep(3)
    print(f"{nv}\nUh, yea.....?\n")
    print(f"{am}\nnoooooooo....\nWhy would you think that?\n")
    print(f"{nv}\nYou know {am}... you dont have to be an a** all the time...\n")
    print(f"Y'know {nv} seeing as YOU wanted to leave us ALL FOR DEAD during the crash...\nI, think I, "
          f"have the right, to"
          f" 'be an a**'...")
    print("They both leave")
    time.sleep(3)
    print(rl_squig)
    print(rl_squig)
    print()
    print("You have a thin black cloth over your eyes,\n but you can still see a bit... \nYou notice the beam you are "
          "cuffed to has\n taken some damage in the crash... its a \nbit high and you'll have to dislocate your\n "
          "shoulders to bring your arms through... \nwhile everyone is distracted...\n")

    while not done:

        print("....")
        user_choice = input(f"So {name}... figure now the best time for escape?(Y/N):\n")
        if user_choice.upper() == "Y":
            print("You go through the usual motions\nYou have to stand up, stretch your arms back and up, "
                  "then rotate those shou-\n*Various crunching noises*...\n")
            time.sleep(4)
            print("...well its about time to go is it not?... Just remember\n")
            print("You ARE on an unknown planet... so its not wise to stray too far, you want to stay out of sight "
                  f"but still keep an eye out...\n{am} will notice you're gone soon... make a move")
            time.sleep(4)
        elif user_choice.upper() == "N":
            print("uhh... ok then\n")
            time.sleep(4)
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
            time.sleep(4)

        print()
        user_choice = input("you've been running for a while and see a large skeleton in "
                            "the distance....\nDo you want to check it out?(Y/N):  \n")

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
                f"~~~IN A UNDISCLOSED LOCATION~~~\nAS you are aware six months ago, the merchant vessel carrying "
                f"escaped"
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
            time.sleep(3)
            time.sleep(2)
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
            print("You sprint towards the cries for help\n")
            time.sleep(3)
            print("As you are getting closer... you see some tubular structures in the distance...\n")
            time.sleep(3)
            print("Arriving at the tubes you see one has a makeshift canopy attached to it... ")
            print(f"It was probably left by {cm}...and its covering a hole in the ground...\nwith another bloody "
                  f"hole in it...")
            print("Since the canopy is the only thing you see that's man made, you check underneath...")
            print("*Squelching*")
            print(f"You find {cm}... stuck halfway into the hole")
            print()
            print("whats that noise...")
            time.sleep(3)
        elif user_choice.upper() == "N":
            print("~Eh? fagettabout em~\n")
            print("Spoken like a true space italian...")
            print("...")
            print("You think to yourself... 'I should go, I want to figure out if anything else is here")
            print("...")
            print("You sprint towards the cries for help\n")
            time.sleep(3)
            print("As you are getting closer... you see some tubular structures in the distance...\n")
            time.sleep(3)
            print("Arriving at the tubes you see one has a makeshift canopy attached to it...")
            print("Since the canopy is the only thing you see that's man made, you check underneath...")
            print("*Squelching*")
            print("You find one of the Brady Bunch... stuck halfway into the hole")
            print()
            print("*whats that noise...*")

        user_choice = input("Do you want to pull them out?(Y/N)\n")
        if user_choice.upper() == "Y":
            print("You grab them by the legs and give a sturdy pull... *POP*...\n"
                  "The look of disdain on your face says it all... not being ironic but all that was left was "
                  "below the waist... Hmph")
            print("~OH ****! Watch out!!!!~\nA creature scrawls out of the hole...\nYou hear "
                  "'OooOOOooooOOo' over and over and over...\n")
            print(rl_squig)
            print("Hi, narrator/creator here!!!\n")
            print("Lil Bro had to be absolutely plastered... I dont know if it knows but, "
                  "we dont play that noisy ****")
            print(rl_squig)
        elif user_choice.upper() == "N":
            print("Nah, You'd rather wait for backup... sh** if you heard the screams everyone else should have...")

        user_choice = input("Forget this nonsensical behavior... You MUST to kick it... "
                            "no skateboard(TYPE:kick)\n")
        if user_choice.upper() == "kick":
            print("No questions asked, you kick the literal alien sh-"
                  " well we really dont know what it was... could have been spit or blood or whatever...\n")
            print("Regardless, it seems that you've made a mistake... you misjudged the defensive "
                  "capabilities of the alien species...\n")
        if shiv == 1:
            print(f"*IT LUNGES AT YOU*... you have {shiv} shiv\n")
            user_choice = input("Would you like to use it?!(Y/N)\n")
            if user_choice.upper() == "Y":
                print("You shiv the creature above the mouth... where its face is supposed to be...\n"
                      "a mere stun... it was enough to make it retreat... not without "
                      "its bounty though.\n")
            if user_choice.upper() == "N":
                print("You continuously kick the creature until it retreats.... not without its bounty though...\n")
        time.sleep(3)
        print()
        print("...LOADING")
        print()
        time.sleep(3)
        print("Not even a minute after your encounter, the rest of the little rascals "
              "decide to make an appearance...")
        print("Being that you are a extremely dangerous criminal.... they assume you were "
              f"the cause of the screaming and blood and did something to {cm}...\n")
        print(f"*{am} beats you with a nightstick*")
        print(f"*{sz} gets a face-kick in...*")
        time.sleep(3)

#CHAPTER 2/4
        print(rl_squig)
        print(rl_squig)
        print("~~~~~~~Chapter 2~~~~~~~\n~~~~~~~Back to Lockup~~~~~~~")
        print(rl_squig)
        print(rl_squig)
        print()
        print(f"{lb}\nWell, back again?....ahhh yes... chains this time... you think it'll hold this time {am}"
              f"?...")
        print(f"Of course after what happened under the canopy {am} wants to interrogate you...\n*{nv} is present "
              f"too...*")
        print()
        print(rl_squig)
        print()
        print("You do not see the point in giving the same answer over and over but their disturbed faces make it worth"
              " it you guess...\n")
        print(f"{am}\nSo {name}... where is the body?\n")
        print(f"{name}\n...\n")
        print(f"*{am} getting a bit aggressive and visibly shaking* \nWHERE IS {cm}'s DA** BODY {name}!?")
        print(f"{name}\n...\n")
        print(f"*{am} leaves to calm down*")
        print(f"*{nv} takes over...*")
        print(f"{nv}\nWhere is {cm}'s body? ...\n")
        time.sleep(4)
        print(f"{name}\n...")
        print(f"{nv}\nIf you dont want to talk... that's fine, BUT I want you to know...\nTheres a debate on weather"
              f" to leave you here to...")
        print(f"{name}\nYou mean the whispers?")
        print(f"{nv}\nWhat whispers?")
        print(f"{name}\nThe ones telling me to go for the sweet-spot next to the spine\n The liver... Its a metallic"
              f" taste, human blood... copper-ish but, if paired with Deuce then-")
        print(f"{nv}\nYou want to tell me the truth?\n...\nAll you people are sooo scared of me... *hmph*\n Out here"
              f"its not me you have to worry about")
        print(f"{nv}\nLet me see your eyes {name}")
        print(f"{name}\nYou'd have to come closer...")
        print(f"*{nv} walks closer to you*")
        time.sleep(2)
        print(f"{name}\n")
        time.sleep(3)
        print()
        print("*BANG...*")
        print()
        time.sleep(3)
        print(f"You are now about a foot away from {nv}... looking into each others eyes...")
        print(f"{lb}\nYOOOOOO where do I get eyes like that?!\n")
        print(f"{name}\n*hmph*You gotta kill a few people...\n")
        print(f"{lb}\nOK!, I can do it...!")
        print(f"{name}\nThen you have to get sent to a slam, where they'll tell you you'll never "
              f"see daylight again...")
        print("You dig up a doctor... let em do a surgical shine job on your eyeballs...")
        print(f"{lb}\nSo you can see who's sneaking up on you in the dark?")
        print(f"{name}\nExactly...!")
        print(f"{nv}\nLEAVE...!\n")
        print(f"*{lb} stares at {nv}*\n")
        print(f"{nv}\nleave...")
        print(f"*{lb} walks upstairs*")
        time.sleep(5)
        print(f"{name}\nNice kid....\nBut did I kill a few people...? Sure, but did I kill {cm}... No...")
        print(f"{nv}\nThere not in the hole!")
        print(f"{name}\nLook deeper...")

        print(f"*As {nv} is walking out you ask*\nAsk {am} why they shake so much...\n")
        print(f"*{nv} leaves*\n\nYou decide to take a nap...\n\n")
        time.sleep(4)
        print("...LOADING...\n\n")
        time.sleep(4)
        print(f"You are awoken by {nv} coming to take the chains off...\nYou save her the trouble and break them"
              f" yourself\n")
        print(f"You see {nv} is covered in blood and cuts... You ask what happened...\n")
        print(f"{name}")
        print("What happened while I was sleep?\n")
        print(f"{nv}\nI went into the hole to see if you were telling the truth and I found {cm}'s body "
              f"in a commons area, heard something and got out...")
        print(f"{name}\nOk but that doesnt explain the blood...\n")
        print(f"{nv}\n*Reluctant to tell you*...\nThere were too many tunnels and I got confused in the rush and "
              f"climbed the wrong tunnel... as I was climbing something grabbed my rope and started pulling "
              f"me back down!...\nI fought and got to the top where the crew helped pull me out...\n")
        print(f"{name}\nOh? The cosby kids have some use huh...Still doesn't explain the blood...")
        print(f"{nv}\nIts a rough climb and I was being attacked... you do the math.")
        print(f"Anyway I made it out and told the crew I saw what was left of {cm}'s body down\n"
              f"there... and they decided once again that your are useful...\n")
        print(f"{name}\nYou went through all that trouble for lil ole me?\n")
        print(f"{nv}\nDont flatter yourself... I just wanted to know what happened to {cm}...")
        print(rl_squig)
        print(rl_squig)
        print()
        print("*You're freed*")
        print(f"{name}")
        print("Ahhhhh.... \nfree at last\nfree... at... last...")
        print()
        print(rl_squig)
        print(rl_squig)
        time.sleep(4)
#chapter 3/4
        print()
        print("New Beginnings = New Problems")
        print()
        print(rl_squig)
        print()
        print("You've been walking with the minions for a good while now... they have you pulling this power "
              "transmitter... for what? no clue but you take it easy when pulling... "
              "never know when you'll need to run")

        print("While walking on of the Pj's drops a bottle")
        print("As you're walking to it, you see its owner... and the bottle that lay at your feet...\nJust as you"
              "place your hand on the bottle, its owner arrives.... ")
        print("A older male... not really a looker but his designer pajamas, with matching cap, say he's well fed...\n")
        print("*You can see the nervousness within him*\n")
        print(f"{pp}.P.Keelby, Entrepreneur, antiquities dealer, said standing up...")
        print(f"{name}.J.Hollin, said shaking hands...")
        user_choice = input("Did you want to sample the bottle?")
        if user_choice.upper() == "Y":
            print("You put the bottle to your lips and begin drinking...")
            print(f"{pp} chimes in...\nThat's actually very expensive-... ok help yourself...")
        elif user_choice.upper() == "N":
            print(f"You hand the bottle back to {pp}...")
            print(f"{pp} chimes in...\nThat's actually very expensive-... ok help yourself...")

        print("time passes, and you've made it to a camp with the others...")
        time.sleep(4)
        print("You see a pair of glasses next to a door...")
        print("You move back a cover... it says Coring Room")
        print(f"As you move the cover, {am} appears from about 10 feet behind you...\n{am}\nYou're missing the party,"
              f"cmon boy")
        print(f"As you are about to leave... you rip down the cover exposing {lb}...\n{name}\nCmon... you're missing"
              f"the party")
        print(f"You see that {iw} got the water pump working... everyone is taking their cups")
        print(f"As you are drinking... the crew is exploring the main building, debating whatever... "
              f"you really dont care")
        print(f"{pp}\nWho are these people? miners?\n")
        print(f"{sz}\nLooks like geologists.. you know? and advanced team that moves around from rock to rock?"
              f"like space noma-")
        print(f"{nv}\nNice of them to leave so much stuff here. Why'd they leave their ship?\n")
        print("*EVERYONE BEGINS TO SPECULATE*\n")
        print(f"{am}\nWell its not technically a ship, its a skiff and they are usually disposable, really.")
        print(f"{pp}\nMore like a emergency raft right?")
        print(f"{sz}\nYeah, they probably had like a mothership of somthing come pick them up...")
        print(f"{name}\nThese people didn't leave.... lol come on.\nUse your heads... whatever got {cm}, probably"
              f"got them too...\nThere all dead")
        print("*Visual Discomfort on everyone elses face*")
        print(f"{name}\nYou dont really think that they left without their belongings... right?\nI mean photos on"
              f" shelves, clothes on the hooks... ")
        print(f"{sz}\nMaybe they had weight limits or-...")
        print(f"{name}\nI know you dont prep your emergency ship without there being a dam* emergency...")
        print(f"{lb}\nThey're right dam* it...!")
        print(f"{am} and {sz}\n*Simultaneously* Watch your mouth...!")
        print(f"{name}'s just saying what were all thinking")
        print("...")
        print(f"*{iw} enters the room again*\nHas anyone seen {ali}?")
        user_choice = input("Do you mention the coring room?")
        if user_choice.upper() == "Y":
            print(f"{name}\nDid you check the coring room?")
        elif user_choice.upper() == "N":
            print("...")

        print("*INSIDE CORING ROOM*")
        print(f"{ali} walks around the room and finds a monkey wrench... ")
        print(f"{ali} opens a shutter to let sunlight into the room\nIts mechanical, so its operated by a console...")


#chapter 4/4
        done = True

        if done:
            print("Hope all was enjoyed today... Yes this project was originally not turned in and yes "
                  "I did promise a full game... as I "
                  "am writing this, I have 50 minutes left and currently about 411 lines of code. "
                  "Its due today after being due tuesday, I "
                  "had to work and I have the MEANEST stomach virus or something.... been on and off for about a month."
                  "Anyway right now I am thinking about leaving the time.sleep() out... simply because this is a pretty"
                  "linear game and I want you to go the way I want you too but feel like you have an option you know?")
            print(rl_squig)
            print(rl_squig)
            print("Anyway... YOOOOOO CONGRATULATIONS ON MAKING IT OFF THE PLANET... you're still a well wanted "
                  "escaped convict so its not like you can do back to civilization... ")
            print(f"Matter fact didn't you say you wanted to go to {planet}?\nI know I said it was a bad choice but..."
                  f" shoot anythings gotta be better than that...!")


main()
