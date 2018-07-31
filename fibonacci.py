def fib (x):
    if x == 0:
        a = []
    elif x == 1:
        a = [1]
    elif x == 2:
        a = [1,1]
    elif x > 2:
        a = [1,1]
        for i in range (1,x-1):
            a.append(a[i-1] + a[i])
            i += 1
    return a
print (fib(int(input(("How many numbers do you want to know from Fibonacci? ")))))
   
    
    


    
    
