#31. Calculator project. Makes 5 functions that reture an answer value

def add(a, b):
    answer = a+b
    return answer

def substract(a, b):
    answer = a-b
    return answer

def multiply(a, b):
    answer = a*b
    return answer

def divide(a, b):
    answer = a/b
    return answer

def exp(a, b):
    answer = a**b
    return answer

print(add(1, 2))
print(substract(1, 2))
print(multiply(1, 2))
print(divide(1, 2))
print(exp(1, 2))