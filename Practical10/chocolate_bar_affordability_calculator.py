#create a function
def calculator():
    total_money = input("Type the total money here: ")
    price = input("Type the price here: ") #ask users to input totall money and price
    x = int(total_money)// int(price) #calculate the number of bars can be bought
    y = int(total_money) % int(price) #calculate the amount of change 
    class bar: #I can print the result directly,but I tried a more complicated method......
          def __init__(self):
              self.number = str(x)
              self.change = str(y)
    def bar_calculator():
        return bar()
    s = bar_calculator()
#print the outcome
    print("The number of bars that can be bought is " + s.number + ".")
    print("The change that will be left over is " + s.change + ".")

#example:
# calculator()
# Type the total money here: 100
# Type the price here: 8
# The number of bars that can be bought is 12.
# The change that will be left over is 4.
