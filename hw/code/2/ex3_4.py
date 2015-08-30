# Homework 2
# sgandhi@ncsu.edu
   
# Solution 3.4
def do_twice(f, val):
    f(val)
    f(val)
    
def do_four(f, val):
    f(print_twice, val)
    f(print_twice, val)
    
def print_twice(stuff):
    print stuff
    
#do_twice(print_twice, "spam")
do_four(do_twice, "spam")
