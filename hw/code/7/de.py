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
        #print "is ok"
        isPassed = self.generate_chk_constraints(x_list)
        while not isPassed:
            x_list = self.random_x_gen()
            isPassed = self.generate_chk_constraints(x_list)
            #print isPassed
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
        #print "in min max"
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
            #print self.min_agg, self.max_agg
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
        
        
class Golinski(Model):
    def __init__(self):
        Model.__init__(self)
        self.min_x = [2.6, 0.7, 17.0, 7.3, 7.3, 2.9, 5.0]
        self.max_x = [3.6, 0.8, 28.0, 8.3, 8.3, 3.9, 5.5]
        
    def generate_chk_constraints(self, x_list):
        #print x_list
        x1, x2, x3, x4, x5, x6, x7 = x_list
        #if x6 or x2 or x3 or x7 == 0:
        #    return False
        #print "here"
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
        if c1 > 0:
            return False
        if c3 > 0:
            return False
        if c4 > 0:
            return False
        if c5 > 0:
            return False
        if c6 > 0:
            return False
        if c7 > 0:
            return False
        if c8 > 0:
            return False
        if c9 > 0:
            return False
        if c10 > 1300:
            return False
        if c11 > 1100:
            return False
        
        return True
        
    def objectives(self, x):
        x1, x2, x3, x4, x5, x6, x7 = x
        f1 = 0.7854*x1*(x2**2)*((10*(x3**2)/3) + 14.933*x3 - 43.0934) - 1.508*x1*(x6**2 + x7**2) +\
            7.477*(x6**3 + x7**3) + 0.7854*(x4*(x6**2) + x5*(x7**2))
        f2 = sqrt((745.0*x4/(x2*x3))**2 + 1.69*(10**7))/(0.1*(x6**3))
        return(f1, f2)
        
    def solution(self):
        #print "in sol"
        min_energy, max_energy = self.find_min_max()
        x = self.ok(self.random_x_gen())
        energy_x = self.aggregator(x)
        norm_energy = self.normalize(energy_x, min_energy, max_energy)
        #print x, norm_energy
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
        #print x, "in mutate", mutate_vector, k
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
            mutated_neigh[k] = step_min + increment*i
            mutated_neigh = model.ok(mutated_neigh)
            mutant_e = model.aggregator(mutated_neigh)
            best_e = model.aggregator(best_neigh)
            if mutant_e > best_e:
                best_neigh = mutated_neigh
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
    #print init_solution, init_score
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
                if out_x == x_vec:
                    output += "."
                    better_count += 1
                else:
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
        sn, en = model.solution()

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

def de(model):
    """
    Returns best solution and energy after all runs
    """
    max_tries = 100
    np = 100
    extrapolate_amt = 0.75
    crossover_prob = 0.3
    epsilon = 0.01
    k = 0
    j = 0
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
        i = 0
        for k in xrange(len(model.min_x)):
            mutate = (frontier_x[three_neighbors_index[i]][k] + 0.75 * \
                (frontier_x[three_neighbors_index[i+1]][k] - frontier_x[three_neighbors_index[i+2]][k]))
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

            else:                
                get_solution = extrapolate(get_neighbors)
                if model.ok(get_solution):
                    x_vals[index] = get_solution
                    unnorm_e, e_vals[index] = model.get_energy(get_solution)
                    current_e = model.get_energy(get_solution)
                    temp = "+"

            if current_e < eb and current_e >= threshold:
                temp = "?"
                eb = current_e
                sb = x_vals[index]
            
            j = j + 1
            total_print += temp
            if j % 25 == 0: 
                print "eb = %6f | %s" % (eb, total_print)
                total_print = " "
    print "-"*120
    print "Best solution: ", sb
    print "Best energy: ", eb
    return frontier_x
    
if __name__ == '__main__':
    print "Generic Experiments"
    
    for model in [Golinski]:
        for optimizer in [sa, mws, de]:
            optimizer(model())