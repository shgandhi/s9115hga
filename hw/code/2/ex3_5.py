# Homework 2
# sgandhi@ncsu.edu
   
# Solution 3.5
for i in range(40):
    print "=",
print "\n"
print "Solution 3.5"
for i in range(40):
    print "=",
print "\n"
    
def draw_hor_line(k):
    for cross in range(k):
        print "+",
        for hypen in range(4):
            print "-",
    print "+"
    
def draw_ver_line(k):
    for vertical in range(4):
        for slash in range(k):
            print "|",
            for space in range(4):
                print " ",
        print "|"
        
def draw_grid(size):
    print "Grid with ", size,"rows and ", size, "columns"
    for i in range(size):
        draw_hor_line(size)
        draw_ver_line(size)
    draw_hor_line(size)
    
# draws grid 2X2
draw_grid(2)

#draws grid 4X4
draw_grid(4)

for i in range(40):
    print "=",
