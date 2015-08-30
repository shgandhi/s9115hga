# Homework 2
# sgandhi@ncsu.edu
   
# Solution 3.5
def draw_hor_line(k):
    for cross in range(k):
        print "+",
        for hypen in range(2*k):
            print "-",
    print "+"
    
def draw_ver_line(k):
    for vertical in range(2*k):
        for slash in range(k):
            print "|",
            for space in range(2*k):
                print " ",
        print "|"
        
def draw_grid(size):
    for i in range(size):
        draw_hor_line(size)
        draw_ver_line(size)
    draw_hor_line(size)
    
# draws grid 2X2
draw_grid(2)

#draws grid 4X4
draw_grid(4)
