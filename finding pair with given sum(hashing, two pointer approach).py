from collections import defaultdict

for _ in range(int(input())):
    d=defaultdict(int)
    n,s1=map(int, input().split())
    l=list(map(int, input().split()))
    for i in l:
        d[i]+=1
    c=0
    for i in l:
        c+=d[s1-i]
        if(i==s1-i):
            c-=1
    print(c//2)

#  two pointer approach
# Approach: Two Different methods have already been discussed here. Here, a method based on sorting will be discussed.

# Sort the array and take two pointers i and j, one pointer pointing to the start of the array i.e. i = 0 and another pointer pointing to the end of the array i.e. j = n – 1.
# If arr[i] + arr[j] is
# Greater than the sum then decrement j.
# Lesser than the sum then increment i.
# Equals to the sum then count such pairs.