from collections import defaultdict

def first_index(ele):
    return ele[0]
for _ in range(int(input())):
    n=int(input())
    l1=list(map(int, input().split()))
    l2=list(map(int, input().split()))
    d1=defaultdict(int)
    d2=defaultdict(int)
    l1.sort()
    l2.sort()
    if(l1==l2):
        print(0)
        continue
    for i in l1:
        d1[i]+=1
    for i in l2:
        if(d1[i]>0):
            d1[i]-=1
            continue
        d2[i]+=1
    ar=[]
    # print(d1, d2)
    flag, flag1=False, False
    for i in d1:
        if(d1[i]%2!=0):
            flag=True
            break
        ar.append((i, d1[i]))
    s1=0
    for i in d2:
        if(d2[i]%2!=0):
            flag1=True
            break
        ar.append((i, d2[i]))
        s1+=d2[i]
    # print(ar)
    ar=sorted(ar, key=first_index)
    # print(ar)

    # ar[i][0]//key
    # ar[i][1]// count
    sum,ans=0,0
    # print(s1, "s1")
    

        
    if(flag or flag1):
        print(-1)
    else:
        for i in range(len(ar)):
            abc=ar[i][0]
            sum+=ar[i][1]
            
            
            if(sum>s1):
                sum-=ar[i][1]
                abc=(s1-sum)
                ans+=ar[i][0]*abc
                break
                
            ans+=ar[i][1]*abc
        
        print(ans//2)

    