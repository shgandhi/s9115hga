# Homework 2
# sgandhi@ncsu.edu

"""
# Solution 3.1
repeat_lyrics()

def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."

def repeat_lyrics():
    print_lyrics()
    print_lyrics()
   
# Solution 3.2
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
    
def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."
    
repeat_lyrics()
"""

def right_justify(s):
    num_spaces = 70 - len(s)
    offset_string = ""
    for i in range(num_spaces + 1):
        offset_string += " "
    offset_string += s + "\n"
    print offset_string
    print offset_string.index(s[0])
    print offset_string.index(s[0 + len(s) - 1])

right_justify("blahblahblaaaah")