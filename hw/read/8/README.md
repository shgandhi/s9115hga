##Summary

###(i) Reference: Gordon Fraser, Andrea Arcuri, IEEE, 2012. [Sound Empirical Evidence in Software Testing](http://dl.acm.org/citation.cfm?id=2337245). 

###(ii) Keywords:
* (ii1) **Test Case Generation:** .

* (ii2) **Unit Testing:** .

* (ii3) **Class Corpus:** A collection of classes.

* (ii4) **Security Exception:** .

###(iii) Artifacts:

* (iii1) **Motivation:** Over the years, a lot of complex techniques for automated testing of software have been proposed, one problem faced when proposing these techniques is the difficulty to mathematically prove their effectiveness, this is where empirical analysis comes into picture. One of the biggest challenge in empirical testing is the choice of the case study. Currently this choice is not made in a systematic way, i.e., researchers choose software artifacts without providing any specific and unbiased motivation. Even a manual choice of software artifacts when choosing case studies for test data generation for open source software can introduce bias in the results. The absence of of any empirical study in the literature addressing threats to external validity focussing on possible biases due to case study selection motivated the authors to conduct an empirical study with statistical sound selection case studies for open source software.

* (iii2) **Study Instruments:** The authors conducted a survey of the literature on test generation for object-oriented software to get a better picture of the current practice in evaluations in software engineering research. The authors explicitly listed the number the number of container classes from among all the classes considered as container classes represent a particular type of classes that avoids many problems such as environment interaction and can result in high coverage by even simple random testing. Out of the 44 evaluations considered in the literature survey, 17 papers were found to exclusively focus on container classes, 29 selected their case study programs from open source programs, while only six evaluations included industrial code, 17 evaluations used artificially created examples, either by generating them or by reusing them from the literature. Also, it was found that not a single paper out of those considered justifies why those particular set of classes was selected, and how this selection was done.

* (iii3) **Sampling Procedures:** 

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


