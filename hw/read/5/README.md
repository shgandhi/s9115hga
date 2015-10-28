##Summary

###(i) Reference: Mark Harman and Phil McMinn, IEEE TRANSACTIONS ON SOFTWARE ENGINEERING, VOL. 36, NO. 2, MARCH/APRIL 2010. [A Theoretical and Empirical Study of Search-Based Testing: Local, Global, and Hybrid Search](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=5342440&tag=1). 

###(ii) Keywords:
* (ii1) **Search Based Testing:** The approach of applying search based optimization technique on the problem of software test data generation.

* (ii2) **Evolutionary Testing:** It is a sub-field of search based testing which uses evolutionary algorithms (most commonly implemented as genetic algorithms) to guide the search.

* (ii3) **Schema Theory:** According to the Schema Theory those schemata with a better than average fitness will
receive proportionally more fitness evaluations as the computation of the Genetic Algorithm progresses. ( Achema is a template chromosome that stands for a whole set of individual chromosomes, each of which share some common fixed values)

* (ii4) **Royal Road Theory:** Royal road theory predicts that evolutionary testing that holds the *royal road property, performs well because of the presence of crossover operation such that fitter schemata are given more fitness evaluations as compared to lesser fit schemata. (The royal road property is obeyed if schemas of each order are composable
to produce schemas of the next higher order)

* (ii5) **Memetic Algorithms:** Memetic Algorithms are Evolutionary Algorithms which employ a stage of local search to improve each individual at the end of each generation.

###(iii) Artifacts:

* (iii1) **Motivation:** 
* (iii2) **Hypotheses**
  * Global Search is more effective but less efficient
  * 

* (iii2) **Related Work:** 
 * Inkumsah, K., Xie, T.: _"Evacon: A framework for integrating evolutionary and concolic testing for object-oriented programs"_. In: ASE 2007, pp. 425–428 (2007)
 * Tonella, P.: _"Evolutionary testing of classes"_. In: ISSTA 2004, pp. 119–128 (2004)
 * Sen, K., Agha, G.: _"CUTE and jCUTE: Concolic unit testing and explicit path model-checking tools"_. In: Ball, T., Jones, R.B. (eds.) CAV 2006. LNCS, vol. 4144, pp. 419–423. Springer, Heidelberg (2006)
 * Majumdar, R., Sen, K.: _"Hybrid concolic testing"_. In: ICSE 2007, pp. 416–426. IEEE Computer Society, Los Alamitos (2007)
 * Botella, B., Gotlieb, A., Michel, C.: _"Symbolic execution of floating-point computations"_. Softw. Test, Verif. Reliab 16(2), 97–121 (2006)


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


