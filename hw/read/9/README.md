##Summary

###(i) Reference: Gordon Fraser, Andrea Arcuri, IEEE TRANSACTIONS ON SOFTWARE ENGINEERING, 2013. [Whole Test Suite Generation](http://www.computer.org/csdl/trans/ts/2013/02/tts2013020276-abs.html). 

###(ii) Keywords:
* (ii1) **Search Based Software Engineering:** Search Based Software Engineering (SBSE) is the name given to a body of work in which Search Based Optimisation is applied to Software Engineering, it seeks to reformulate Software Engineering problems as ‘search problems’.

* (ii2) **Length of a Test Suite:** A test case is a sequence of statements t = of length l. The length of a test suite is defined as the sum of the lengths of its test cases.

* (ii3) **Branch Coverage:** It is a testing metric which considers a branch in a code (eg. if statements, loops) to be covered only if it is executed both ways, i.e. the branch must have been true at least once, and false atleast once during testing.

* (ii4) **Infeasible Goal:** Coverage goals are said to be infeasible if there exists no input that would cover them.

* (ii5) **Collateral Coverage:** When a test case generated for one goal implicitly also cover any number of further coverage goals, it is called collateral or serendipitous coverage.

###(iii) Artifacts:

* (iii1) **Motivation:**  

* (iii2) **Related Work:** 

* (iii3) **Informative Visualizations:** 

* (iii4) **New Results:**
 
###(v) **Suggested Improvements:**
* (v1) The experiments for benchmark functions could have been repeated for variable number of iterations to account for the inherent stochastic behavior of meta-heuristics used in custom solvers.
* (v2) The reason could have been mentioned for choosing those specific benchmark and open source functions, and whether the chosen functions were representative of the maximum possible input domain.
* (v3) Statistical analysis of the results could have been visually represented for open source libraries as well to give more insightful interpretations.

###(vi) **Connection to other papers:**
This paper extends the work done _"Evolutionary Generation of Whole Test Suites by Fraser and Arcuri"_ by -
* Using a much larger and more variegated case study 
* Verifying that the presence of infeasible branches has no negative impact on performance
* Providing theoretical analyses to shed more light on the properties of the proposed approach. 
* Demonstrate the effectiveness of EVOSUITE by applying it to 1,741 classes coming from open source libraries and an industrial case study


