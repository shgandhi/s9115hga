##Summary

###(i) Reference: Gordon Fraser, Andrea Arcuri, IEEE TRANSACTIONS ON SOFTWARE ENGINEERING, 2013. [Whole Test Suite Generation](http://www.computer.org/csdl/trans/ts/2013/02/tts2013020276-abs.html). 

###(ii) Keywords:
* (ii1) **Search Based Software Engineering:** Search Based Software Engineering (SBSE) is the name given to a body of work in which Search Based Optimisation is applied to Software Engineering, it seeks to reformulate Software Engineering problems as ‘search problems’.

* (ii2) **Length of a Test Suite:** A test case is a sequence of statements t = of length l. The length of a test suite is defined as the sum of the lengths of its test cases.

* (ii3) **Branch Coverage:** It is a testing metric which considers a branch in a code (eg. if statements, loops) to be covered only if it is executed both ways, i.e. the branch must have been true at least once, and false atleast once during testing.

* (ii4) **Infeasible Goal:** Coverage goals are said to be infeasible if there exists no input that would cover them.

* (ii5) **Collateral Coverage:** When a test case generated for one goal implicitly also cover any number of further coverage goals, it is called collateral or serendipitous coverage.

###(iii) Artifacts:

* (iii1) **Motivation:** The conventional approach in the literature of generating a test case for each coverage goal and then to combine them in a single test suite, poses a lot of problems, namely - collateral coverage, varying difficulty levels for coverage from one target to another, and infeasibility of coverage goals. Furthermore, this leads to the question of properly allocating testing budget (e.g., the maximum total time allowed for testing by the user) used for each target, and redistributing such budget to other uncovered targets when the current target is covered before its budget is fully consumed. This motivated the authors to evaluate the approach that improves upon the current approach of targeting one goal at a time.

* (iii2) **Tutorials:** Extensive documentation has been made available for working with EVOSUITE at http://www.evosuite.org/documentation/

* (iii3) **Future Work:**
  * Combinination of search-based test generation with dynamic symbolic execution, and search optimizations such as testability transformation or local search to further improve the achieved coverage.
  * Integration of enhancements in the literature of search algorithms and their evaluation in EVOSUITE, as, for example, island models and adaptive parameter control.
  * Investigation of ways to support the developer by automatically producing effective assertions for mitigating the _oracle problem_ and, making the produced test cases more readable for ease of understanding.

* (iii4) **New Results:**
  * Strong statistical evidence show that the EVOSUITE approach yields significantly better results (i.e., either higher coverage or, if the same coverage, then smaller test suites) compared to the traditional approach of targeting each testing goal independently.
  * In some cases, EVOSUITE achieved up to 188 times higher coverage on average, and test suites that were 62 percent
smaller while maintaining the same structural coverage.
  * Running EVOSUITE with a constrained budget (1 million statement executions during the search, up to a
maximum 10 minutes timeout) resulted in 83 percent of coverage on average on the case study under consideration.
 
###(v) **Suggested Improvements:**
* (v1) The performance EVOSUITE could have been compared with other tools in literature, to get a better ranking of the tool and the approach of _whole test suite generation_ as compared to the existing tools.

###(vi) **Connection to other papers:**
This paper extends the work done _"Evolutionary Generation of Whole Test Suites by Fraser and Arcuri"_ by -
* Using a much larger and more variegated case study 
* Verifying that the presence of infeasible branches has no negative impact on performance
* Providing theoretical analyses to shed more light on the properties of the proposed approach. 
* Demonstrate the effectiveness of EVOSUITE by applying it to 1,741 classes coming from open source libraries and an industrial case study


