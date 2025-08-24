import time
while True:
   userinput=input("Welcome to my minigame, can i take your name?")
   if userinput:
        print(f"hello {userinput.title()}, choose these five weapons!")
        weapons=[
               "Knife atk 5 def 3 AURA INFINITE",
               "Dagger atk 8 def 2 speed 999",
               "Sword atk 20 def 2 honor 999",
               "LOVE atk 999 def 0 SPECIAL you dont wanna know!"
               ]
        for weapon in weapons:
            print(weapon)
        uinput=input("choose wisely:")
        enemies=["Goblin","dragon","bandit"]
        if uinput.lower()=="knife":
            print("uhh! LEON??? OHH YEAHHH!\n")
        elif uinput.lower()=="dagger":
            print("nice\n")
        elif uinput.lower()=="sword":
            print("hehe, zelda?\n")
        elif uinput.lower()=="love":
            print("ohhhhh....i dont get it!WHY LOVE????\n")
        for enemy in enemies:
            print(f"{enemy} has arrived! Good luck in your fight!")
        ainput=input("Tap 'enter' to start the WARRRRR!")
        while True:
                print("Goblins are coming to your way!")
                input()
                print("Dragons swifting through air! their mouth open ready to let our agonizing fire!")
                input()
                print("bandits running with their hands full of shurikens and sticks? that still hurts like hell!")
                if uinput.lower()=="knife":
                    input()
                    print("but....")
                    input("you realise that you are....")
                    print("LEON!")
                    input("and the enemies all started to retreat seeing your AURA! making them contemplate their existence!!!  ")
                    print("good job! mission completed!")
                    break
                elif uinput.lower()=="dagger":
                    input()
                    print("but")
                    input("...you realise that you have...")
                    print("Dagger!!!!")
                    print("you immediately slice couple of goblins!")
                    input()
                    print("even take out those bandits with scary stuff they yield!")
                    input("but")
                    print("you realise that you cant deflect the fire breath of the dragon with your dagger!")
                    print("and sadly turn into ashes!")
                    zinput=input("GAME OVER! try again? (y/n)")
                    if zinput.lower()=="y":
                        print("but you realise that you had only one life!so this choices meant nothing!")
                        time.sleep(2)
                        exit()
                    else:
                        exit()
                elif uinput.lower()=="sword":
                    input()
                    print("but")
                    input("...you realise that you have a...")
                    print("SWORD!!!!")
                    print("you immediately slice couple of goblins!")
                    input()
                    print("even take out those bandits having those scary stuff!")
                    input("but")
                    print("you realise that you cant deflect the fire breath of those dragons with your sword!")
                    input()
                    print("you looked at the sun, not caring even if your eyes are in pain! because you know the dragon is charging its breath!!!")
                    input()
                    print("but you feel some presence beside you, a light surrounding you!")
                    print("and you regret hurting your eyes, wanting to see the presence even when about to face death itself!")
                    input()
                    print("your sword suddenly feels heavy turning into...")
                    input()
                    print("EXALIBUUUUUUUUR!!!")
                    print("Guided by your sword, you immediately deflect the attack slicing the dragon in HALF!!!!!!")
                    input()
                    print("and you saved the world and yourself! but at what cost? YOUR EYES!")
                    print("mission completed? man! i dont even think you can see this!")
                    print("TRY AGAIN!")
                    zinput=input("GAME OVER! try again? (y/n)")
                    if zinput.lower()=="y":
                        print("but you realise that you had only one life!so this choices meant nothing!")
                        time.sleep(2)
                        exit()
                    else:
                        exit()
                elif uinput.lower()=="love":
                    input()
                    print("but")
                    input("...you realise that you have a...")
                    print("love???")
                    print("uhmmm uhmmm!.... goblins, bandits, and dragon are rushing to your way!!!")
                    input()
                    print("you are being unusually calm and happy despite the circumstance!")
                    input()
                    print("...you trust in their change of heart rather than self preserving...")
                    input()
                    print("...you...still...didnt...lose...your...modesty...and...composure!")
                    input()
                    print("...and you feel a light surrounding you, looking like angels are protecting you!")
                    input()
                    print("...but it looks like...")
                    input()
                    print("you are dead!... it seems LOVE doesnt work like those fictions you have read so many times!")
                    input()
                    zinput=input("GAME OVER! try again? (y/n)")
                    if zinput.lower()=="y":
                        print("but you realise that you had only one life!so this choices meant nothing!")
                        time.sleep(2)
                        exit()
                    else:
                        exit()
                    




                
