stored={}
def rec(m,n):
    """
    returns the total number of possible paths in an mxn grid
    """
    try:
        return stored[(m,n)]
    except:
        if m==1 and n==1:
            stored[(m,n)]=2
            return 2
        elif m==1 or n==1:
            if m==1:
                a=rec(1,n-1)+1
                stored[(m,n)]=a
                stored[(n,m)]=a
                return a
            else:
                a=rec(1,m-1)+1
                stored[(m,n)]=a
                stored[(n,m)]=a
                return rec(1,m-1)+1
        else:
            if m==n:
                b=2*rec(m,n-1)
                stored[(m,n)]=b
                return b
            else:
                b=rec(m-1,n)+rec(m,n-1)
                stored[(m,n)]=b
                stored[(n,m)]=b
                return b
