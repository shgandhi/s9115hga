# Homework 2
# sgandhi@ncsu.edu
   
# Solution 3.3
def right_justify(s):
    num_spaces = 70 - len(s)
    offset_string = ""
    for i in range(num_spaces):
        offset_string += " "
    offset_string += s
    print offset_string
    
    #print offset_string.index(s)
    #print offset_string[69]
    
right_justify("Allen")