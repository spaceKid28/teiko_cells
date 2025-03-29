README.md

Name: Bennett Lincoln
Project: Teiko Cells

RUNNING THE PROJECT LOCALLY: 

This project must be run locally. After the repo has been cloned, using your package manager of choice, please install the required libraries listed in environment.yml. Below is some sample code that I would use, 

    python -m venv teikoENV
    source teikoENV/bin/activate
    pip install -r requirements.txt


SOLUTIONS:
Python

1. Assuming the user is at the top most directory (same level as data folder), Run "python python_problems/runner.py" from the command line. 
This will create the solution as a csv file in this location "solutions/python_1.csv". 
Lines 12 - 14 in runner.py create the solution to problem 1. The associated methods can be found in the src/helper.py

2. The command "python python_problems/runner.py" will also generate the solutions to Question Python 2. It shouldn't need to be run again, but the user can if they wish. The boxplots can be found in "solutions/problem_2a". The code to generate the solutions can be found in "python_problems/runner.py". The associated methods can be found in the src/helper.py

b. The only significant difference in relative frequency of cells is among CD4 T cells between responders and non-responders, as the aboslute value of the T statistic is large enough and the the P-Value small enough, to be considered significant (3.988 and .0095 respectively). 

The statistics calculated in the perform_statistical_tests() method in helper class and they are shown in "solutions/problem_2b_statistics.csv". 

These numbers should be treated cautiously, after filtering out the requested fields, we are left with only 9 samples to perform the analysis. 

The calculations are repeated here for ease of the user:

              Population  Statistic   P-Value
0      b_cell_percentage   0.373091  0.743937
1  cd8_t_cell_percentage  -0.210352  0.844362
2  cd4_t_cell_percentage   3.987613  0.009513
3     nk_cell_percentage   1.690309  0.135290
4    monocyte_percentage  -1.835565  0.199775

Database:

The solutions to the Database problems can be found in the "solutions" folder. The first question is in the file: database_question_1.md 
The remaining solutions are in the file: database_question_2_3_4_5.md

These files should be opened in preview mode (right click open preview)