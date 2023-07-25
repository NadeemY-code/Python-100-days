#bmi 2.0
weight = float(input("enter the weight in kg\n"))
height = float(input("enter the height in m2\n"))
bmi = round(weight/height**2)
if bmi < 18.5:
    print(f"your bmi is {bmi} ,you are underweight\n")
elif bmi < 25:
        print(f"your bmi is {bmi} ,you are normal weight\n")
elif bmi < 30:
            print(f"your bmi is {bmi} ,you are over weight\n")
elif bmi < 35:
                print(f"your are bmi is {bmi} , you are obese\n")
else:
    print(f"(your bmi is {bmi} ,you are clinically obese\n")                

    
    


