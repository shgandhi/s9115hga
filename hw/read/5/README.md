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

* (iii1) **Motivation:** 
* (iii2) **Hypotheses**
  * Global Search is more effective but less efficient
  * 

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


* (iii3) **Informative Visualizations:** The paper is described along the following lines to demonstrate the effectiveness of the proposed technique -
<img src="https://cloud.githubusercontent.com/assets/7557398/10125842/a9b509aa-6550-11e5-9541-347dc13b9923.jpg">
<img src="https://cloud.githubusercontent.com/assets/7557398/10125841/a7caf38e-6550-11e5-903a-8f9c9d1cb62b.jpg">

* (iii4) **New Results:**
   * For benchmark functions, it was observed that 
      * ES Solver was most effective, achieving 100% block coverage for 5 out of 6 functions. 
      * AVM failed to reach the Pex goal for the Rosenbrock function, and also fails in 3 out of 30 runs for the Beale function. 
      * Neither ES or AVM solver achieved full coverage of the Powell function.
      * It was found that the custom solvers can improve the coverage of Pex for floating point computations
      * For 3 out of 6 functions Pex was able to achieve 100% block coverage without using any heuristics on top of Z3.
   * For open source functions, it was observed that 
      * The coverage with the AVM solver enabled, was less than with the custom solvers disabled.
      * The ES solver only marginally increased the coverage compared to Pex’s default solvers (i.e. Z3 and randomsearch).
      * the custom solvers proposed in this paper should only be enabled if the code is known to produce many constraints over floating point variables. In such a case, sufficient resources, in terms of fitness evaluations as well as runtime, should be allocated for the solvers to be effective.
   * It was also observed how often constraints over floating point variables are a problem for DSE in practice. For Alglib (a numerical analysis and data processing library), over a third of its methods contain constraints over floating point numbers that could not be solved by either Z3 or a random search. For the QLNet (quantitative finance
operations library) on the other hand, this figure was found to be much smaller at around 3% of its methods.
  
###(v) **Suggested Improvements:**
* (v1) The experiments for benchmark functions could have been repeated for variable number of iterations to account for the inherent stochastic behavior of meta-heuristics used in custom solvers.
* (v2) The reason could have been mentioned for choosing those specific benchmark and open source functions, and whether the chosen functions were representative of the maximum possible input domain.
* (v3) Statistical analysis of the results could have been visually represented for open source libraries as well to give more insightful interpretations.

###(vi) **Connection to other papers:**
FloPSy combines SBST and DSE for a particular setting of floating point constraints while the authors for _"Combining Search-based and Constraint-based Testing"_, give a more general approach of combining these two automatic test generation approaches. FloPSy which is a search based extension to Microsoft's DSE tool PEX that relies on the native code to have constraints, and is specifically an extension for DSE. The work in _"Combining Search-based and Constraint-based Testing"_ works along these lines, but focusses on improving both SBST and DSE without any hard requirement for constraints in native code.


