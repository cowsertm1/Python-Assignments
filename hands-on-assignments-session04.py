# 1. Write a function called get_user_name() that asks the user for their name and returns it.

def get_user_name():
    user_name = input("What is your name? ")
    return user_name

# 2. Write a function called get_user_age() that asks the user for their age and returns it as a number.

def get_user_age():
    age = int( input("How old are you? ") )
    return age

# 3. Write a function called is_of_legal_age() which takes age as an argument and returns True or False.

def is_of_legal_age(age):

    if age >= 18:
        is_over_18 = True
    else:
        is_over_18 = False

    return is_over_18

# 4. Write a program that asks the user for their age and prints out whether they are of legal age.
    

age = get_user_age()
is_over_18 = is_of_legal_age(age)
if is_over_18:
    print ("Drink up, you are of legal age.")
else:
    print ("Sorry, dude, you ain't welcome around here -- yet.")


# 5. Write a function called get_age_bracket() which takes age as an argument and returns “minor”; “adult”; or “senior”.

def get_age_bracket(age):
    if age < 18:
        age_bracket = "minor"
    elif age > 65:
        age_bracket = "senior"
    else: # catches all folks age >= 18 and age < 65
        age_bracket = "adult"
        
    return age_bracket

# 6. Write a program that asks the user for their name and age and prints out (e.g.)
#
# Maria is an adult.
# John is a minor.
# Catarina is a senior.


name = get_user_name()
age = get_user_age()
age_bracket = get_age_bracket(age)

if age_bracket == "adult":
    print(name + " is an " + age_bracket + ".")
else: # matches age_bracket == "minor" or age_bracket == "senior":
    print(name + " is a " + age_bracket + ".")

