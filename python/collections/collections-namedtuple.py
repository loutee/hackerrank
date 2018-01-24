
m collections import namedtuple

n = int(raw_input())
values = raw_input().split()

Student = namedtuple("Student", values)

average = 0.0
for i in xrange(n):
    w,x,y,z = raw_input().split()
    average += int(Student(w, x, y, z).MARKS)

print(round(average / n, 2))
