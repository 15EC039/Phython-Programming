a = int(input())
c = len(str(a))
s= 0
t =a
while t > 0:
  d = t % 10
  s += d ** c
  t //= 10
if a == s:
  print('yes')
