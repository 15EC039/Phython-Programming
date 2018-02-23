a = int(input())
b = int(input())

for x in range(a,b+ 1):
   c = len(str(x))
   s= 0
   t =x
   while t > 0:
       d = t % 10
       s += d ** c
       t //= 10
   if x == s:
       print(x)
