from __future__ import division
from random import randint

#10.15 Ex 8 Part 2
def birthday_paradox(num_item, num_iter):
    total_list = []
    for val in range(num_iter):
        birthday_list = []
        for i in range(num_item):
            birthday_list.append(randint(1,31))
        total = 0
        if isinstance(birthday_list, list):
            sort_list = sorted(birthday_list)
            for i in range(len(sort_list)):
                rep = sort_list.count(sort_list[i])
                if rep > 1:
                    if sort_list[i-1] != sort_list[i]:
                        total += rep
        total_list.append(total/len(birthday_list))
    print "The size of the birthday list: ", len(birthday_list)
    print "Total num of iterations: ", num_iter
    print "The probability of having the same birth date is: ", sum(total_list)/num_iter
 

if __name__== '__main__':
    birthday_paradox(23, 1000)    
