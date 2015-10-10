from random import randint

def solution_separator():
    for i in range(40):
        print "=",
    print "\n"
    
#10.15 Ex 8 Part 1
def has_duplicate(in_list):
    if isinstance(in_list, list):
        sort_list = sorted(in_list)
        for i in range(len(sort_list)):
            if i > 0:
                if sort_list[i] == sort_list[i-1]:
                    return True

#10.15 Ex 8 Part 2
def birthday_paradox(in_list):
    total = 0
    if isinstance(in_list, list):
        sort_list = sorted(in_list)
        for i in range(len(sort_list)):
            rep = sort_list.count(sort_list[i])
            if rep > 1:
                if sort_list[i-1] != sort_list[i]:
                    total += rep
    print total, "people have birthdays on same date"
 
 
solution_separator()
print "Solution 10.15.8 - 1"
solution_separator()

#Call has_duplicate 
t = list(raw_input("Enter the elements of the list here: ").split())
check = has_duplicate(t)
print "Returned True; Duplicate exists!" if check else "No Duplicate"

while True:
    if_continue = raw_input("To check again, press Y. To go to birthday_paradox press N: ")
    if if_continue == 'Y':
        t = list(raw_input("Enter the elements of the list here: ").split())
        check = has_duplicate(t)
        print "Returned True; Duplicate exists!" if check else "No Duplicate"
    else:
        break

#Call birthday_paradox            
solution_separator()
print "Solution 10.15.8 - 2"
solution_separator()

birthday_list = []
for i in range(23):
    birthday_list.append(randint(1,31))
print "The random birthday list: ",birthday_list
birthday_paradox(birthday_list)    
