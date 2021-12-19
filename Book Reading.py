def min_day(nday,r_time,arr) :
    total=0
    i=0
    while total<r_time and i<=nday :
        total+=(86400-arr[i])
        i+=1
    return i

n_day,time=map(int,input().split())
array=list(map(int,input().split()))

print(min_day(n_day,time,array))
