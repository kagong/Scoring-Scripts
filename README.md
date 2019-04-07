## Scoring-Scipts
This is bash script for **Scoring HomeWork**

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

# License

MIT License

Copyright (c) 2019 kagong

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
