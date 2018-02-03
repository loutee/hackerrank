n,x = map(int, raw_input().split())

subject_scores = []
for _ in xrange(x):
    subject_scores.append(map(float, raw_input().split()))

for student_scores in zip(*subject_scores):
    print(sum(student_scores) / x)
