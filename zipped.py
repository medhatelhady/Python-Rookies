
# Enter your code here. Read input from STDIN. Print output to STDOUT

nstudents, nsubject = tuple(map(int, input().strip().split()))

matrix = [list(map(float, input().split())) for i in range(nsubject)]

for i in range(nstudents):
  print(sum([row[i] for row in matrix])/ nsubject)
