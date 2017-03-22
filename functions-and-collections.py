""" 

As we saw in class, in Python arguments passed to a function are
treatedly differently depending on whether they are a "normal"
variable or a collection. In this file we will go over some additional
examples so that you get used to this behavior:

1. Write a program that assigns some value to a global variable called
"my_global_string". 

Add to your program a function called "modify_string" that receives a
string as an argument. (Call the argument something like "string_arg",
eg.) Have that function try to set the string to a different value and
then return.

In your program, call that function, passing it my_global_string as an
argument, and then print out the value of my_global_string.

Observe what happens.

2. Repeat exercise one but for a number (integer) variable. Observe
what happens.

3. Write a program that creates a dictionary called 'peoples_ages'
mapping names to ages. Insert into the dictionary data for 3 people.

4. Add to that program a function called "modify_dictionary" that
takes a dictionary as an argument. (When defining the function, be
sure to name the argument something *other* than 'peoples_ages'.) In
that function, 

(i) add a new element to the argument (e.g., "marisa" => 75)
(ii) modify the age of one of the people listed in peoples_ages
(iii) remove from the argument one element present in peoples_ages.

In your program, run that function and then print out the contents of
peoples_ages. Observe what happened. Which of the three changes made
within the function modify_dictionary to its argument were actually
being done on (the global collection) peoples_ages?

5. Add to that program a new function called "modify_dictionary_2"
that takes a dictionary as an argument. (As above, when defining the
function, be sure to name the argument something *other* than
'peoples_ages'. Below, and for the sake of clarity, I assumed the
argument is 'dic_passed_as_argument'.) In this function, to to "clear"
or "empty" the dictionary passed as an argument by assigning to it an
empty dictionary, e.g.:

dic_passed_as_argument = {}

As above, have your program execute this function and then print out
the dictionary peoples_ages. What happened?

6. Edit the function modify_dictionary_3 so that, rather than assigning

dic_passed_as_argument = {}

it instead calls 

dic_passed_as_argument.clear()

Why did this work while our attempt in question 5 failed?


7. To really drive the point home, do a similar experiment with a list
and a set. See if they behave the same way as dictionaries.

===

So, as we see above Python lets your functions modify the arguments
passed to functions -- as long as those arguments are *collections*. 

Does that mean you should do it? Nope. To keep your code clean and
easy to maintain, if your function wants to share some modified data
with the rest of your program, the way to do so is by having your
function *return* that modified data -- never by directly modifying
its arguments.


"""
