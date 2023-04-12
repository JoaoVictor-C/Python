print('===== DESAFIO 63 =====')
n = int(input('Digite quantos valores você deseja ver da sequência de fibonacci:  '))
p = 0
fib1 = 0
fib2 = 1
while p <= n-1:
   if p == 0:
      print(0)
   p += 1
   res = fib1 + fib2
   print(res)
   fib2 = 
   fib1 = res - fib2

# 0 +  0    = 0
# 1º   2º   = 1       
# 0 +  1    = 1        
# 1 +  1    = 2       
# 2 +  1    = 3        
# 3 +  2    = 5        
# 5 +  3    = 8        
# 5 +  8    = 13       
# 13 + 8    = 21       
# 21 + 13   = 34      
# 34 + 21   = 55