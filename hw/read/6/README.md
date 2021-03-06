##Summary

###(i) Reference: Nikolai Tillmann and Jonathan de Halleux, Springer, 2008. [Pex–White Box Test Generation for .NET](http://dl.acm.org/citation.cfm?id=1792798). 

###(ii) Keywords:
* (ii1) **Parametrized Unit Test:** A method that takes parameters, performs a sequence of method calls that exercise the code-undertest, and asserts properties of the code’s expected behavior.

* (ii2) **Dynamic Symbolic Execution:** DSE which is a combination of symbolic and concrete execution uses concrete execution to drive the symbolic exploration of a program, the runtime values produced by symbolic execution are used to simplify path constraints to make them more feasible for constraint solving.

* (ii3) **The Testing Problem:** Given a sequential program (single threaded) P with statements S, compute a set of program
inputs I such that for all reachable statements s in S there exists an input i in I such that P(i) executes s.

* (ii4) **Constraint solver:** A program that computes solutions to logic formulas in a given logic

###(iii) Artifacts:

* (iii1) **Motivation:** .NET uses dynamic class loading, which makes it difficult to determine the statements of a program ahead of time. The worst case way to determine the reachability of all statements is by using incremental analysis of all possible execution paths in a program, but the analysis of all possible execution paths may take infinite amount of time. Since time is limited, the authors sought motivation from this problem, and aimed for an analysis that could produce test inputs for most reachable statements fast. Another problem that motivated the authors to create Pex was that, most static analysis tools produced false positives (because of conservative assumptions) for programs for which statement semantics were not known ahead of time. To eliminate the possibility of false positives, environment interactions were taken into account by Pex.

* (iii4) **Checklist:**
  * _Introduction_ to Pex - How and why Dynamic Symbolic Execution came to be used for Pex.
  * _Pex Implementation_
    * _Instrumentation_ - describing the shadow interpreter used by Pex.
    * _Symbolic Representation of Values and Program State_ - how Pex deals with representation of values and program state.
    * _Symbolic Pointers_ and their respresentation in Pex. 
    * _Search Strategy_ employed by Pex, and the reason why it uses that strategy.
    * _Constraint Solving_ processes used by Pex.
    * _Pex Architecture_ describing the libraries used by Pex.
    * _Limitations_ of Pex by delineating situations where it does not analyze code properly.
  * _Application_ of Pex as Visual Studio add-in. Demonstration of how Pex can analyze unsafe managed .NET code.
  * _Evaluation_ of Pex on a core .NET component that had already been extensively tested over several years.

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


###(v) **Suggested Improvements:**
* (v1) The knowledge about the reachability of the blocks and arcs could have made a stronger case for percent coverage evaluation.
* (v2) Pex was tested on a _core .NET component_, more tests on other components could have given a better overview of the kind of problems Pex is most effective in solving.
* (v3) Other coverage criteria such as function, statement and condition coverage could have also been used for the analysis.

###(vi) **Connection to other papers:**
In _Combining Search-based and Constraint-based Testing_ by Malburg and Fraser, Pex is used as one of the basic DSE tools for comparison of constraint based testing with search based testing. in _Evolutionary Generation of Whole Test Suites_ by Fraser and Arcuri, the idea of targeting a single test goal as by Pex is expanded to incorporate an entire test suite in which
all test cases are considered at the same time. Whereas in _FloPSy_ (Search-Based Floating Point Constraint Solving for Symbolic Execution) by Lakhotia et al. PEX is extended to use a search-based approach to solve floating point constraints.


