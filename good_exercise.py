for _ in range(int(input())):
    n=int(input())
    l1=list(map(int, input().split()))
    l2=list(map(int, input().split()))
    l1.sort()
    l2.sort()
    c=1
    max=1
    i, j=1,0
    while(i<n and j<n):
        if(l1[i]>l2[j]):
            c-=1
            j+=1
        else:
            c+=1
            
            if(max<c):
                max=c
                time=l1[i]
            i+=1
    print(max, time)

        
# ques
# Find the point where maximum intervals overlap
# Consider a big party where a log register for guest’s entry and exit times is maintained. Find the time at which there are maximum guests in the party. Note that entries in register are not in any order.
# Example :

# Input: arrl[] = {1, 2, 9, 5, 5}
#        exit[] = {4, 5, 12, 9, 12}
# First guest in array arrives at 1 and leaves at 4, 
# second guest arrives at 2 and leaves at 5, and so on.

# Output: 5
# There are maximum 3 guests at time 5.  