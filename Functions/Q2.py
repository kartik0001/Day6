# Q2.

def perfect(number):
    '''Function to determine Perfect Number'''
    sum=0
    for i in range(1,number):
        if number%i==0:
            sum+=i
    if sum==number:
        print(number)
print("Perfect numbers between 1 and 1000 are:")
for i in range(1,1001):
    perfect(i)



