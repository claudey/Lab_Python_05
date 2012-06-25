# Factorial
n = int(raw_input("Please enter a number: "))
def factorial(n):
    fac = 1
    while n > 0:
        fac *= n
        n -= 1
    return fac
print factorial(n)
        
#Fibonacci
n = int(raw_input("Please enter the nth Fibonacci series you want: "))
def fibonacci (n):
    fibo = 1
    count = -1
    x = 1
    print "The first",n,"Fibonacci numbers are"
    while x < n:
        count += 1
        print fibo
#        count = fibo
        fibo += count
        x += 1
    return fibo
print fibonacci (n)

#Prime numbers
n = int(raw_input("Please enter the number: "))
def prime (n):
    prime_count = 0
    divisor_count = 0
    for i in range(1,n+1):
        if n % i == 0:
            divisor_count += 1
    if divisor_count == 2:
        print n, "is a prime number!"
    elif divisor_count > 2:
        print n, "is not a prime number!"
    return n
print prime(n)

# isPalindrome
