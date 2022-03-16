#first I want to calculate the total number of pizza slices that can be cut from an 
#increasing unmber of straight cuts, for example, from 1 to 10.	
for n in range(1,11):
 p=(n**2+n+2)/2
 print(p)

#In order to calculate the number of cuts needed, I choose a while circulation to limit the p value. Define the initial value of n and p.
n=1
p=2
while  p < 64:
#print sentences to explain. We should use the command str()
  print("When the number of straight cuts is "+str(n)+", we can get "+str(p)+" pieces of pizza.")
#After print the sentences, let n+=1 and calculate the corresponding p value. Continue to cycle. 
  n+=1
  p=(n**2+n+2)/2
#Exit cycle and use n to print a final sentence as outcome.
print("When the number of straight cuts is "+str(n)+", we get enough pieces of pizza.")

