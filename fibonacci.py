n = 10
f = {}          
f[0] = 0        
f[1] = 1        

i = 2
while i <= n:
    f[i] = f[i-1] + f[i-2]
    i = i + 1

print(f[n])