while True:
   userinput=input("Welcome to my minigame, can i take your name?")
   if userinput:
      print(f"hello {userinput.title()}, choose these five weapons!")
      weapons=["Knife atk 5 def 3 AURA INFINITE",
               "Dagger atk 8 def 2 speed 999","Sword atk 20 def 2 honor 999",
               "MAGIC atk 50 def 0 honor WITCH!",
               "LOVE atk 999 def 0 SPECIAL you dont wanna know!"]
      for weapon in weapons:
         print(weapon)
         uinput=input("choose wisely:")
         if uinput=="knife" or "KNIFE" or "Knife":
            print("uhh! LEON??? oh yeah")