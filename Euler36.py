def reverse(s):
    """
    Returns the reversed string
    """
    flag=0
    n=len(s)
    for i in range(len(s)):
        if s[i]!=s[n-i-1]:
            flag=1
            return -1
    return 1

def binary(n):
    """
    Returns the binary number of n
    """
    a=str(n)
    bin=""
    while n>=1:
        bin+=str(int(n%2))
        n=n//2
    bin=bin[len(bin)-1:-0:-1]+bin[0]
    for ele in bin:
        if ele!=0:
            index=bin.find(ele)
            break
    return bin

add=0
for i in range(1,1000000):
    a=str(i)
    if reverse(a)==1:
        b=binary(i)
        if reverse(b)==1:
            print(i)
            add+=i
print(add)

