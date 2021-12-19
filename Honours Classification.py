#def grade - Honours Classification

first_name=input("Please enter first name: ")
last_name=input("Please enter last name: ")
mark=int(input("Please enter weighted mark: "))


if (mark<0 or mark>100):
     print("Mark must be between 0 and 100")
else:
      if(mark>=70):
         honours="First Class."
         message="Excellent, well done!"
      elif(mark>=60):
         honours="Upper Second."
         message="Very good, well done!"
      elif(mark>=50):
         honours="Lower Second."
         message="Good, well done!"
      elif(mark>=40):
         honours="Third Class."
         message="Work harder next time!"
      else:
         honours="Failed."
         message="Oh dear, try again!"

def grade (mark):
    mark = honours, message
    print (honours, message, first_name, last_name)
    

