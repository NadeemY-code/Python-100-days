print("welcome to the treasure hunt game\n")
choice1 = input('enter your choice "left" or "right"\n').lower()
if choice1 == "left":
  choice2 = input("you are near a lake will you swim or wait\n").lower()
  if choice2 == "wait":
      choice3 = input("the boat has arrived,there are 3 doors red , yellow , green which one would you choose\n").lower()
      if choice3 == "red":
         print("the treasue is yours\n") 
      elif choice3 == "yellow":
            print("you are killed by lions\n")
      elif choice3 == "green":
               print("killed by ninjas\n")
      else:
         print("eaten by crocodile,game over\n")
  else:
   print("died due to poison , game over") 
else:
   print("a tree hit you and you died, game over")        
        
        
#error was using  two = signs at choosing places e.g:- choice1 = input not choice1 == input: