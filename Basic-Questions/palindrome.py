num = int(input("Enter a number: "))
result = 0

while num > 0:
    last_digit = num % 10
    print(last_digit)
    result = result * 10 + last_digit
    num = num//10
    print(num)
    
print(result)