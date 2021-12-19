#Simple Login System

username=input("Please enter username: \n")
password=input("Please enter password: \n")

while (username != "admin"):
    username=input("NOT A VAILD USERNAME--Please enter username again: \n")

while (password != "pwd"):
    password=input("NOT A VALID PASSWORD--Please enter password again: \n")

print ("ACCESS GRANTED")