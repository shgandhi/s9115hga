##Summary

###(i) Reference: Mark Harman and Phil McMinn, IEEE TRANSACTIONS ON SOFTWARE ENGINEERING, VOL. 36, NO. 2, MARCH/APRIL 2010. [A Theoretical and Empirical Study of Search-Based Testing: Local, Global, and Hybrid Search](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=5342440&tag=1). 

###(ii) Keywords:
* (ii1) **Search Based Testing:** The approach of applying search based optimization technique on the problem of software test data generation.

* (ii2) **Evolutionary Testing:** It is a sub-field of search based testing which uses evolutionary algorithms (most commonly implemented as genetic algorithms) to guide the search.

* (ii3) **Schema Theory:** According to the Schema Theory those schemata with a better than average fitness will
receive proportionally more fitness evaluations as the computation of the Genetic Algorithm progresses. ( Achema is a template chromosome that stands for a whole set of individual chromosomes, each of which share some common fixed values)

* (ii4) **Royal Road Theory:** Royal road theory predicts that evolutionary testing that holds the *royal road property, performs well because of the presence of crossover operation such that fitter schemata are given more fitness evaluations as compared to lesser fit schemata. (The *royal road property is obeyed if schemas of each order are composable
to produce schemas of the next higher order)

* (ii5) **Memetic Algorithms:** Memetic Algorithms are Evolutionary Algorithms which employ a stage of local search to improve each individual at the end of each generation.

###(iii) Artifacts:

* (iii1) **Motivation:** Search based testing having got the kind of attention it had, the authors realized that there were some very fundamental questions still unanswered. These questions (below) coupled with the lack of strong empirical results that would use real world programs with large and complex search spaces, motivated the authors to pursue this study.
  * Which types of search (global and local)  were effective for which type of test data generation scenario?
  * Does Evolutionary Testing perform well on the Royal Road landscape? How does it compare to a hill climbing algorithm?
  * How does Evolutionary Testing perform on Royal Road functions when the effects of the crossover operator are removed?
  * How Evolutionary Testing performs relative to Hill Climbing in the the absence of Royal Roads, and how badly its performance is be affected in a non-Royal Road landscape?
  * Do hybrid memetic algorithms cover all the branches covered by Evolutionary Tesing and Hill Climbing?
  * Is the performance of the Memetic Algorithm similar with Royal Road branches as for Evolutionary Testing?
  * Do memetic algorithms improve on Evolutionary Testing on non-Royal Road branches, offering similar levels of efficiency on these branches as with Hill Climbing?
 
* (iii2) **Checklist:** 
  * Predict the suitability of Evolutionary Testing for structural test data generation problems using Royal Road and Schema Theory for Evolutionary Testing.
  * Empirically validate that Evolutionary Testing performs well for Royal Road functions and this is due to the presence of the crossover operator.
  * Empirically assess the performance of Evolutionary Testing compared to Hill Climbing and Random Testing.
  * Empirically assess Hybrid Memetic Algorithm which incorporates Hill Climbing into Evolutionary Testing.

* (iii2) **Related Work:** 
 * W. Miller and D. Spooner, _“Automatic Generation of Floating-Point Test Data,”_ IEEE Trans. Software Eng., vol. 2, no. 3,
pp. 223-226, Sept. 1976.
 * B. Korel, _“Automated Software Test Data Generation,”_ IEEE Trans. Software Eng., vol. 16, no. 8, pp. 870-879, Aug. 1990.
 * S. Xanthakis, C. Ellis, C. Skourlas, A.L. Gall, S. Katsikas, and K.Karapoulios, _“Application of Genetic Algorithms to Software Testing (Application Des Algorithms Ge´ne´tiques Au Test Des Logiciels),”_ Proc. Fifth Int’l Conf. Software Eng. and Its Applications, pp. 625-636, 1992.
 * H.-C. Wang and B. Jeng, _“Structural Testing Using Memetic Algorithm,”_ Proc. Second Taiwan Conf. Software Eng., 2006.
 * P. McMinn, _“Search-Based Software Test Data Generation: A Survey,”_ Software Testing, Verification and Reliability, vol. 14, no. 2, pp. 105-156, 2004.
 * N. Mansour and M. Salame, _“Data Generation for Path Testing,”_ Software Quality J., vol. 12, no. 2, pp. 121-134, 2004.
 * M. Xiao, M. El-Attar, M. Reformat, and J. Miller, _“Empirical Evaluation of Optimization Algorithms When Used in Goal- Oriented Automated Test Data Generation Techniques,”_ Empirical Software Eng., vol. 12, no. 2, pp. 183-239, 2007.
 * M. Harman and P. McMinn, _“A Theoretical & Empirical Analysis of Evolutionary Testing and Hill Climbing for Structural Test Data Generation,”_ Proc. Int’l Symp. Software Testing and Analysis, pp. 73-83, 2007.
 * M. Harman, Y. Hassoun, K. Lakhotia, P. McMinn, and J. Wegener, _“The Impact of Input Domain Reduction on Search-Based Test Data Generation,”_ Proc. ACM SIGSOFT Symp. Foundations of Software Eng., pp. 155-164, 2007.


* (iii3) **Sampling Procedures:** The authors used nine different programs for their empirical study, of which 38 functions containg 760 branches were studied. The factors that influenced their decision of choosing the projects they studied were -
  * Input Domain Size: The search space sizes for the programs ranged from 10^5 to 10^524. 
  
###(v) **Suggested Improvements:**
* (v1) The experiments for benchmark functions could have been repeated for variable number of iterations to account for the inherent stochastic behavior of meta-heuristics used in custom solvers.
* (v2) The reason could have been mentioned for choosing those specific benchmark and open source functions, and whether the chosen functions were representative of the maximum possible input domain.
* (v3) Statistical analysis of the results could have been visually represented for open source libraries as well to give more insightful interpretations.

###(vi) **Connection to other papers:**
FloPSy combines SBST and DSE for a particular setting of floating point constraints while the authors for _"Combining Search-based and Constraint-based Testing"_, give a more general approach of combining these two automatic test generation approaches. FloPSy which is a search based extension to Microsoft's DSE tool PEX that relies on the native code to have constraints, and is specifically an extension for DSE. The work in _"Combining Search-based and Constraint-based Testing"_ works along these lines, but focusses on improving both SBST and DSE without any hard requirement for constraints in native code.


