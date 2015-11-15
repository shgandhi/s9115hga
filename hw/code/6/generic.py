from __future__ import division
from random import random, randrange, randint
from abc import ABCMeta, abstractmethod
from math import exp, sqrt, sin
import datetime
import sys

class Model(object):
    """
    Fills in the generic candidate
    Computes objective score for each candidate
    """
    __metaclass__ = ABCMeta
    
    def __init__(self):
        """
        Initializes variable bounds for 
        - energy
        - x vector (initialized in subclass)
        """
        self.min_agg = sys.maxint
        self.max_agg = -self.min_agg
        self.min_x = 0
        self.max_x = 0
        
    def random_x_gen(self):
        """
        Generates x's in the range 
        specified by the subclass model
        Input: None
        Output: x vector
        """
        if isinstance(self.min_x, list):
            x_list = []
            for i,j in zip(self.min_x, self.max_x):
                x_list.append(randrange(i,j))
            return x_list
        else:
            x_list = [randrange(self.min_x, self.max_x)]
            return x_list
            
    def generate_chk_constraints(self, x_list):
        #overridden by subclass
        """
        Generates and checks constraints
        Input: x_list
        Output: True if constraints passed/no constraints
                False if not passed
        """
        return True
            
    def ok(self, x_list):
        """
        Generates first solution THEN
        Generates solution in loop, till constraints passed
        Input: x_list
        Output: valid x vector
        """
        isPassed = self.generate_chk_constraints(x_list)
        while not isPassed:
            x_list = self.random_x_gen()
            isPassed = self.generate_chk_constraints(x_list)
        return x_list
        
    def aggregator(self, x_list):
        """
        Generates energy by summing all objectives got from subclass
        
        """
        agg = 0
        for obj in self.objectives(x_list): 
            agg += obj
        return agg
        
    @abstractmethod
    def objectives(self, x):
        raise NotImplementedError("Must override objectives()")
        
    def find_min_max(self, iterations = 100):
        for _ in xrange(iterations):
            while True:
                solution = self.random_x_gen()
                if self.ok(solution):
                    break
                
            curr_agg = self.aggregator(solution)
            
            if curr_agg > self.max_agg:
                self.max_agg = curr_agg
                
            if curr_agg < self.min_agg:
                self.min_agg = curr_agg
            
        return self.min_agg, self.max_agg
            
    def normalize(self, energy, min_energy, max_energy):
        norm_energy = (energy - min_energy)/(max_energy - min_energy)
        return norm_energy
        
class Schaffer(Model):
    def __init__(self):
        Model.__init__(self)
        self.min_x = -10**5
        self.max_x = 10**5
        
    def objectives(self, x):
        f1 = (x[0])**2
        f2 = (x[0]-2)**2
        return(f1, f2)
        
    def solution(self):
        min_energy, max_energy = self.find_min_max()
        x = self.ok(self.random_x_gen())
        energy_x = self.aggregator(x)
        norm_energy = self.normalize(energy_x, min_energy, max_energy)
        return x, norm_energy
        
    def mutate_solution(self, x, k = 0):
        min_energy, max_energy = self.find_min_max()
        old_x = x
        mutate_vector = self.random_x_gen()
        old_x[k] = mutate_vector[k]
        new_x = self.ok(old_x)
        energy_x = self.aggregator(new_x)
        norm_energy = self.normalize(energy_x, min_energy, max_energy)
        return new_x, norm_energy
    
        
class Osyczka2(Model):
    def __init__(self):
        Model.__init__(self)
        self.min_x = [0, 0, 1, 0, 1, 0]
        self.max_x = [10, 10, 5, 6, 5, 10]
        
    def generate_chk_constraints(self, x_list):
        x1, x2, x3, x4, x5, x6 = x_list
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
        
    def objectives(self, x):
        x1, x2, x3, x4, x5, x6 = x
        f1 = -(25*((x1 - 2)**2) + (x2 - 2)**2 + ((x3 - 1)**2)*((x4 - 4)**2) + (x5 - 1)**2)
        f2 = x1**2 + x2**2 + x3**2 + x4**2 + x5**2 + x6**2
        return(f1, f2)
        
    def solution(self):
        min_energy, max_energy = self.find_min_max()
        x = self.ok(self.random_x_gen())
        energy_x = self.aggregator(x)
        norm_energy = self.normalize(energy_x, min_energy, max_energy)
        return x, norm_energy
        
    def mutate_solution(self, x, k = 0):
        min_energy, max_energy = self.find_min_max()
        old_x = x
        mutate_vector = self.random_x_gen()
        old_x[k] = mutate_vector[k]
        new_x = self.ok(old_x)
        energy_x = self.aggregator(new_x)
        norm_energy = self.normalize(energy_x, min_energy, max_energy)
        return new_x, norm_energy
        
        
