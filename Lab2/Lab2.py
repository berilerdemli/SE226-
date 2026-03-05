n = int(input("Please enter a positive integer greater than 1: "))

steps = 0
print(n, end="")

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    
    print(" ->", n, end="")
    steps += 1

print("Total steps:", steps)



n = int(input("Please enter a number between 10 and 100: "))

while n < 10 or n > 100:
    print("Invalid input.")
    n = int(input("Please enter a number between 10 and 100: "))

fizz = 0
buzz = 0
fizzbuzz = 0

for i in range(1, n + 1):

    if i % 7 == 0:
        print(f"({i} is skipped)")
        continue

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        fizzbuzz += 1
    elif i % 3 == 0:
        print("Fizz")
        fizz += 1
    elif i % 5 == 0:
        print("Buzz")
        buzz += 1
    else:
        print(i)

print("--- Summary ---")
print("Fizz count:", fizz)
print("Buzz count:", buzz)
print("FizzBuzz count:", fizzbuzz)



n = int(input("Please enter a number between 3 and 9: "))

for i in range(1, 2*n):
    k = n - abs(n - i)
    print("*" * k)
