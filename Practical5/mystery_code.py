# What does this piece of code do?
# Answer:For each process, generate an random integer from 1 to 100, repeate 
#        the process for 10 times and print n when process==9.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

# define a number of progress 
progress=0
#progress will begin with 0 and end with 9, which means n will be renerated 
#10 times.
while progress<10:
# progress=progress+1
	progress+=1
#draws a number between 1 and 100
	n = randint(1,100)

#print the final n
print(n)
