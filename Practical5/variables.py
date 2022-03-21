a=19245301
b=4218520
c=271
d=b-c
e=a-b
if d>e:
 print("The rate of new cases is greater in 2020")
elif d<e:
 print("The rate of new cases is greater in 2021")
else:
 print("The rate of new cases in 2021 is the same as 2020")


X="True"
Y="False"
W=X and Y
print(W)

X="False"
Y="True"
W=X and Y
print(W)

X="Hello"
Y=""
W=X and Y
print(W)

X=""
Y="Hello"
W=X and Y
print(W)
