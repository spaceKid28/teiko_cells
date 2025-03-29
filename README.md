README.md

Name: Bennett Lincoln
Project: RAG Agent SEC Filings

RUNNING THE PROJECT LOCALLY: 

This project must be run locally. After the repo has been cloned, using your package manager of choice, please install the required libraries listed in environment.yml. Below is some sample code that I would use, using Conda as a package manager:

    conda env create -f environment.yml
    conda activate teikoENV

Note that I have named this environment teikoENV in the requirements.yml file

SOLUTIONS:
Python

1.
Run "python python_problems/runner.py". This will create the solution as a csv file in this location "solutions/python_1.cvs

2. Run all the cells in problem_2.ipynb

b. The only significant difference in relative frequency of cells is among CD4 T cells between responders and non-responders, as the aboslute value of the T statistic is large enough the the P-Value small enough, to be considered significant (3.988 and .0095 respectively). 

The statistics calculated in the "" method in helper class and they are shown in "solutions/problem_2b_statistics.csv". 

These numbers should be treated cautiously, after filtering out the requested fields, we are left with only 9 samples to perform the analysis. 

The calculations are repeated here:

              Population  Statistic   P-Value
0      b_cell_percentage   0.373091  0.743937
1  cd8_t_cell_percentage  -0.210352  0.844362
2  cd4_t_cell_percentage   3.987613  0.009513
3     nk_cell_percentage   1.690309  0.135290
4    monocyte_percentage  -1.835565  0.199775