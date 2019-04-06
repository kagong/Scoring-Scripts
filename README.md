This is bash script for scoring HomeWork

we assume that DIR HW[homework number] has dirs named student ID that have files named studentsID_[problem number].c

ex) files - students - HW1 - 20151575 - 1 - HW1_20151575_1.c

1. ./make_dir_hw [homework number]
- then it makes dir hw[homework number] in "files/students, files/results/, files/solutions, files/testcases"

2. put the homeworks in [homework folder]

3. ./push_homeworks_to_files [homework folder]
- it push *.c to folder that matches its name

3. put the solution of [homework number] in files/solutions/HW[homework number]/[problem number]

4. put the testcases of [homework number] in files/testcases/HW[homework number]/[problem number]

5. ./scoring_bash [HW#] [problem#] 
- ex) ./scoring_bash HW1 1

5. Check the results
