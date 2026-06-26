def fibonacci(n):
  if n == 0:
    fib = []
  elif n==1:
    fib = [0]
  else:
    fib = [0,1]
  for i in range(2,n): # "2" because we already have 1st two numbers
    new_fib = fib[-1] + fib[-2] #new_fib = last fibonnacci + 2nd last fibonacci
    fib.append(new_fib)
  return fib
print(fibonacci(10))
  
