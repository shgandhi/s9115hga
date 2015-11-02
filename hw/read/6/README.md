##Summary

###(i) Reference: Nikolai Tillmann and Jonathan de Halleux, Springer, 2008. [Pex–White Box Test Generation for .NET](http://dl.acm.org/citation.cfm?id=1792798). 

###(ii) Keywords:
* (ii1) **Parametrized Unit Test:** A method that takes parameters, performs a sequence of method calls that exercise the code-undertest, and asserts properties of the code’s expected behavior.

* (ii2) **Dynamic Symbolic Execution:** DSE which is a combination of symbolic and concrete execution uses concrete execution to drive the symbolic exploration of a program, the runtime values produced by symbolic execution are used to simplify path constraints to make them more feasible for constraint solving.

* (ii3) **The Testing Problem:** Given a sequential program (single threaded) P with statements S, compute a set of program
inputs I such that for all reachable statements s in S there exists an input i in I such that P(i) executes s.

* (ii4) **A constraint solver:** A program that computes solutions to logic formulas in a given logic

###(iii) Artifacts:

* (iii1) **Motivation:**  Dynamic Symbolic Execution and Search Based Software Testing are the most effective approaches for automatic generation of test cases. But both these approaches have their own complementary strength and weaknesses. While DSE is better suited to discover the structure of the input to the system under test, SBST provides a natural way to express coverage based test adequacy criteria as a multi–objective problem. The primary motivation was that -
  * While some work had been done to combine the two approaches, nothing had been done to mitigate the problem of tackling floating point computations in DSE, which originate from limitations of most constraint solvers. Since the constraint solvers approximate constraints over floating point numbers as constraints over rational numbers, the solutions valid for rational numbers are not always valid when mapped to floating point numbers because of limited precision of computers. 

Thus, the authors approached this problem by devising a framework that handled constraints over floating point variables and proposing a combination of DSE with SBST to improve code coverage in the presence of floating point computations.

* (iii2) **Related Work:** 
 * Inkumsah, K., Xie, T.: _"Evacon: A framework for integrating evolutionary and concolic testing for object-oriented programs"_. In: ASE 2007, pp. 425–428 (2007)
 * Tonella, P.: _"Evolutionary testing of classes"_. In: ISSTA 2004, pp. 119–128 (2004)
 * Sen, K., Agha, G.: _"CUTE and jCUTE: Concolic unit testing and explicit path model-checking tools"_. In: Ball, T., Jones, R.B. (eds.) CAV 2006. LNCS, vol. 4144, pp. 419–423. Springer, Heidelberg (2006)
 * Majumdar, R., Sen, K.: _"Hybrid concolic testing"_. In: ICSE 2007, pp. 416–426. IEEE Computer Society, Los Alamitos (2007)
 * Botella, B., Gotlieb, A., Michel, C.: _"Symbolic execution of floating-point computations"_. Softw. Test, Verif. Reliab 16(2), 97–121 (2006)


* (iii3) **Tutorial Materials:** Given below is the tutorial material provided by Microsoft Research for PEX.
  * ![Getting Started](http://research.microsoft.com/en-us/projects/pex/getstarted.pdf)

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


