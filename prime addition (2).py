

def prime(n):
    count = 0 
    for i in range(1,n):
        if n % i ==0:
            count = count +1
        
    if count <= 1 :
        
        return n
    else :
        return 0 


n=int(input('enter the no of elements'))
s=0
l=[]
while s < n:
    ip=int(input('enter the numbers'))
    l.append(ip)
    s = s+1
    
print(l)    


p = []
for i in l:
    if prime(i) != 0 :
        p.append(i)

print(p)
print(sum(p))

    
    



    
            




            
            
    

  