class Kursawe(Model):
    def __init__(self):
        Model.__init__(self)
        self.min_x = [-5, -5, -5]
        self.max_x = [5, 5, 5]
        
    def objectives(self, x):
        f1 = -10*(exp(-0.2*sqrt(x[0]**2 + x[1]**2)) + exp(-0.2*sqrt(x[1]**2 + x[2]**2)))
        f2 = sum([((abs(x[i]))**0.8 + 5*sin(x[i])) for i in xrange(0,3)])
        return(f1, f2)
        
    def solution(self):
        min_energy, max_energy = self.find_min_max()
        x = self.ok(self.random_x_gen())
        energy_x = self.aggregator(x)
        norm_energy = self.normalize(energy_x, min_energy, max_energy)
        return x, norm_energy
        
    def mutate_solution(self, x, k = 0):
        min_energy, max_energy = self.find_min_max()
        old_x = x
        mutate_vector = self.random_x_gen()
        old_x[k] = mutate_vector[k]
        new_x = self.ok(old_x)
        energy_x = self.aggregator(new_x)
        norm_energy = self.normalize(energy_x, min_energy, max_energy)
        return new_x, norm_energy
    
    
def mws(model):
    """
    Returns best solution and energy after all runs
    """
    
    def max_score_local(x_val, k = 0):
        """
        Generates best neighbor upon mutating in one random direction
        Input: x_val to be mutated
        Output: neighbor with best score along index k in x_val
        """
        steps = 10
        best_neigh = x_val[:]
        mutated_neigh = x_val
        if isinstance(model.max_x, list):
            step_max = model.max_x[k]
            step_min = model.min_x[k]
        else:
            step_max = model.max_x
            step_min = model.min_x
        increment = (step_max - step_min)/steps
        for i in xrange(steps):
            #print "here", i, steps
            #print "mut", mutated_neigh, "inc", int(step_min + increment), "xval", x_val
            mutated_neigh[k] = int(step_min + increment*i)
            #print "mut", mutated_neigh, "inc", int(step_min + increment*i), "xval", x_val
            mutated_neigh = model.ok(mutated_neigh)
            mutant_e = model.aggregator(mutated_neigh)
            best_e = model.aggregator(best_neigh)
            #print mutated_neigh, best_neigh
            #print mutant_e!= best_e
            if mutant_e > best_e:
                #print "here"
                best_neigh = mutated_neigh
        #print "out"
        #print best_neigh
        return best_neigh
    
    
    max_tries = 100
    max_changes = 50
    threshold = 100
    p = 0.5
    k = 0
    output = " "
    better_count = 0
    confused_count = 0
    best_count = 0
    init_solution, init_score = model.solution()
    print "#"*120
    print "Running MWS for ", type(model).__name__
    print "#"*120
    print "Constraints: "
    print "Lower Bound for x= ", model.min_x
    print "Upper Bound for x= ", model.max_x
    print "Max trials = %d, Max changes = %d, p = %0.2f, threshold = %d" % (max_tries, max_changes, p, threshold)
    print "-"*120
    for i in range(max_tries):
        x_vec, x_score = model.solution()
        #print x_vec, x_score
        #print x_vec, score
        for j in range(max_changes):
            c = randrange(0, len(init_solution))
            if x_score > threshold:
                return x_vec

            if p < random():
                x_vec, x_score = model.mutate_solution(x_vec, c)
                output += "?"
                confused_count += 1
                
            else:
                out_x = max_score_local(x_vec, c)
                #print out_x, x_vec
                if out_x == x_vec:
                    output += "."
                    better_count += 1
                else:
                    #print "here?"
                    output += "+"
                    x_vec = out_x
                    best_count += 1
                   
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
    print "-"*120
    print "Best solution: ", init_solution
    print "Best energy: ", init_score

    
def probability(e, en, t):
    #Returns the probability function of minimizing SA
    if t == 0:
        return 0
    else:
        return exp((e-en)/t)
        
def sa(model):
    #Returns best solution and energy after all runs
    
    #initial solution
    s, e = model.solution()
    
    #best solution
    sb, eb = s, e
    
    #constants
    kmax = 1000
    emax = -.1
    k = 0
    t = k/kmax
    drunk_jump = 0
    better_jump = 0
    output = " "
    print "#"*120
    print "Running SA for ", type(model).__name__
    print "#"*120
    print "kmax: ", kmax
    print "emax: ", emax
    print "Constraints: "
    print "Lower Bound for x= ", model.min_x
    print "Upper Bound for x= ", model.max_x
    print "-"*120

    while k < kmax and e > emax:
        #print "I am here"
        sn, en = model.solution()
        #print sn, en
        
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
            
        if k % 25 == 0: 
            print "eb = %6f | ? = %2d | + = %2d | %s" % (eb, drunk_jump, better_jump, output)
            output = " "
            drunk_jump = 0
            better_jump = 0
            
        k = k + 1
    print "-"*120
    print "Best solution: ", sb
    print "Best energy: ", eb
    return sb, eb

    
if __name__ == '__main__':
    print "Generic Experiments"
    
    for model in [Schaffer, Osyczka2, Kursawe]:
        for optimizer in [sa, mws]:
            optimizer(model())