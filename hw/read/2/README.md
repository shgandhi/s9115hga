##Summary

###(i) Reference: Gordon Fraser, Saarland University and Andrea Arcuri, Simula Research Laboratory, IEEE, 2011. [Evolutionary Generation of Whole Test Suites](http://ieeexplore.ieee.org/xpl/login.jsp?tp=&arnumber=6004309&url=http%3A%2F%2Fieeexplore.ieee.org%2Fxpls%2Fabs_all.jsp%3Farnumber%3D6004309). 

###(ii) Keywords:
* (ii1) **Length of Test Suite:** A test case is a sequence of statements _t = <s1,s2, . . . ,sl>_ of length l. The length of a test suite is defined as the sum of the lengths of its test cases.

* (ii2) **Collateral coverage:** When a test case targeting a particular coverage goal also satisfies further coverage goals by accident, it is called collateral or serendipitious coverage.

* (ii3) **Infeasible coverage:** Infeasibility in coverage goals means that there exists no test that would exercise those goals; this is an instance of the undecidable infeasible path problem

* (ii4) **Genetic Algorithm:** Genetic Algorithms (GAs) qualify as meta-heuristic search technique that attempt to imitate the mechanisms of natural adaptation in computer systems. A population of chromosomes is evolved using genetics-inspired operations, where each chromosome represents a possible problem solution.

###(iii) Artifacts:

* (iii1) **Motivation:**  While generating tests from the source code satisfying a certain coverage criteria, the fundamental assumptions are that all coverage goals are equally important, equally difficult to reach and independent of each other. This flawed assumption motivated the authors to challenge the general approach that worked along devising a test case that exercises a particular coverage goal at a time, ignoring the possibility of a coverage goal being infeasible, or difficult to satisfy or causing collateral coverage. These problems cannot be efficiently predicted, which led the authors to propose an approach to mitigate them. Instead of tackling individual coverage goals with distinct test cases, the authors suggested an approach to optimize the entire test suite towards satisfying a coverage criteria.

* (iii2) **Related Work:** 
 * A. Arcuri and X. Yao, _“Search based software testing of object-oriented containers,”_ Information Sciences, vol. 178, no. 15, pp. 3075–3095, 2008.
 * L. Baresi, P. L. Lanzi, and M. Miraz, _“Testful: an evolutionary test approach for Java,”_ in ICST’10: Proceedings of the 3rd International Conference on Software Testing, Verification and Validation. IEEE Computer Society, 2010, pp. 185–194.
 * B. Baudry, F. Fleurey, J.-M. J´ez´equel, and Y. Le Traon, _“Automatic test cases optimization: a bacteriologic algorithm,”_ IEEE Software, vol. 22, no. 2, pp. 76–82, Mar. 2005.
 * C. Pacheco and M. D. Ernst, _“Randoop: feedback-directed random testing for Java,”_ in OOPSLA’07: Companion to the 22nd ACM SIGPLAN Conference on Object-oriented Programming Systems and Application. ACM, 2007, pp. 815–816

* (iii3) **Statistical Tests:** 
 * The proposed approach "EVOSUITE" and search based testing are based on randomized algorithms, to properly analyze the algorithms the authors followed the guidelines in _A. Arcuri and L. Briand, “A practical guide for using statistical tests to assess randomized algorithms in software engineering,” IEEE ICSE 2011_. The authors ran EVOSUITE against the single branch strategy for each of the 727 public classes, to compare their achieved coverage. Each experiment comparison was repeated 100 times with different seeds for the random number generator.
 *  *Mann Whitney U Test*- It is a non-parametric statistical hypothesis test, i.e. it allows the comparison of two samples with unknown distributions. It was used to assess whether the effectiveness of EVOSUITE and single branch based approach were statistically different. 
 *  *Vargha-Delaney Aˆ12 statistic*- To measure the magnitude of the difference in a standardized way i.e. using the _effect size_; the Aˆ12 statistic was used. In the context of this experiment, the Aˆ12 is an estimation of the probability that, better coverage is obtained upon running EVOSUITE, than running the single branch strategy. When two randomized algorithms were equivalent, then Aˆ12 = 0.5. A high value Aˆ12 = 1 meant that, in all of the 100 runs of EVOSUITE, higher coverage values were obtained than the ones obtained in all of the 100 runs of the single branch strategy.
 *  Boxplots were used to visualize the comparison between the two approaches for all the six case studies by using as a measure -
   * Average branch coverage
    * Aˆ12 for coverage
    * Average length values when Aˆ12 = 0.5
    * Aˆ12 for length
   
* (iii4) **Informative Visualizations:**

<img src="https://cloud.githubusercontent.com/assets/7557398/10121569/64383824-64c0-11e5-9aa5-dad53a31a7a2.png" width = "420" height="320"><img src="https://cloud.githubusercontent.com/assets/7557398/10121566/642c239a-64c0-11e5-822d-b8338c8c573c.png" width = "420" height="320">

<img src="https://cloud.githubusercontent.com/assets/7557398/10121567/6436d38a-64c0-11e5-8cf0-cc505fb7fc53.png" width = "420" height="320"><img src="https://cloud.githubusercontent.com/assets/7557398/10121568/6436fe82-64c0-11e5-8cb0-f561c23a24c8.png" width = "420" height="320">
  
###(v) **Suggested Improvements:**
* (v1) The reason for specifically using Mann Whitney U Test and Vargha Delaney effect size for statistical evaluation could have been mentioned.
* (v2) The performance measures that take into account the difficulty to check the correctness of the outputs could have been used.
* (v3) There could have been a mention of why specific case studies were chosen, and whether those selected were infact representative of all the possible variation of the input classes.

###(vi) **Connection to other papers:**
The work done in this paper forms the basis for _"Combining Search-based and Constraint-based Testing"_, which uses whole suite test generation for GA implementation in a hybrid approach that integrates search based testing with constraint based testing.
