# Homework 2
# sgandhi@ncsu.edu
   
# Solution 3.4
for i in range(40):
    print "=",
print "\n"
print "Solution 3.4"
for i in range(40):
    print "=",
print "\n"
    
def do_twice(f, val):
    f(val)
    f(val)
    
def do_four(f, val):
    f(print_twice, val)
    f(print_twice, val)
    
def print_twice(stuff):
    print stuff
    
print "Output of do_twice"
do_twice(print_twice, "spam")

print "Output of do_four"
do_four(do_twice, "spam")
