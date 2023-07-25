#remaining age calculator
age = input(" enter your age\n")
age_as_int = int(age)
remaining_age = 90 - age_as_int
remaining_months = remaining_age * 12
remaining_weeks = remaining_age * 52
remaining_days = remaining_age *365
print(f"_you have {remaining_age} age,{remaining_days} days,{remaining_weeks} weeks,{remaining_months} months left")