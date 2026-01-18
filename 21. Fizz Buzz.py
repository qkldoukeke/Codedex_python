# Write code below 💖
for num in range(1,100):
  if num % 3 == 0 and num % 5 != 0:
    print("Fizz")
  elif num % 3 !=0 and num % 5 == 0:
    print("Buzz")
  elif num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
  else:
    print(num)