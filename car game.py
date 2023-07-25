command = ''
started = False
while True:
   command = input(">").lower()
   if command == "start" :
      if started :
         print("car is already started")
      else:
         started = True
         print("car started")
   elif command == "stop":
      if not started:
         print("car is already stopped")
      else:
         started = False
      print('car stopped.')
      
   elif command == "help":
      print("""
start- car has started
stop - car stopped
quit-quit""")
   elif command == "quit":
      break
   else:
       print("sorry, i don't understand that")
