#I have found multiple ways to calculate it.

#frist define an original value of y
y=0
#display the first 10 values from 1 to 10. I choose "for" cycle to demostrate.
for x in range (1,11):
#I use the cumulation method.
 y=y+x
 print(y)

#Also, I want to try the sum formula.
y=0
for x in range (1,11):
 y=(1+x)*x/2 #use the summation formula.
 print(y)

#After that, I used "while" cycle.
y=0
x=1
while x < 11:
 y=y+x #the method is also cumulation.
 x=x+1
 print(y)
