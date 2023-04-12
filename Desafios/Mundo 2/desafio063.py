print('===== DESAFIO 63 =====')
n = int(input('Digite quantos valores você deseja ver da sequência de fibonacci:  '))
p = 0
res1 = 1
res2 = 1
res3 = 2
while p <= n-1:
   if p == 0:
      print(0)
      p += 1
   if p-n < 1:
      print(res1)
      res1 = res2 + res3
      p += 1
   if p-n < 0:
      print(res2)
      res2 = res1 + res3
      p += 1
   if p-n < 0:
      print(res3)
      res3 = res2 + res1
      p += 1
      
# 0 +  0    = 0
# 1 +  0    = 1       
# 0 +  1    = 1        
# 1 +  1    = 2       
# 1 +  2    = 3        
# 2 +  3    = 5        
# 3 +  5    = 8        
# 5 +  8    = 13       
# 8 +  13   = 21       
# 13 + 21   = 34      
# 21 + 34   = 55