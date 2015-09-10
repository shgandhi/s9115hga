##Summary

###(i) Reference: Jan Malburg and Gordon Fraser, Saarland University, ASE-2011. [Combining Search Based and Constraint Based Testing](http://dl.acm.org/citation.cfm?id=2190094). 

###(ii) Keywords:
* (ii1) **Search Based Testing:** It defines the testing problem as a search problem and applies efficient algorithms to find inputs that can serve as tests.

* (ii2) **Symbolic Execution:** The key idea here is to generalize testing by using *unknown* symbolic variables in evaluation. A symbolic executor collects all path conditions (eg. if clauses) and operations on symbolic variables along the path selected by a tester. Then these conditions are fed to a constraint solver to derive all inputs that make the program follow this path, as done in *classic constraint based testing*

* (ii3) **Dynamic Symbolic Execution (DSE):** A dynamic symbolic executor evaluates and collects path branching conditions, updates symbolic states whenever they are changed, this is done along a path selected by executing a program for a random value. One of the collected path constraints is negated to describe an unexecuted path, and exploration is continued along this path.

* (ii4) **Branch Coverage:** It is a testing metric which considers a branch in a code (eg. if statements, loops) to be covered only if it is executed both ways, i.e. the branch must have been true at least once, and false atleast once during testing.

###(iii) Artifacts:

* (iii1) **Motivation:** The most successful approaches to automatically generate test data achieving high test coverage are usually based on meta-heuristic search or constraint solvers. While the search based testing is scalable, and can work with any code and test criterions, its' success depends on the availability of suitable fitness functions that can guide the search to an optimal solution. The presence of local optima/ plateaux in the search landscape described by the fitness function can lead to getting stuck in local optima/degrade to random search, respectively. Similarly, constraint based testing that uses DSE to generate constraints, while efficient, has limited scalability as there are certain domain of constraints it can not handle such as non-linear or floating point arithmetics. These open issues called for the need of developing a testing method that surpassed the given methods.

* (iii2) **Hypotheses:** The authors realized that the two approaches with the best coverage i.e the search based and constraint solver based methodolgies complemented each other in terms of their advantages and disadvantages. Though, there had been previous attempts to combine the two, those methods were more focussed on hooking the two techniques together rather than intrinsically combining them. The authors decided to use a standard Genetic Algorithm for generating tests, with DSE being the mutation operator. This would negate the the problems of the search based method getting stuck in local optima, and when the constraint solver encountered unsolvable constraints, it would fall back on standard mutation. This was expected to handle the drawbacks of both the methods.

* (iii3) **New Results:** The authors developed a prototype based on Java PathFinder and evaluated it on a set of 20 case study objects containing a combination of linear/non-linear constraints, and used 50,000 test executions to compare the performance of *random search, genetic algorithm (GA), DSE, GA-DSE (proposed hybrid)*. The results were as follows -
  *  GA-DSE achieved highest coverage on 18 out of 20 examples. In two linear constraints, it had same performance as GA and random search.
  *  GA-DSE achieved higher coverage than DSE on 9 out of 20 examples. For the other 11, DSE and GA-DSE achieved equivalent performance.
  *  DSE outperforms GA and random search on 15/20 examples, i.e. all except non linear constraints. Those 5 cases are included in the above point of 9/20 where GA-DSE is superior to all methods.
  *  The approach does not cover any coverage criteria other than branch coverage, and it does not take test suite size into consideration.

* (iii4) ****

###(v) Suggested Improvements:
* (v1) Metrics other than branch coverage could have been used to indicate more comprehensive performance comparison.
* (v2) An equivalent mix of linear and non linear constraints could have been chosen for the benchmark case study examples. The paper used 15 linear and 5 non-linear/floating arithmetic cases.
* (v3) The table used for comparison could have been replaced by a more insightful visualization.

