# Part 1
start = 2

while start <= 10:
	print(start)
	start = start + 1

# Part 2
start = 2
my_file = open("numbers.txt", 'w')
while start <= 10:
	my_file.write(str(start))
	my_file.write("\n")
	start = start + 1
my_file.close()

# Part 3
lines = [line.rstrip('\n') for line in open('numbers.txt')]

for num in lines:
	print(str(int(num) * 10))
my_file.close()