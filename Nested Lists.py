

if __name__ == '__main__':
    score_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        score_list.append([name, score])
    sorted_score_list = sorted(score_list, key = lambda x: x[1])

    i = 1
    while sorted_score_list[i][1] == sorted_score_list[i-1][1]:
      i += 1


    my_list = [sorted_score_list[i][0]]


    while i < len(sorted_score_list)-1 and sorted_score_list[i][1] == sorted_score_list[i + 1][1]:
      i += 1
      my_list.append(sorted_score_list[i][0])
    print('\n'.join(sorted(my_list)))
        

    
    
