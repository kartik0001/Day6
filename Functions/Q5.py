# Q5.

d={}

def fact(n):
    ''' Function to find the Factorial of a number'''

    if n==0:
        return 1
    else:
        return n*fact(n-1)

num=int(input("Enter the number whose factorial to be calculated: "))
factorial=fact(num)
d[num]=factorial
print(d)
