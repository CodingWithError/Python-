import sys
import math
class SimpleCalculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    def factorial(self, n):
        return math.factorial(n)
    def power(self,a,b):
        return a**b


if __name__ == "__main__":
    calcu=SimpleCalculator()
    print("Choose operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Factorial")
    print("6. Power")
    x=int(input())
    if x<1 and x>5:
      print("Invalid input")
      sys.exit()
    ans=0
    if x in [1,2,3,4,6]:
      print("Answer type Integer or Float?")
      s=input().strip()
      if s not in ['Integer','Float']:
        print("Invalid input")
        sys.exit()
      a=float(input("Enter first number: "))
      b=float(input("Enter second number: "))
      if x==1:
        ans=calcu.add(a,b)
      elif x==2:
        ans=calcu.subtract(a,b)
      elif x==3:
        ans=calcu.multiply(a,b)
      elif x==4:
        ans=calcu.divide(a,b)
      elif x==6:
        ans=calcu.power(a,b)
      if s=='Integer':
        print("The result is:", int(ans))
      else:
        print("The result is:", float(ans))
    elif x==5:
      a=int(input("Enter a number: "))
      ans=calcu.factorial(a)
      print("The result is:", int(ans))
    else:
      print("Not today")
      sys.exit()

    
   