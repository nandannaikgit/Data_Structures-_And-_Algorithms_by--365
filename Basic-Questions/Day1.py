# 1. Check even or odd

# n=int(input("Enter a number: "))
# if n%2==0:
#     print(True)
# else:
#     print(False)
    
# def evenodd():
#     if n%2==0:
#         return True
#     else:
#         return False

# if __name__ == "__main__":   
#     n=int(input("Enter a number: "))
#     if evenodd():
#             print("True")
#     else:
#             print("false")


# 2.Program for multiplication table

# n=int(input("Enter a number: "))
# i=0
# for i in range(1,11):
#     multi=n*i
#     print(f"{n} * {i} = {multi}")
    
def printTable():
    for i in range(1,11):
        multi=n*i
        print(f"{n} * {i} = {multi}")
        
if __name__ == "__main__":
    n=int(input("Enter a number: "))
    printTable()