###Hyper Parameter Optimization for DTLZ for 3 objectives

The report is divided in three sections:
  I. Frontier visualization for DTLZ 1,3, 5, 7 for 3 objective 10 decisions.
  II. Divergence of the final frontier from the frontier formed by baseline population for DTLZ 1, 3 , 5 and 7 for 2, 4, 6, 8 objectives and 10, 20, 40 decisions, using default parameters for GA.
  III. Hypervolume calculation for the final frontiers for DTLZ 1, 3 , 5 and 7 for 2, 4, 6, 8 objectives and 10, 20, 40 decisions, using default parameters for GA.
  
**I. Frontier visualization for DTLZ 1,3, 5, 7 for 3 objective 10 decisions.**
The following figures show the change in the frontier formed by DTLZ 1, 3, 5, and 7. For each of the DTLZs the first figure shows the baseline frontier and the second figure shows the final frontier. The parameters finally used were decided after running the GA with different configuration, and observing the results keeping in mind the feasibility of the runs. The parameters used were -
1. Number of Generations = 500
2. Number of Candidates = 100
3. Number of Decisions = 10
4. Number of objectives = 3

**DTLZ 1 - _Baseline Era_**
![DTLZ1 Era0](https://cloud.githubusercontent.com/assets/7557398/11612920/8ff35c08-9bdb-11e5-8cf1-93882a67f9d9.png)

**DTLZ 1 - _Final Era_**
![DTLZ1 Eraf](https://cloud.githubusercontent.com/assets/7557398/11612925/9008310a-9bdb-11e5-9969-826b12de8dea.png)

**DTLZ 3 - _Baseline Era_**
![DTLZ3 Era0](https://cloud.githubusercontent.com/assets/7557398/11612919/8ff20088-9bdb-11e5-9efb-6ba07593337c.png)

**DTLZ 3 - _Final Era_**
![DTLZ3 Eraf](https://cloud.githubusercontent.com/assets/7557398/11612921/8ff79fb6-9bdb-11e5-8c69-833b18f40060.png)

**DTLZ 5 - _Baseline Era_**
![DTLZ5 Era0](https://cloud.githubusercontent.com/assets/7557398/11612922/8ff7c55e-9bdb-11e5-83f4-444601268bb0.png)

**DTLZ 5 - _Final Era_**
![DTLZ5 Eraf](https://cloud.githubusercontent.com/assets/7557398/11612923/8ffbdcca-9bdb-11e5-9bdb-b43a4367cf21.png)

**DTLZ 7 - _Baseline Era_**
![DTLZ7 Era0](https://cloud.githubusercontent.com/assets/7557398/11612924/8ffd14e6-9bdb-11e5-8fae-f141f34521c7.png)

**DTLZ 7 - _Final Era_**
![DTLZ7 Eraf](https://cloud.githubusercontent.com/assets/7557398/11612918/8ff0e478-9bdb-11e5-9a9a-6c2b86ff3200.png)

**II. Divergence**
To quantify the change in the frontier from the baseline population, we used the **from Hell** calculation. For each candidate on the final frontier, the nearest candidate on baseline was found using the nearest neighbour algorithm. The euclidean distance used to find the corresponding closest baseline candidate for each final frontier frontier candidate, was then averaged over the entire population and gave us the divergence of the frontier from the baseline, which we have assumed to be the **point of hell* for our final frontier.

![2and4_1](https://cloud.githubusercontent.com/assets/7557398/11613463/80749fa8-9bef-11e5-9c6a-4abebcecae84.png)
![2and4_2](https://cloud.githubusercontent.com/assets/7557398/11613464/85526938-9bef-11e5-9942-c971e3ef71fa.png)
![2and4_3](https://cloud.githubusercontent.com/assets/7557398/11613465/8a2db0de-9bef-11e5-8545-011bcfd0e8e1.png)
![2and4_4](https://cloud.githubusercontent.com/assets/7557398/11613467/8cee0bca-9bef-11e5-929b-f484f280d024.png)

![6and8_1](https://cloud.githubusercontent.com/assets/7557398/11613481/14553354-9bf0-11e5-960b-64aaa69ee85f.png)
![6and8_2](https://cloud.githubusercontent.com/assets/7557398/11613480/1454acea-9bf0-11e5-8633-8584d62c9a60.png)
![6and8_3](https://cloud.githubusercontent.com/assets/7557398/11613478/1453c0c8-9bf0-11e5-8272-487709f94611.png)
![6and8_4](https://cloud.githubusercontent.com/assets/7557398/11613479/1453ba9c-9bf0-11e5-9121-bdeb115cf583.png)

**III. Hypervolume calculation**
![Hypervolume](https://cloud.githubusercontent.com/assets/7557398/11613520/e42962d4-9bf1-11e5-827d-38cf49876b0a.JPG)
