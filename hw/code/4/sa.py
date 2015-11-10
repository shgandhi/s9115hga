from __future__ import division
from random import random, randrange
from math import exp
import datetime

class Schaffer(object):
    def __init__(self, min_x = - 10**5, max_x = 10**5):
        self.min_x = min_x
        self.max_x = max_x
        
        
    def random_x_gen(self, lo, hi):
        return randrange(lo, hi)
        
        
    def aggregator(self, x):
        return x**2 + (x-2)**2
        
        
    def find_min_max(self, norm_iter = 10**5):
        lo_val = self.aggregator(self.max_x)
        hi_val = - lo_val
        #print lo_val, hi_val
        for _ in xrange(norm_iter):
            x = self.random_x_gen(self.min_x, self.max_x)
            curr_agg = self.aggregator(x)
            
            if curr_agg < lo_val:
                lo_val = curr_agg
                
            if curr_agg > hi_val:
                hi_val = curr_agg
                
        return lo_val, hi_val
        
        
    def soln(self):
        x = self.random_x_gen(self.min_x, self.max_x)
        
        min_energy, max_energy = self.find_min_max()
        energy_x = self.aggregator(x)
        norm_energy = (energy_x - min_energy)/(max_energy - min_energy)
        
        return x, norm_energy
        

def probability(e, en, t):
    """ Returns the probability function of minimizing SA"""
    if t == 0:
        return 0
    else:
        return exp((e-en)/t)
    
def sa():
    """Returns best solution and energy after all runs"""
    model = Schaffer()
    
    #initial solution
    s, e = model.soln()
    
    #best solution
    sb, eb = s, e
    
    #constants
    kmax = 10000
    emax = -.1
    k = 0
    t = k/kmax
    drunk_jump = 0
    better_jump = 0
    output = " "
    
    while k < kmax and e > emax:
        sn, en = model.soln()
        
        if en < eb:
            eb = en
            sb = sn
            output += "!"
            
        if en < e:
            e = en
            s = sn
            output += "+"
            better_jump += 1
        
        elif probability(e, en, (k/kmax**0.6)) < random():
            e = en
            s = sn
            output += "?"
            drunk_jump += 1
          
        else:
            output += "."
            
        if k % 50 == 0: 
            print "eb = %6f | ? = %2d | + = %2d | %s" % (eb, drunk_jump, better_jump, output)
            output = " "
            drunk_jump = 0
            better_jump = 0
            
        k = k + 1
    return sb, eb
        
if __name__ == '__main__':
    print "#SIMULATED ANNEALER FOR THE SCHAFFER MODEL"
    ta = datetime.datetime.now()
    best_s, best_e = sa()
    tb = datetime.datetime.now()
    print "#Run time %f" % ((ta - tb).microseconds/1000000)

    