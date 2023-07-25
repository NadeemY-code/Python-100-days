import random
random_integer = random.randint(1,10)
print(random_integer)
#for floating numbers.(it will print 0-0.99 but not 1)
random_float = random.random()
print(random_float)
#now for floating numbers that are above 0 and below 1.(we simply have to multiply the random_floating number)
#i.e,if we need a floating number between 1-5 we have to multiply floating nuumber with 5.
new_float=random_float*5
print(new_float)
