#Dicts
import time

#Ex2
def histogram(s):
    d = dict()
    for c in s:
        d[c] = 1 + d.get(c, 0)
    return d
    
#my_dict = histogram("abracadabra")

#Ex3
def print_hist(d):
    print d.keys()
    
#print_hist(my_dict)

#Ex4 
def reverse_lookup(d, v):
    key_list = []
    for k in d:
        if d[k] == v:
            key_list.append(k)
    return key_list
    
#print reverse_lookup(my_dict, 2)

#Ex5
#http://stackoverflow.com/questions/7423428/python-dict-get-vs-setdefault

#Ex6
known = {0:0, 1:1}

def fibonacci(n):
    if n in known:
        return known[n]
        
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res
    
def fib_no_memo(n): 
    if n in known:
        return known[n]
        
    total = fib_no_memo(n-1) + fib_no_memo(n-2)
    return total
    
#t1 = time.clock()
#val2 = fib_no_memo(50)
#print val2, time.clock() - t1

t0 = time.clock()
val1 = fibonacci(50)
print val1, time.clock() - t0


            