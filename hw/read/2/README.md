##Summary

###(i) Reference: Kobi Inkumsah and Tao Xie, North Carolina State University, ASE-2008. [Improving Structural Testing of Object-Oriented Programs via Integrating Evolutionary Testing and Symbolic Execution](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=4639333). 

###(ii) Keywords:
* (ii1) **Search Based Testing:** It defines the testing problem as a search problem and applies efficient algorithms to find inputs that can serve as tests.

* (ii2) **Symbolic Execution:** The key idea here is to generalize testing by using *unknown* symbolic variables in evaluation. A symbolic executor collects all path conditions (eg. if clauses) and operations on symbolic variables along the path selected by a tester. Then these conditions are fed to a constraint solver to derive all inputs that make the program follow this path, as done in *classic constraint based testing*

* (ii3) **Method Sequence Skeleton:** It is a method sequence whose methods' primitive arguments are not specified.

* (ii4) **Branch Coverage:** It is a testing metric which considers a branch in a code (eg. if statements, loops) to be covered only if it is executed both ways, i.e. the branch must have been true at least once, and false atleast once during testing.

###(iii) Artifacts:

* (iii1) **Motivation:** To increase the confidence in a unit test of a code under test, it is imperative that the unit has good structural coverage (eg. branch coverage). Despite of many test generation tools having been built over time to ensure good structural coverage, there are still two main challenges when it comes to achieving good branch coverage. First is the requirement of an in-depth knowledge of program structure and semantics to generate tests to cover complex logics in some branches. Second is generating special method sequences out of the huge search space of method sequences, to cover branches that lead receiver objects/ non primitive arguments (in Object Oriented Programming) can reach a desirable state only via special method sequences. Though these two challenges have been met by symbolic execution and evolutionary testing, respectively, no work had been done to combine the two approaches and meet both the challenges simulataneously, this led the authors to propose a framework *Evacon*. 

* (iii2) **Checklist:** The authors followed the following series of steps in the paper.
 * Devise the framework for the integration of two existing testing techniques to address the problems in structural testing of object oriented programs. The authors describe their framework with the following 4 components -
    * *Evolutionary testing:* Do population initialization, fitness calculation, chromosome selection, recombination and mutation.
    * *Symbolic Execution:* Using jCUTE, do in loop - concrete execution and constraint collection, followed by constraint solving and input generation.
    * *Argument Transformation:* Transform method arguments of method sequences into symbolic arguments.
    * *Chromosome Construction:* Constructs non random chromosomes out of method sequences generated using symbolic execution for evolutionary testing.
 * Show the empirical comparison of the integration with the state of the art respresentative testing tools for test generation techniques such as search-based test generation using genetic algorithms, symbolic execution and random testing.
 * Give a detailed comparison of strengths and weaknesses of different testing tools in terms of achieving high structural coverage.

* (iii3) **Patterns:** The authors carried out comprehensive analysis of the test generation tools that they used for comparison with their Evacon framework. This directs the prospective user to both the (dis)advantages of these tools. The following can be reused - 
  |Test generation tool | Used for | Advantages | Disadvantages |
  |---------------------|----------|------------|---------------|
  |Randoop              | random testing|
* (iii4) **Related Work:**
  * *Combination of existing evolutionary tool with DSE tool:* K. Inkumsah and T. Xie, “Improving structural testing of object-oriented programs via integrating evolutionary testing and symbolic execution,” in Proceedings of the 2008 23rd IEEE/ACM International Conference on Automated Software Engineering (ASE’08).
  * *DSE tool - PEX Extension:* K. Lakhotia, N. Tillmann, M. Harman, and J. de Halleux, “FloPSy - search-based floating point constraint solving for symbolic execution,” in 22nd IFIP International Conference on Testing Software and Systems, ser. Lecture Notes in Computer Science. Springer Berlin / Heidelberg, 2010.
  * *DSE and random search combination:* R. Majumdar and K. Sen, “Hybrid concolic testing,” in Proceedings of the 29th International Conference on Software Engineering (ICSE’07).

###(v) Suggested Improvements:
* (v1) Metrics other than branch coverage could have been used to indicate more comprehensive performance comparison.
* (v2) An equivalent mix of linear and non linear constraints could have been chosen for the benchmark case study examples. The paper used 15 linear and 5 non-linear/floating arithmetic cases.
* (v3) The table used for comparison could have been replaced by a more insightful visualization.

