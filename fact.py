num = 5

# Factorial
fact = 1
for i in range(1, num + 1):
    fact = fact * i

print("Factorial =", fact)

# Prime number check
if num <= 1:
    print("Not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")