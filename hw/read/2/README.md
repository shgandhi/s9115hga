##Summary

###(i) Reference: Kobi Inkumsah and Tao Xie, North Carolina State University, ASE-2008. [Improving Structural Testing of Object-Oriented Programs via Integrating Evolutionary Testing and Symbolic Execution](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=4639333). 

###(ii) Keywords:
* (ii1) **Evolutionary Testing:** It tries to improve the effectiveness and efficiency of testing process by transforming testing objectives into search problem, and applying evolutionary computation in order to solve them.

* (ii2) **Symbolic Execution:** The key idea here is to generalize testing by using *unknown* symbolic variables in evaluation. A symbolic executor collects all path conditions (eg. if clauses) and operations on symbolic variables along the path selected by a tester. Then these conditions are fed to a constraint solver to derive all inputs that make the program follow this path, as done in *classic constraint based testing*

* (ii3) **Method Sequence Skeleton:** It is a method sequence whose methods' primitive arguments are not specified.

* (ii4) **Structural Coverage:** It is a testing metric based on the structure of the program, intended to find defects rather than exploring the behaviour of the system. It can be focussed on either exploring the control aspect of the code, or explore the definition/use relationship between data elements.

###(iii) Artifacts:

* (iii1) **Motivation:** To increase the confidence in a unit test of a code under test, it is imperative that the unit has good structural coverage (eg. branch coverage). Despite of many test generation tools having been built over time to ensure good structural coverage, there are still two main challenges when it comes to achieving good branch coverage. First is the requirement of an in-depth knowledge of program structure and semantics to generate tests to cover complex logics in some branches. Second is generating special method sequences out of the huge search space of method sequences, to cover branches that lead receiver objects/ non primitive arguments (in Object Oriented Programming) can reach a desirable state only via special method sequences. Though these two challenges have been met by symbolic execution and evolutionary testing, respectively, no work had been done to combine the two approaches and meet both the challenges simulataneously, this led the authors to propose a framework *Evacon*. 

* (iii2) **Checklist:** The authors followed the following series of steps in the paper.
 * Devise the framework for the integration of two existing testing techniques to address the problems in structural testing of object oriented programs. The authors describe their framework with the following 4 components -
    * *Evolutionary testing:* Do population initialization, fitness calculation, chromosome selection, recombination and mutation.
    * *Symbolic Execution:* Using jCUTE, do in loop - concrete execution and constraint collection, followed by constraint solving and input generation.
    * *Argument Transformation:* Transform method arguments of method sequences into symbolic arguments.
    * *Chromosome Construction:* Constructs non random chromosomes out of method sequences generated using symbolic execution for evolutionary testing.
 * Show the empirical comparison of the integration with the state of the art respresentative testing tools for test generation techniques such as search-based test generation using genetic algorithms, symbolic execution and random testing.
 * Give a detailed comparison of strengths and weaknesses of different testing tools in terms of achieving high structural coverage.

* (iii3) **Patterns:** 
 * The authors clearly delineated the research questions investigated in the paper, which can be used as benchmark questions for analyzing any test generation tool or framework -
    * *Utility:* How does the proposed tool fare against representative test generation tools.
    * *Demonstrating the need of the solution:* The proposed framework specifically targets branches that required longer method sequences, the authors demonstrated that certain type of branches needed longer method sequences for optimal branch coverage.
    * *Identifying other solutions based on uniqueness of the problem solved:* The authors identified other tools for comparison based on those tools' unique coverage of some branches which couldn't be covered by other tools. This was the basis of shortlisting tools required for achieving optimal branch coverage.
 * The authors carried out comprehensive analysis of the test generation tools that they used for comparison with their propsed Evacon framework. This directs the prospective user to both the (dis)advantages of these tools. 
 * The average branch coverage of the proposed frameworks were found to be lower than the aggregated average of all the other 4 tools combined. This suggested that for some classes, using multiple tools in combination may be more beneficial than using a single tool to achieve optimal coverage.
 * Use of *Branch ranking metric*: Instead of widely used percentages of branch coverage, branch ranking metric is more useful when selecting multiple tools to use in combination among the tools under comparison. It also,
    * Helps in selecting appropriate tools or their combination for *residual* branch coverage,
    * Compares relative strength of each tool in a set of tools in terms of branch coverage.
    * It does not let including a poor tool in tool comparison affect the comparison of tools with relatively better effectiveness.
  
* (iii4) **Future Work:**
 * Compare the effectiveness of test generation tools in achieving other types of coverage criteria such as data flow coverage and mutation testing.
 * Using branch ranking metric for doing the above.
 * Empirically investigate the effectiveness of the feedback loop formed between evolutionary testing and symbolic execution due to the two types of integration and compare it to the two existing integration types in Evacon.
  
###(v) Suggested Improvements:
* (v1) Their could have been more subject programs and third party tools in the experiments to further secure against external validity threat.
* (v2) Mention if there was any consequence of not being able to impose time limit on the JUnit Factory on the overall results.
* (v3) The tables used for comparison could have been replaced by a more insightful visualization.

