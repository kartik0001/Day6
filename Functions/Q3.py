# Q3.


i=1
def multiply(n,i,lst):
    ''' Function to print the multiplication table of 12 '''
    if i==1:
        lst.insert(0,n)
    else:
       lst.insert(0,(n*i))
       multiply(n, i - 1, lst)

lst=[]
multiply(12,10,lst)
for j in lst:
	print(j)


