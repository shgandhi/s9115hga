from __future__ import division
from random import random, randrange, randint, uniform
from math import exp
import datetime
import sys

class Osyczka2(object):
    
    def __init__(self):
        self.max_x = 10, 10, 5, 6, 5, 10
        self.min_x = 0, 0, 1, 0, 1, 0
        
    def random_x_gen(self):
        """
        Generates x's in the range 
        specified by Osyczka2
        Input: None
        Output: x1, x2, x3, x4, x5, x6
        """
        #print "Generating x's"
        x1 = randrange(0,10)
        x2 = randrange(0,10)
        x3 = randrange(1,5)
        x4 = randrange(0,6)
        x5 = randrange(1,5)
        x6 = randrange(0,10)
        return x1, x2, x3, x4, x5, x6
        
    def generate_constraints(self, x_val):
        """
        Generates and checks constraints
        Input: x_val
        Output: True if constraints passed
                False if not passed
        """
        x1, x2, x3, x4, x5, x6 = x_val
        c1 = x1 + x2 - 2 
        c2 = 6 - x1 - x2
        c3 = 2 - x2 + x1
        c4 = 2 - x1 + 3*x2
        c5 = 4 - (x3 - 3)**2 - x4
        c6 = (x5 - 3)**3 + x6 - 4
        if c1 >= 0 and c2 >= 0 and c3 >= 0 and c4 >= 0 and c5 >= 0 and c6 >= 0:
            return True
        else:
            return False
        
    def xval_new_or_mutate(self, flag, existing_x_vals = [0 for _ in xrange(6)]):
        """
        Checks whether to mutate OR
        Generate a new solution
        Input: flag (new/mutate)
        Output: x_val
        """
        if flag == "new":
            new_val = self.random_x_gen()
        if flag == "mutate":
            """"mutate random c"""
            k = randrange(0,6)
            c = list(existing_x_vals)
            mutate_vector = list(self.random_x_gen())
            c[k] = mutate_vector[k]
            new_val = tuple(c)
            #print new_val, "in checker when mutate"
        return new_val
        
    def ok(self, flag, x_val):
        """
        Generates first solution THEN
        Generates solution in loop, till constraints passed
        Input: x_val
        Output: True if constraint passing solution obtained
                False if not
        Calls(In order): xval_new_or_mutate, generate_constraints
        """
        isPassed = self.generate_constraints(x_val)
        while not isPassed:
            x_val = self.xval_new_or_mutate(flag, x_val)
            isPassed = self.generate_constraints(x_val)
        #print "Out of loop", x_val
        return True, x_val
        
    def find_min_max(self, x_valid, iterations = 1000):
        """
        Returns min and max energy for given iterations
        Input: number of iterations
        Output: min_energy, max_energy
        """
        #print lo_val, hi_val
        min_energy = sys.maxint
        max_energy = -1*min_energy
        for _ in xrange(iterations):
            initial_x = self.xval_new_or_mutate("new")
            x, curr_agg = self.generate_energy("new", initial_x)
            #print min_energy, max_energy, curr_agg
            
            if curr_agg > max_energy:
                max_energy = curr_agg
                
            if curr_agg < min_energy:
                min_energy = curr_agg
            
        return min_energy, max_energy
        
        
    def generate_energy(self, flag, x_val):
        """
        Returns energy calculation for passed solution
        Input: flag, x_val
        Output: solution, aggregation of f1 and f2
        """
        isPassed, s = self.ok(flag, x_val)
        if isPassed:
            x1, x2, x3, x4, x5, x6 = s
            f1 = -(25*((x1 - 2)**2) + (x2 - 2)**2 + ((x3 - 1)**2)*((x4 - 4)**2) + (x5 - 1)**2)
            f2 = x1**2 + x2**2 + x3**2 + x4**2 + x5**2 + x6**2
            return s, f1 + f2
            
    def generate_solution(self, flag, existing_x_vals = [0 for _ in xrange(6)]):
        """
        Generates -x vector (new or mutated)
                  -valid x, and corresponding f1 + f2
                  -corresponding min and max energy
                  -corresponding normalized energy
        Input: flag
        Output: x_valid, normalized energy
        """
        if flag == "mutate":
            initial_x = self.xval_new_or_mutate(flag, existing_x_vals)
        if flag == "new":
            initial_x = self.xval_new_or_mutate(flag)
        x_valid, aggregate_energy = self.generate_energy(flag, initial_x)
        x_min_energy, x_max_energy = self.find_min_max(x_valid)
        if x_max_energy != x_min_energy:
            norm_energy = (aggregate_energy - x_min_energy)/(x_max_energy - x_min_energy)
        else:
            norm_energy = 0
        return x_valid, norm_energy
        
    def max_score_local(self, x_val):
        """
        Generates best neighbor upon mutating in one random direction
        Input: x_val to be mutated
        Output: neighbor with best score along index k in x_val
        """
        steps = 100
        best_neigh = list(x_val)
        mutated_neigh = list(x_val)
        k = randrange(0,6)
        step_max = self.max_x[k]
        step_min = self.min_x[k]
        increment = (step_max - step_min)/steps
        for i in xrange(steps):
            #print "here", i, steps
            mutated_neigh = list(mutated_neigh)
            mutated_neigh[k] = int(step_min + increment)
            mutant_x, mutant_e = self.generate_energy("mutate", mutated_neigh)
            best_x, best_e = self.generate_energy("mutate", best_neigh)
            if mutant_e > best_e:
                best_neigh = mutated_neigh
        #print "out"
        return best_neigh
        
def mws():
    """Returns best solution and energy after all runs"""
    max_tries = 100
    max_changes = 50
    threshold = 100
    p = 0.5
    k = 0
    output = " "
    better_count = 0
    confused_count = 0
    best_count = 0
    model = Osyczka2()
    init_solution, init_score = model.generate_solution("new")
    print "Max trials = %d, Max changes = %d, p = %0.2f, threshold = %d" % (max_tries, max_changes, p, threshold)
    for i in range(max_tries):
        x_vec, x_score = model.generate_solution("new")
        #print x_vec, x_score
        #print x_vec, score
        for j in range(max_changes):
            if x_score > threshold:
                return x_vec

            if p < random():
                output += "?"
                confused_count += 1
                x_vec, x_score = model.generate_solution("mutate", x_vec)
                
            else:
                out_x = model.max_score_local(x_vec)
                if (out_x != x_vec):
                    output += "+"
                    x_vec = out_x
                    best_count += 1
                else:
                   output += "."
                   better_count += 1
                   
            if x_score > init_score:
                init_solution = x_vec
                init_score = x_score

            if k % 50 == 0: 
                print "eb = %6f | ? = %d | + = %d |  . = %d | %s" % (init_score, confused_count, best_count, better_count, output)
                output = " "
                better_count = 0
                confused_count = 0
                best_count = 0
            k = k + 1
    print init_solution, init_score

if __name__ == '__main__':
    print "#MWS for the Osyczka2 Model"
    mws()