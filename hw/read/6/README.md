##Summary

###(i) Reference: Nikolai Tillmann and Jonathan de Halleux, Springer, 2008. [Pex–White Box Test Generation for .NET](http://dl.acm.org/citation.cfm?id=1792798). 

###(ii) Keywords:
* (ii1) **Parametrized Unit Test:** A method that takes parameters, performs a sequence of method calls that exercise the code-undertest, and asserts properties of the code’s expected behavior.

* (ii2) **Dynamic Symbolic Execution:** DSE which is a combination of symbolic and concrete execution uses concrete execution to drive the symbolic exploration of a program, the runtime values produced by symbolic execution are used to simplify path constraints to make them more feasible for constraint solving.

* (ii3) **The Testing Problem:** Given a sequential program (single threaded) P with statements S, compute a set of program
inputs I such that for all reachable statements s in S there exists an input i in I such that P(i) executes s.

* (ii4) **Constraint solver:** A program that computes solutions to logic formulas in a given logic

###(iii) Artifacts:

* (iii1) **Motivation:**  Dynamic Symbolic Execution and Search Based Software Testing are the most effective approaches for automatic generation of test cases. But both these approaches have their own complementary strength and weaknesses. While DSE is better suited to discover the structure of the input to the system under test, SBST provides a natural way to express coverage based test adequacy criteria as a multi–objective problem. The primary motivation was that -
  * While some work had been done to combine the two approaches, nothing had been done to mitigate the problem of tackling floating point computations in DSE, which originate from limitations of most constraint solvers. Since the constraint solvers approximate constraints over floating point numbers as constraints over rational numbers, the solutions valid for rational numbers are not always valid when mapped to floating point numbers because of limited precision of computers. 

Thus, the authors approached this problem by devising a framework that handled constraints over floating point variables and proposing a combination of DSE with SBST to improve code coverage in the presence of floating point computations.

* (iii2) **Related Work:** 
 * Anand, S., Pasareanu, C.S., Visser, W.: [Jpf-se: A symbolic execution extension to java pathfinder](http://cs.stanford.edu/people/saswat/research/SymExTool.pdf). In: Grumberg, O., Huth, M. (eds.) TACAS 2007. LNCS, vol. 4424, pp. 134–138. Springer, Heidelberg (2007)
 * Grieskamp, W., Tillmann, N., Schulte, W.: [XRT - Exploring Runtime for .NET - Architecture and Applications](http://research.microsoft.com/apps/pubs/default.aspx?id=77413). In: SoftMC 2005: Workshop on Software Model Checking, July 2005. Electronic Notes in Theoretical Computer Science (2005)
 * Godefroid, P., Klarlund, N., Sen, K.: [DART: directed automated random testing](http://research.microsoft.com/en-us/um/people/pg/public_psfiles/pldi2005.pdf). SIGPLAN Notices 40(6), 213–223 (2005)
 * Sen, K., Marinov, D., Agha, G.: [Cute: a concolic unit testing engine for c](http://mir.cs.illinois.edu/marinov/publications/SenETAL05CUTE.pdf). In: ESEC/FSE-13: Proceedings of the 10th European software engineering conference held jointly with 13th ACM SIGSOFT international symposium on Foundations of software engineering, pp. 263–272. ACM Press, New York (2005)
 * Sen, K., Agha, G.: [CUTE and jCUTE: Concolic unit testing and explicit path model-checking tools](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.79.2063). In: Ball, T., Jones, R.B. (eds.) CAV 2006. LNCS, vol. 4144, pp. 419–423. Springer, Heidelberg (2006)
 * Cadar, C., Ganesh, V., Pawlowski, P.M., Dill, D.L., Engler, D.R.: [Exe: automatically generating inputs of death](http://web.stanford.edu/~engler/exe-ccs-06.pdf). In: CCS 2006: Proceedings of the 13th ACM conference on Computer and communications security, pp. 322–335. ACM Press, New York (2006)
 * Godefroid, P., Levin, M.Y., Molnar, D.: [Automated whitebox fuzz testing](http://research.microsoft.com/en-us/um/people/pg/public_psfiles/ndss2008.pdf) . Technical Report MSR-TR-2007-58, Microsoft Research, Redmond, WA (May 2007)
 * Pacheco, C., Lahiri, S.K., Ernst, M.D., Ball, T.: [Feedback-directed random test generation](http://people.csail.mit.edu/cpacheco/publications/feedback-random.pdf). In: ICSE 2007, Proceedings of the 29th International Conference on Software Engineering, Minneapolis, MN, USA, May 23–25 (2007)
 * Saff, D., Boshernitsan, M., Ernst, M.D.: [Theories in practice: Easy-to-write specifications that catch bugs](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.118.2538&rep=rep1&type=pdf). Technical Report MIT-CSAIL-TR-2008-002, MIT Computer Science and Artificial Intelligence Laboratory, Cambridge, MA, January 14
(2008)

* (iii3) **Tutorial Material:** 
  * [Getting Started with Pex](http://research.microsoft.com/en-us/projects/pex/getstarted.pdf)
  * [Exploring Code with Microsoft Pex](http://research.microsoft.com/en-us/projects/pex/digger.pdf)
  * [Parameterized Unit Testing with Microsoft Pex](http://research.microsoft.com/en-us/projects/pex/pextutorial.pdf)
  * [The Pex Forum](http://research.microsoft.com/en-us/projects/pex/)
  * [Pex Coding Duel For Fun](http://www.pexforfun.com/)

* (iii4) **New Results:**

###(v) **Suggested Improvements:**
* (v1) The experiments for benchmark functions could have been repeated for variable number of iterations to account for the inherent stochastic behavior of meta-heuristics used in custom solvers.
* (v2) The reason could have been mentioned for choosing those specific benchmark and open source functions, and whether the chosen functions were representative of the maximum possible input domain.
* (v3) Statistical analysis of the results could have been visually represented for open source libraries as well to give more insightful interpretations.

###(vi) **Connection to other papers:**
FloPSy combines SBST and DSE for a particular setting of floating point constraints while the authors for _"Combining Search-based and Constraint-based Testing"_, give a more general approach of combining these two automatic test generation approaches. FloPSy which is a search based extension to Microsoft's DSE tool PEX that relies on the native code to have constraints, and is specifically an extension for DSE. The work in _"Combining Search-based and Constraint-based Testing"_ works along these lines, but focusses on improving both SBST and DSE without any hard requirement for constraints in native code.


