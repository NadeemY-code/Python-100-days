print("welcome to tip calculator!\n")
bill = float(input("enter bill amount \n$"))
tip = int(input("enter tip percentage\n"))
people = int(input("enter number of people\n"))
tip_percentage = tip/100
total_tip = bill*tip_percentage
total_bill = total_tip+bill
per_person = total_bill/people
share = round(per_person,2)
print("{:.2f}".format(share))