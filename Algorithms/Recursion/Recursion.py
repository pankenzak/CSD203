def sayHello(count):
    print("Hello")
    count += 1
    if count == 5:
        return
    sayHello(count)
    
def factorial(n):
    if n == 1:
        return 1
    result = n * factorial(n-1)
    return result
    
def power(n, p):
    if p < 0:
        result = 1/power(n, -p)
        return result
    if p == 0:
        return 1
    result = n*(power(n, p-1)) 
    return result

def fibonacci(pos):
    if pos < 0:
        return
    if pos == 0:
        return 0
    if pos == 1:
        return 1
    
    result = fibonacci(pos - 1) + fibonacci(pos - 2)
    return result
    
def main():
    print(factorial(5))
    print(power(2,3))
    print(fibonacci(-2))
    
main()