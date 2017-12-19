students = []
grades = set()
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    students.append([name,score])
    grades.add(score)
students.sort()
grades.discard(min(grades))
minimum = min(grades)
for i in xrange(len(students)):
    if (students[i][1] == minimum):
        print (students[i][0])
