# Q4.

def power(a,b):
    ''' function to calculate power of a raised by b'''
    if b==1:
        return a
    else:
        return a*power(a,b-1)
a=int(input("Enter the value of a in a**b: "))
b=int(input("Enter the value of b in a**b: "))
print(power(a,b))