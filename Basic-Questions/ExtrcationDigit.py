# num = input("Enter a number: ")

# while num>0:
#     last_digit = num % 10
#     print(last_digit)
#     num = num//10
#     print(num)


# 1️⃣ Extract numbers from a string

# text = input("Enter a characters:")  # or text = jshgf1342rtgf
# numbers = ""

# for ch in text:
#     if ch.isdigit():
#         numbers += ch

# print(numbers)


# 2️⃣ Extract numbers as a list

text = input("Enter a characters:")
numbers =[]

for ch in text:
    if ch.isdigit():
        numbers.append(int(ch))
        
print(numbers)


