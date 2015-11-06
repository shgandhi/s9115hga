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

* (iii3) **Sampling Procedures:** To select an unbiased sample of Java software, the authors decided to go with SourceForge open source development platform, for it was a dominant site of the type having more than 300,000 registered projects at the time of their experiment. Since there were 48,109 Java programming projects at the site at the time, it wasn't possible to apply EVOSUITE (a tool which automatically generates test suites for Java classes, targeting branch coverage - Read Review 2 for details) to all the projects in reasonable time, hence random sampling of data set was performed. For each chosen project the most recent sources from the corresponding source repository were downloaded to build the program. the issues faced here were - empty projects, misclassified projects, old projects relying on unavailable Java APIs. For projects that the authors weren't able to compile, they downloaded the binaries as EVOSUITE did'nt require source code for test generation.The authors had to consider a total of 321 projects until they had a set of 100 projects in binary format, which the authors called [SF100 corpus of classes](http://www.evosuite.org/subjects/sf100/)

* (iii4) **Informative Visualizations:**

<figure><img src="https://cloud.githubusercontent.com/assets/7557398/10985536/f1f9b054-83ef-11e5-9379-42615dcb7b89.jpg" width = "420" height="320"><figcaption>For each 10% code coverage interval, the proportion of
projects that have an average coverage (averaged out of 10 runs on all their
classes) within that interval. Labels show the upper limit (inclusive). For
example, the group 40% represent all the projects with average coverage
greater than 30% and lower or equal to 40%.</figcaption></figure><figure><img src="https://cloud.githubusercontent.com/assets/7557398/10985537/f39a31f4-83ef-11e5-86b0-054ff56cd869.jpg" width = "420" height="320"></figure>

<img src="https://cloud.githubusercontent.com/assets/7557398/10985538/f5389f78-83ef-11e5-8957-e2e6aab8fcef.jpg" width = "420" height="320"><img src="https://cloud.githubusercontent.com/assets/7557398/10985539/f8abf768-83ef-11e5-9cce-0affdf25e85e.jpg" width = "420" height="320">

  
###(v) **Suggested Improvements:**
* (v1) The experiments for benchmark functions could have been repeated for variable number of iterations to account for the inherent stochastic behavior of meta-heuristics used in custom solvers.
* (v2) The reason could have been mentioned for choosing those specific benchmark and open source functions, and whether the chosen functions were representative of the maximum possible input domain.
* (v3) Statistical analysis of the results could have been visually represented for open source libraries as well to give more insightful interpretations.

###(vi) **Connection to other papers:**
FloPSy combines SBST and DSE for a particular setting of floating point constraints while the authors for _"Combining Search-based and Constraint-based Testing"_, give a more general approach of combining these two automatic test generation approaches. FloPSy which is a search based extension to Microsoft's DSE tool PEX that relies on the native code to have constraints, and is specifically an extension for DSE. The work in _"Combining Search-based and Constraint-based Testing"_ works along these lines, but focusses on improving both SBST and DSE without any hard requirement for constraints in native code.


