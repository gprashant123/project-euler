def coin(L):
    """
    Brute-force method for the coin sums problem
    """
    count=1
    b=c=d=e=f=g=0
    for a in range(0,201):
        print(a)
        b=0
        while a+2*b<=200: 
            c=0
            while a+2*b+5*c<=200:
                d=0
                while  a+2*b+5*c+10*d<=200:
                    e=0
                    while  a+2*b+5*c+10*d+20*e<=200:
                        f=0
                        while a+2*b+5*c+10*d+20*e+50*f<=200:
                            g=0
                            while a+2*b+5*c+10*d+20*e+50*f+100*g<=200:
                                if a+2*b+5*c+10*d+20*e+50*f+100*g==200:
                                    count+=1
                                g+=1
                            f+=1
                        e+=1
                    d+=1
                c+=1
            b+=1

    return count
