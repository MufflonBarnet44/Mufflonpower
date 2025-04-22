#EuroJackopotto
import random

# Select 5 randomnumbers between 1- 50
my_numbers = random.sample(range(1, 51), 5)
my_numbers.sort()   

for num in my_numbers:
    print(num, end=" ")    

print()    

 # Select 2 randomnumbers between 1- 10
ext_numbers = random.sample(range(1, 11), 2)
ext_numbers.sort()   

for ex_num in ext_numbers:
    print(ex_num, end=" ") 



