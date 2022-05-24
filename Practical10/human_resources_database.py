#create a class "staff‘ to store data
class Staff:
    def __init__(staff, first_name, last_name, location, role): #The content should include these data
        staff.first_name = first_name
        staff.last_name = last_name
        staff.location = location
        staff.role = role
    def myfunc(staff): #use this function to output results
        print("Full name:" + staff.first_name + " " + staff.last_name + " Location:" + staff.location + " Role:" + staff.role)
#example:
#p1=Staff("Rob", "Young", "Edinburgh", "faculty")
#p1.myfunc()
#the result is:
#Full name:Rob Young Location:Edinburgh Role:faculty
