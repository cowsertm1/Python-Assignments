# Part 1
name = input("What's your name? ")
graduation = input("What's your graduation year? ")
my_file = open("userdata.txt", 'w')
my_file.write("The user is called " + name + ".")
my_file.write("\n")
my_file.write("S/he will be graduating in " + graduation + ".")
my_file.close()

# Part 2
lines = [line.rstrip('\n') for line in open('userdata.txt')]
name = lines[0].split()[-1].split(".")[0]
graduation = lines[1].split()[-1]

print(name + " will graduate in " + graduation)
