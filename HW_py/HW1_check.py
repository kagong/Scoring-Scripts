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
    solution = open("../files/solutions/HW1/1/"+str(testcase),"r")
    list_sol.append({})
    for line in solution.readlines():
        line = line.split('\n')[0]
        list_sol[testcase-1][line] = 0
    solution.close()


for student_id in students.split(' '): 
    print(student_id + " start")
    for testcase in range(start,end+1):
        flag = False

        for key in list_sol[testcase-1].keys():
            list_sol[testcase-1][key] = 0

        print("\t"+str(testcase) + ":",end = ' ')

        try:
            result = open("../files/results/HW1/"+student_id+"/1/"+str(testcase),"r")
            for line in result.readlines():
                line = line.split('\n')[0]
                if line in list_sol[testcase-1].keys():
                    list_sol[testcase-1][line] += 1
                else:
                    raise ValueError("invalid output")
                    
    
            for key in list_sol[testcase-1].keys():
                if (not flag) and (list_sol[testcase-1][key] is not 1):
                    raise ValueError("Duplication or Missing")
            print("succes!")
            result.close()
        except Exception as err:
            print(err)
