from __future__ import division
from random import random, randrange, randint, uniform
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
                x_list.append(uniform(i,j))
            return x_list
        else:
            x_list = [uniform(self.min_x, self.max_x)]
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
        
    def find_min_max(self, iterations = 10):
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

class Golinski(Model):
    def __init__(self):
        Model.__init__(self)
        self.min_x = [2.6, 0.7, 17.0, 7.3, 1, 2.9, 5.0]
        self.max_x = [3.6, 0.8, 5, 28.0, 8.3, 3.9, 5.5]
        
    def generate_chk_constraints(self, x_list):
        x1, x2, x3, x4, x5, x6, x7 = x_list
        f2 = sqrt((745.0*x4/(x2*x3))**2 + 1.69*(10**7))/(0.1*(x6**3))
        a = 745.0*x5/(x2*x3)
        b = 1.575 * (10**8)
        
        c1 = (1.0/(x1*x3*(x2**2)) - (1.0/27.0))
        c2 = (1.0/(x1*x3*(x2**2)) - (1.0/27.0))
        c3 = x4**3/(x2*(x3**2)*(x6**4)) - (1.0/1.93)
        c4 = x5**3/(x2*x3*(x7**4)) - (1.0/1.93)
        c5 = x2*x3 - 40
        c6 = (x1/x2) - 12
        c7 = 5 - (x1/x2)
        c8 = 1.9 - x4 + 1.5*x6
        c9 = 1.9 - x5 + 1.1*x7
        c10 = f2
        c11 = sqrt(a**2 + b)/(0.1*(x7**3))
        if c1 <= 0 and c2 <=  0 and c3 <= 0 and c4 <= 0 and c5 <= 0 and c6 <= 0\
         and c7 <= 0 and c8 <= 0 and c9 <=0 and c10 <= 1300 and c11 <= 1100:
            return True
        else:
            return False
        
    def objectives(self, x):
        x1, x2, x3, x4, x5, x6, x7 = x
        f1 = 0.7854*x1*(x2**2)*((10*(x3**2)/3) + 14.933*x3 - 43.0934) - 1.508*x1*(x6**2 + x7**2) +\
            7.477*(x6**3 + x7**3) + 0.7854*(x4*(x6**2) + x5*(x7**2))
        f2 = sqrt((745.0*x4/(x2*x3))**2 + 1.69*(10**7))/(0.1*(x6**3))
        return(f1, f2)
        
    def solution(self):
        min_energy, max_energy = self.find_min_max()
        x = self.ok(self.random_x_gen())
        energy_x = self.aggregator(x)
        norm_energy = self.normalize(energy_x, min_energy, max_energy)
        return x, norm_energy
        
    def get_energy(self, x):
        min_energy, max_energy = self.find_min_max()
        energy_x = self.aggregator(x)
        norm_energy = self.normalize(energy_x, min_energy, max_energy)
        return energy_x, norm_energy
        
    def mutate_solution(self, x, k = 0):
        min_energy, max_energy = self.find_min_max()
        old_x = x
        mutate_vector = self.random_x_gen()
        old_x[k] = mutate_vector[k]
        new_x = self.ok(old_x)
        energy_x = self.aggregator(new_x)
        norm_energy = self.normalize(energy_x, min_energy, max_energy)
        return new_x, norm_energy

def de(model):
    """
    Returns best solution and energy after all runs
    """
    max_tries = 50
    np = 50
    extrapolate_amt = 0.75
    crossover_prob = 0.3
    epsilon = 0.01
    k = 0
    j = 0
    output = " "
    better_count = 0
    confused_count = 0
    best_count = 0
    threshold = 0
    
    
    frontier_x = []
    frontier_e = []
    def get_frontier():
        for _ in range(np):
            x_val, e_val = model.solution()
            frontier_x.append(x_val)
            frontier_e.append(e_val)
            frontier_x, frontier_e
        return frontier_x, frontier_e
        
    def extrapolate(three_neighbors_index):
        solution = []
        for k in xrange(len(model.min_x)):
            mutate = (frontier_x[three_neighbors_index[0]][k] + 0.75 * \
                (frontier_x[three_neighbors_index[1]][k] - frontier_x[three_neighbors_index[2]][k]))
            if mutate >= model.min_x[k] and mutate <= model.max_x[k]:
                solution.append(mutate)
            else:
                solution.append(frontier_x[three_neighbors_index[randint(0, 2)]][k])
        #print solution
        return solution
        
    #Returns three different things that are not 'parent'.
    def find_replacement(index):
        seen = []
        while len(seen) < 3:
            rand_index = randint(0, np-1)
            if rand_index == index:
                continue
            if rand_index not in seen:
                seen.append(rand_index)
        return seen

    
    print "#"*120
    print "Running DE for ", type(model).__name__
    print "#"*120
    print "Constraints: "
    print "Lower Bound for x= ", model.min_x
    print "Upper Bound for x= ", model.max_x
    print "Max trials = %d, Num = %d, Extrapolate Amount = %f,\
     Prob of Crossover = %f, epsilon = %f" % (max_tries, np, extrapolate_amt, crossover_prob, epsilon)
    print "-"*120
    
    x_vals, e_vals = get_frontier()
    eb = e_vals[0]
    sb = x_vals[0]
    
    total_print = ""
    while j < max_tries:

        if eb == threshold:
            break
        
        for index, s in enumerate(x_vals):
            e = e_vals[index]
            get_neighbors = find_replacement(index)
            #print get_neighbors
            mutant_x = x_vals[get_neighbors[0]]
            mutant_e = e_vals[get_neighbors[0]]
            current_e = e
            temp = "."

            if crossover_prob < random():
                if mutant_e < current_e:
                    current_e = mutant_e
                    x_vals[index] = mutant_x
                    e_vals[index] = mutant_e
                    temp += "+"
                    best_count += 1
        
            else:                
                get_solution = extrapolate(get_neighbors)
                if model.ok(get_solution):
                    #check here
                    x_vals[j] = get_solution
                    unnorm_e, e_vals[j] = model.get_energy(get_solution)
                    current_e = model.get_energy(get_solution)
                    temp = "+"
                    best_count += 1
    
            if current_e < eb and current_e >= threshold:
                temp = "?"
                confused_count += 1
                eb = current_e
                sb = x_vals[j]

            total_print += temp
            if k % 50 == 0: 
                print "eb = %6f | %s" % (eb, total_print)
                total_print = " "
                better_count = 0
                confused_count = 0
                best_count = 0
            k = k + 1
    print "-"*120
    print "Best solution: ", sb
    print "Best energy: ", sb
    return frontier_x
    
if __name__ == '__main__':
    print "Generic Experiments"
    
    for model in [Golinski]:
        for optimizer in [de]:
            optimizer(model())