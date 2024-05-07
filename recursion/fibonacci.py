def fibo(n):
    if n==1:  #base condition 1
        return 0
    if n==2:   #base condition 2
        return 1
    else:      
        ans = fibo(n-1)+ fibo(n-2)  #recursive call
        return ans

print(fibo(8))
    