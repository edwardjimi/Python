#Student gets 10% discount

choice=input("Please enter student, staff or customer: \n")
items=float(input("Please enter cost of items: \n"))

discount = (10/100) * items

if choice == "student":
    print ("student gets 10% discount:£", items - discount)

if choice == "staff":
    print ("staff:£", items)

if choice == "customer":
    massage = "Does not qualify for any discount."
    print ("Unknown:", massage, "£",items)