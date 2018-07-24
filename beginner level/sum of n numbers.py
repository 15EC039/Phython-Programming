a = []
num = int(input())
if(num>0):
  for n in range(num):
    numbers = int(input())
    a.append(numbers)
  print(sum(a))
else :
  print('invalid')
