my_courses = set(['Programming in Python', 'Intro to Java'])
neighbour_courses = set(['Programming in Python', 'Intro to C++'])

union_of_courses = my_courses.union(neighbour_courses)

print(union_of_courses)

union_of_courses.remove("Programming in Python")

print("Number of courses in the set after deletion : " + str(len(union_of_courses)))