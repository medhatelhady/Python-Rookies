



if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()


    mean = lambda arr :sum(arr) / len(arr)
    
    print('{:0.2f}'.format(mean(student_marks[query_name])))
