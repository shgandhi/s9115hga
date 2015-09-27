##Summary

###(i) Reference: Matt Staats, University of Minnesota and Corina Pasareanu, Carnegie Mellon University/NASA Ames, ACM, 2010. [Parallel Symbolic Execution for Structural Test Generation](http://dl.acm.org/citation.cfm?id=1831708.1831732). 

###(ii) Keywords:
* (ii1) **Java PathFinder:** Java Pathfinder (JPF) is an open-source tool-set for verifying Java bytecodes. It includes an explicit-state model-checker (core-JPF) and several extensions, e.g. Symbolic PathFinder and ComplexCoverage.

* (ii2) **Simple Static Partitioning:** The method of parallelization that statically partitions and distributes execution by (1) generating a queue of constraints and (2) distributing these constraints (as part of a standard JPF configuration) to workers, which use the constraints to direct symbolic execution.

* (ii3) **Random depth first search:** Random depth first search (RDFS) performs depth first search while randomly selecting the order branches in the tree are explored. It has very low overhead and is amenable to parallel execution via different random seeds.

* (ii4) **Model Checking:** The model-checking algorithm is a decision procedure which in addition to the yes/no answer returns a trace of a faulty behaviour in case the checked property is not satisfied by the model.

###(iii) Artifacts:

* (iii1) **Motivation:**  Symbolic execution achieves high structural coverage for automatic test generation and the paths followed during symbolic execution form a symbolic execution tree, which represent all the possible executions through the
program. However, it's very difficult to explore all possible program execution as the symbolic execution tree can be infinitely large in size. This limits the application of symbolic execution as it is vulnerable to scalability issues. But motivated by the high availability of multi-core computers, and the parallelizable nature of symbolic execution, the authors proposed to mitigate this problem by parallelizing symbolic execution such that the essence of parallelization is maintained. This was proposed to be done by eliminating synchronization overhead by designing approaches that required minimum inter process communication.

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
   * Due to similarity between searching for states satisfying coverage obligations and searching for states violating assertions/properties, the authors propose evaluating the partitioning techniques in other contexts such as fault detection.
   * The authors suggest that combining static partitioning techniques (via control graphs) with dynamic partitioning could be very effective for parallelizing symbolic execution, and plan to work in that direction.
  
###(v) **Suggested Improvements:**
* (v1) Include an emperical comparison of using shallow execution bounds and longer bounds.
* (v2) Mention the reason for running parallel workers with parallel RDFS using specifically 64 random seeds and 1,000 samples.
* (v3) Statistical analysis of the results could have been done to give more insightful interpreations.

###(vi) **Connection to other papers:**
The case studies WBS (theWheel Brake System, a synchronous reactive component from the automotive domain), FGS and ASW (the Altitude Switch, a synchronous reactive component from the avionics domain) used for analysis in _"Combining Search-based and Constraint-based Testing"_, were translated to Java for analysis in this paper.
