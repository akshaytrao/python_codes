def revs(n):
    rev = 0
    while n > 0:
        dig = n%10
        rev = rev*10+dig
        n=n//10
    return rev 


def palin(n):
    res = revs(n)
    if res == n :
       
        return n 
    else :
      
        return 0

def inc(k):
    
    att=0
    s = palin(k)
    if s == 0:
        while att <= 10:
            k = k+1
            ch = palin(k)
            if ch != 0:
                
        
                return k
            att =att+1
           
    else:
      
        return k
       
def dec(d):
    att1 = 0
    s1 = palin(d)
    if s1 == 0 :
        while att1 <= 10:
            d = d-1
            ch1 = palin(d)
            if ch1 !=0:
                return d
            att1 = att1+1
    else :
        return d 

def absval(h):
    if h < 10:
        print( h ,'is the closest palindrome')
    else:
        
        res1 = inc(h)
        res2 = dec(h)
        diff1 = res1 - h
        diff2 = h - res2
        if diff1> diff2:
            print(res2,'is the closest palindrome')
            return (res2)
        else:
            print(res1,'is the closest palindrome')
            return (res1)

num = int(input(' enter the number'))
absval(num)
