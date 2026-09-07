# 3 Sum problem 
# fibonacci series
n = int(input("Enter number of terms: "))
a = 1
b = 1
print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c