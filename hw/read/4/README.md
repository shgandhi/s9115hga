##Summary

###(i) Reference: Kiran Lakhotia, Mark Harman, University College London and Nikolai Tillmann, Jonathan de Halleux, Microsoft Research, Springer, 2010. [FloPSy - Search-Based Floating Point Constraint Solving for Symbolic Execution](http://link.springer.com.prox.lib.ncsu.edu/chapter/10.1007/978-3-642-16573-3_11). 

###(ii) Keywords:
* (ii1) **Search Based Software Testing:** In SBST, an optimization algorithm is guided by an objective function which is  defined in terms of a test adequacy criterion to generate test data.

* (ii2) **Dynamic Symbolic Execution:** DSE which is a combination of symbolic and concrete execution uses concrete execution to drive the symbolic exploration of a program, the runtime values produced by symbolic execution are used to simplify path constraints to make them more feasible for constraint solving.

* (ii3) **Alternating Variable Method:** AVM is a form of hill climbing. It works by continuously changing an input parameter to a function in isolation. It first constructs a vector of input variables, then explores the "neighbourhood" of each input variable in this vector in turn. If changes in the values of the input variable do not result in an increased fitness, the search considers the next input variable, and so on - recommencing from the first input variable if necessary - until no further improvements can be made or test data has been found.

* (ii4) **Evolution Strategies:** ES falls in the family of evolutionary algorithms. In ES an individual has two components: an object vector which contains the inputs to the function under test and a strategy parameter vector. The strategy parameters control the strength of the mutations of the object vector by evolving themselves, so that the ES can self–adapt to the underlying search landscape.

###(iii) Artifacts:

* (iii1) **Motivation:**  Symbolic execution achieves high structural coverage for automatic test generation and the paths followed during symbolic execution form a symbolic execution tree, which represent all the possible executions through the
program. However, it's very difficult to explore all possible program execution as the symbolic execution tree can be infinitely large in size. This limits the application of symbolic execution as it is vulnerable to scalability issues. But motivated by the high availability of multi-core computers, and the parallelizable nature of symbolic execution, the authors proposed to mitigate this problem by parallelizing symbolic execution such that the essence of parallelization is maintained. This was proposed to be done by eliminating synchronization overhead by designing approaches that required minimum inter process communication.

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
   * Due to similarity between searching for states satisfying coverage obligations and searching for states violating assertions/properties, the authors propose evaluating the partitioning techniques in other contexts such as fault detection.
   * The authors suggest that combining static partitioning techniques (via control graphs) with dynamic partitioning could be very effective for parallelizing symbolic execution, and plan to work in that direction.
  
###(v) **Suggested Improvements:**
* (v1) An empirical comparison of using shallow execution bounds and longer bounds could have been included to show more representative results.
* (v2) The reason for running parallel workers with parallel RDFS using specifically 64 random seeds and 1,000 samples could have been mentioned.
* (v3) Statistical analysis of the results could have been done to give more insightful interpretations.

###(vi) **Connection to other papers:**
The case studies WBS (theWheel Brake System, a synchronous reactive component from the automotive domain), FGS and ASW (the Altitude Switch, a synchronous reactive component from the avionics domain) used for analysis in _"Combining Search-based and Constraint-based Testing"_, were translated to Java for analysis in this paper.

