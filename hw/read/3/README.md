##Summary

###(i) Reference: Matt Staats, University of Minnesota and Corina Pasareanu, Carnegie Mellon University/NASA Ames, ACM, 2010. [Parallel Symbolic Execution for Structural Test Generation](http://dl.acm.org/citation.cfm?id=1831708.1831732). 

###(ii) Keywords:
* (ii1) **Length of Test Suite:** A test case is a sequence of statements _t = <s1,s2, . . . ,sl>_ of length l. The length of a test suite is defined as the sum of the lengths of its test cases.

* (ii2) **Collateral coverage:** When a test case targeting a particular coverage goal also satisfies further coverage goals by accident, it is called collateral or serendipitious coverage.

* (ii3) **Infeasible coverage:** Infeasibility in coverage goals means that there exists no test that would exercise those goals; this is an instance of the undecidable infeasible path problem

* (ii4) **Genetic Algorithm:** Genetic Algorithms (GAs) qualify as meta-heuristic search technique that attempt to imitate the mechanisms of natural adaptation in computer systems. A population of chromosomes is evolved using genetics-inspired operations, where each chromosome represents a possible problem solution.

###(iii) Artifacts:

* (iii1) **Motivation:**  While generating tests from the source code satisfying a certain coverage criteria, the fundamental assumptions are that all coverage goals are equally important, equally difficult to reach and independent of each other. The general approach of devising a test case that exercises a particular coverage goal at a time, ignores the possibility of a coverage goal being infeasible, or difficult to satisfy or causing collateral coverage. These problems cannot be efficiently predicted, hence the authors proposed an approach to mitigate them. Instead of tackling individual coverage goals with distinct test cases, the authors suggested an approach to optimize the entire test suite towards satisfying a coverage criteria.

* (iii2) **Related Work:** 
 * Parallelizing software model checking: 
    * M. Dwyer, S. Elbaum, S. Person, and R. Purandare. _"Parallel randomized state-space search"_. In Proc of 29th Int’l.
Conference on Software Engineering, pages 3–12, 2007.
     * G. Holzmann and D. Bosnacki. _"The design of a multicore extension of the spin model checker"_. IEEE Transactions on
Software Engineering, 33(10):659–674, 2007.
     * G. Holzmann, R. Joshi, and A. Croce. _"Tackling large verification problems with the swarm tool"_. Proc. 15th Int’l.
SPIN Workshop, 5156:134–143, 2008.
     * U. Stern and D. Dill. Parallelizing the Mur\phi verifier. Formal Methods in System Design, 18(2):117–129, 2001.
 * Parallelizing symbolic execution:
    * L. Ciortea, C. Zamfir, S. Bucur, V. Chipounov, and G. Candea. _"Cloud9: A Software Testing Service"_.
    * A. King. _"Distributed parallel symbolic execution"_. Master’s thesis, Kansas State University, 2009.
 * Counterexample based test generation:
    * P. E. Ammann, P. E. Black, and W. Majurski. _"Using model checking to generate tests from specifications"_. In Proc. of
2nd IEEE Int’l. Conference on Formal Engineering Methods, pages 46–54. IEEE Computer Society, Nov. 1998. 
     * S. Rayadurgam and M. P. Heimdahl. _"Coverage based test-case generation using model checkers"_. In Proc. of the 8th
IEEE Int’l. Conference and Workshop on the Engineering of Computer Based Systems, pages 83–91. IEEE Computer Society, April 2001.
     * S. Khurshid, C. Pasareanu, and W. Visser. _"Generalized symbolic execution for model checking and testing"_. Proc. of
the 9th TACAS, pages 553–568, 2003.

* (iii3) **Checklists:** The paper is described along the following lines to demonstrate the effectiveness of the proposed technique -
 * _Description & Implementation_ - The authors describe and implement a technique for statically partitioning a symbolic execution tree and distributing the partitions across parallel instances.
 * _Framework Development_ - The authors develop a flexible, extensible framework for parallelizing Java Pathfinder, using a simple client-server model, with coordination and communication across parallel instances of JPF handled by an extension of JPF listeners.
 * _Evaluation_ - The authors evaluate their work in terms of the speedup when exploring a finite symbolic execution
tree (the time to completely explore a finite symbolic execution tree) and the performance of automatic test generation ( time to generate tests meeting the Modified Condition/Decision Coverage (MC/DC) structural coverage criterion).

* (iii4) **Future Work:**

<img src="https://cloud.githubusercontent.com/assets/7557398/10121569/64383824-64c0-11e5-9aa5-dad53a31a7a2.png" width = "420" height="320"><img src="https://cloud.githubusercontent.com/assets/7557398/10121566/642c239a-64c0-11e5-822d-b8338c8c573c.png" width = "420" height="320">

<img src="https://cloud.githubusercontent.com/assets/7557398/10121567/6436d38a-64c0-11e5-8cf0-cc505fb7fc53.png" width = "420" height="320"><img src="https://cloud.githubusercontent.com/assets/7557398/10121568/6436fe82-64c0-11e5-8cb0-f561c23a24c8.png" width = "420" height="320">
  
###(v) **Suggested Improvements:**
* (v1) Mention why specifically Mann Whitney U Test and Vargha Delaney effect size were used in statistical evaluation.
* (v2) Use of performance measures that take into account how difficult it will be to check the correctness of the outputs.
* (v3) Analysis of the results specific to each case study to more clearly delineate why the proposed approach is better.

###(vi) **Connection to other papers:**
The work done in this paper forms the basis for _"Combining Search-based and Constraint-based Testing"_, which uses whole suite test generation for GA implementation in a hybrid approach that integrates search based testing with constraint based testing.
