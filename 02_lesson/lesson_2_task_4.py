n = int(input("Введите число:"))
def fizz_buzz(n):
  for i in range(1, n + 1):
   if  i % 3 and i % 5 == 0:
    print(f"FizzBuzz")
   if i % 3 == 0:
       print("Fizz")
   if i % 5 ==0:
       print("Buzz")
fizz_buzz(n)