a=int(raw_input())
if (a < 0):
  print("error !!! factorial doesn't occur")
else:
 b=1
 for x in range(1, a+1):
  b=b*x
 print b
