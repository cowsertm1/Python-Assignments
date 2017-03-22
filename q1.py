dict = {}
name = input("Enter your name : ")
age = input("Enter your age : ")
dict[name] = age
name = input("Enter your name : ")
age = input("Enter your age : ")
dict[name] = age
name = input("Whose age do you want to know? : ")

## adding check to see if entered name is in our dictionary

## if it is in dictionary, then we will print the age
if name in dict:
	print(name + " is " + dict[name] + " years old!")
## if not, we will print some message
else:
	print("Name not found!")