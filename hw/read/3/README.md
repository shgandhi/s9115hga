##Summary

###(i) Reference: Gordon Fraser, Saarland University and Andrea Arcuri, Simula Research Laboratory, Quality Software (QSIC), 2011 11th International Conference on. IEEE, 2011. [Evolutionary Generation of Whole Test Suites](http://ieeexplore.ieee.org/xpl/login.jsp?tp=&arnumber=6004309&url=http%3A%2F%2Fieeexplore.ieee.org%2Fxpls%2Fabs_all.jsp%3Farnumber%3D6004309). 

###(ii) Keywords:
* (ii1) **Search based testing:** It tries to improve the effectiveness and efficiency of testing process by transforming testing objectives into search problem, and applying evolutionary computation in order to solve them.

* (ii2) **Length coverage:** The key idea here is to generalize testing by using *unknown* symbolic variables in evaluation. A symbolic executor collects all path conditions (eg. if clauses) and operations on symbolic variables along the path selected by a tester. Then these conditions are fed to a constraint solver to derive all inputs that make the program follow this path, as done in *classic constraint based testing*

* (ii3) **Branch coverage:** It is a method sequence whose methods' primitive arguments are not specified.

* (ii4) **Genetic Algorithm:** It is a testing metric based on the structure of the program, intended to find defects rather than exploring the behaviour of the system. It can be focussed on either exploring the control aspect of the code, or explore the definition/use relationship between data elements.

###(iii) Artifacts:

* (iii1) **Motivation:**  While generating tests from the source code satisfying a certain coverage criteria, the fundamental assumptions are that all coverage goals are equally important, equally difficult to reach and independent of each other. The general approach of devising a test case that exercises a particular coverage goal at a time, ignores the possibility of a coverage goal being infeasible, or difficult to satisfy or causing collateral coverage. These problems cannot be efficiently predicted, hence the authors proposed an approach to mitigate them. Instead of tackling individual coverage goals with distinct test cases, the authors suggested an approach to optimize the entire test suite towards satisfying a coverage criteria.

* (iii2) **Related Work:** 
 * A. Arcuri and X. Yao, “Search based software testing of object-oriented containers,” Information Sciences, vol. 178, no. 15, pp. 3075–3095, 2008.
 * L. Baresi, P. L. Lanzi, and M. Miraz, “Testful: an evolutionary test approach for Java,” in ICST’10: Proceedings of the 3rd International Conference on Software Testing, Verification and Validation. IEEE Computer Society, 2010, pp. 185–194.
 * B. Baudry, F. Fleurey, J.-M. J´ez´equel, and Y. Le Traon, “Automatic test cases optimization: a bacteriologic algorithm,” IEEE Software, vol. 22, no. 2, pp. 76–82, Mar. 2005.
 * C. Pacheco and M. D. Ernst, “Randoop: feedback-directed random testing for Java,” in OOPSLA’07: Companion to the 22nd ACM SIGPLAN Conference on Object-oriented Programming Systems and Application. ACM, 2007, pp. 815–816

* (iii3) **Patterns:** 
 * The authors clearly delineated the research questions investigated in the paper, which can be used as benchmark questions for analyzing any test generation tool or framework -
    * __Utility:__ How does the proposed tool fare against representative test generation tools.
    * __Demonstrating the need of the solution:__ The proposed framework specifically targets branches that required longer method sequences, the authors demonstrated that certain type of branches needed longer method sequences for optimal branch coverage.
    * __Identifying other solutions based on uniqueness of the problem solved:__ The authors identified other tools for comparison based on those tools' unique coverage of some branches which couldn't be covered by other tools. This was the basis of shortlisting tools required for achieving optimal branch coverage.
 * The authors carried out comprehensive analysis of the test generation tools that they used for comparison with their propsed Evacon framework. This directs the prospective user to both the (dis)advantages of these tools. 
 * The average branch coverage of the proposed frameworks were found to be lower than the aggregated average of all the other 4 tools combined. This suggested that for some classes, using multiple tools in combination may be more beneficial than using a single tool to achieve optimal coverage.
 * Use of __Branch ranking metric__: Instead of widely used percentages of branch coverage, branch ranking metric is more useful when selecting multiple tools to use in combination among the tools under comparison. It also,
    * Helps in selecting appropriate tools or their combination for *residual* branch coverage,
    * Compares relative strength of each tool in a set of tools in terms of branch coverage.
    * It does not let including a poor tool in tool comparison affect the comparison of tools with relatively better effectiveness.
  
* (iii4) **Future Work:**
 * Compare the effectiveness of test generation tools in achieving other types of coverage criteria such as data flow coverage and mutation testing.
 * Using branch ranking metric for doing the above.
 * Empirically investigate the effectiveness of the feedback loop formed between evolutionary testing and symbolic execution due to the two types of integration and compare it to the two existing integration types in Evacon.
  
###(v) Suggested Improvements:
* (v1) There could have been more subject programs and third party tools in the experiments to further secure against external validity threat.
* (v2) Mention if there was any consequence of not being able to impose time limit on the JUnit Factory on the overall results.
* (v3) The tables used for comparison could have been replaced by a more insightful visualization.

