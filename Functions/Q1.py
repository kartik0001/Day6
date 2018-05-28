# Q1.

def Area_of_Sphere(radius):
    '''Function to calculate the Area of a sphere using radius'''
    return ((4/3)*(3.14)*(radius**3))

radius=float(input("Enter the radius of sphere: "))
print("Area of sphere with radius {} = {}".format(radius,Area_of_Sphere(radius)))



