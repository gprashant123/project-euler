import math

def divide(c,d):
    L=[c]
    flag=0
    vec=""
    while True:
        c*=10
        #print(c)
        if flag==0:
            vec+="0"
        if c//d==0:
            continue
        else:
            def start(c,d,vec):
                a=c//d
                vec+=str(a)
                c=(c%d)*10
                return [c,vec]  
            while c//d!=0:
                [c,vec]=start(c,d,vec)
                if c in L:
                    return L
                flag=1
                L.append(c)
                if (c*10)//d==0:
                    vec+="0"
               
               
max_rep={}
for d in range(2,1000):
    a=math.modf(math.log(d,2))[0]
    b=math.modf(math.log(d,5))[0]
    c=math.modf(math.log(d,10))[0]
    tol=1e-8
    if a>tol and b>tol and c>tol and d%10!=0:
        new_L=divide(1,d)
        max_rep[d]=len(new_L)-1
        
for ele in max_rep:
  if max_rep[ele]==max(max_rep.values()):
      print(ele)
      break
  
            
        
    
    

