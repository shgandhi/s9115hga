##Summary

###(i) Reference: Florian Gross, Gordon Fraser, Andreas Zeller, ACM, 2012. [Search-Based System Testing: High Coverage, No False Alarms](http://dl.acm.org/citation.cfm?id=2336762). 

###(ii) Keywords:
* (ii1) **Test Case Generation:** .

* (ii2) **System Testing:** .

* (ii3) **GUI Testing:** .

* (ii4) **Test Coverage:** .

###(iii) Artifacts:

* (iii1) **Motivation:**  Dynamic Symbolic Execution and Search Based Software Testing are the most effective approaches for automatic generation of test cases. But both these approaches have their own complementary strength and weaknesses. While DSE is better suited to discover the structure of the input to the system under test, SBST provides a natural way to express coverage based test adequacy criteria as a multi–objective problem. The primary motivation was that -
  * While some work had been done to combine the two approaches, nothing had been done to mitigate the problem of tackling floating point computations in DSE, which originate from limitations of most constraint solvers. Since the constraint solvers approximate constraints over floating point numbers as constraints over rational numbers, the solutions valid for rational numbers are not always valid when mapped to floating point numbers because of limited precision of computers. 

Thus, the authors approached this problem by devising a framework that handled constraints over floating point variables and proposing a combination of DSE with SBST to improve code coverage in the presence of floating point computations.

* (iii2) **Related Work:** 


* (iii3) **Informative Visualizations:** The paper is described along the following lines to demonstrate the effectiveness of the proposed technique -
<img src="https://cloud.githubusercontent.com/assets/7557398/10125842/a9b509aa-6550-11e5-9541-347dc13b9923.jpg">
<img src="https://cloud.githubusercontent.com/assets/7557398/10125841/a7caf38e-6550-11e5-903a-8f9c9d1cb62b.jpg">

* (iii4) **New Results:**
  .
  
###(v) **Suggested Improvements:**
* (v1) The experiments for benchmark functions could have been repeated for variable number of iterations to account for the inherent stochastic behavior of meta-heuristics used in custom solvers.
* (v2) The reason could have been mentioned for choosing those specific benchmark and open source functions, and whether the chosen functions were representative of the maximum possible input domain.
* (v3) Statistical analysis of the results could have been visually represented for open source libraries as well to give more insightful interpretations.

###(vi) **Connection to other papers:**
FloPSy combines SBST and DSE for a particular setting of floating point constraints while the authors for _"Combining Search-based and Constraint-based Testing"_, give a more general approach of combining these two automatic test generation approaches. FloPSy which is a search based extension to Microsoft's DSE tool PEX that relies on the native code to have constraints, and is specifically an extension for DSE. The work in _"Combining Search-based and Constraint-based Testing"_ works along these lines, but focusses on improving both SBST and DSE without any hard requirement for constraints in native code.


