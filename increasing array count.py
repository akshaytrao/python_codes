a = [4,1,3,6,5,2,0]
op = 0
n= 0
print(len(a))
while n < len(a):
    
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            op = op+1
            a[i],a[i+1]=a[i+1],a[i]
            

    n = n+1
    

        
print(op)
print(a)

        
        
    
    
