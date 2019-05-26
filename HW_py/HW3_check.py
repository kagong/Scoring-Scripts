#!/usr/bin/python3
start = 1
end = 5
flag = False
students = ""
while True:
    try:
        s = input()
        students += s+" "
    except EOFError:
        break

list_sol = []
for testcase in range(start,end+1):
    solution = open("../files/solutions/HW3/2/"+str(testcase),"r")
    for line in solution.readlines():
        list_sol.append(line.split('\n')[0]);
    solution.close()

for student_id in students.split(' '):
    if student_id == '':
        break
    print(student_id + " start")
    for testcase in range(end):
        flag = False


        print("\t"+str(testcase+1) + ":",end = ' ')

        try:
            result = open("../files/results/HW3/"+student_id+"/2/"+str(testcase+1),"r")
            for line in result.readlines():
                if list_sol[testcase] in line:
                    flag = True
                    break;
            if flag is True:
                print("succes!")
            else:
                print("fail!")
            result.close()
        except Exception as err:
            print(err)
