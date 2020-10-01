

ma=[[1,2,3],[4,5,6],[7,8,9]]
n=3
m=3
for k in range(0, m):
    i=k
    j=0
    while(i>=0):
        print(ma[j][i], end=' ')
        i-=1
        j+=1
for k in range(1, n):
    i=m-1
    j=k
    while(j<=n-1):
        print(ma[j][i], end=' ')
        i-=1
        j+=1
