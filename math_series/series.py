'''
# fibonacci function
# Create a method that takes an input n
# If n = 1 then return 1
# If n = 0 then return 0
# return recursive function with "n-1" as arg and recursive function with "n-2" as arg
'''
def fibonacci(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fibonacci(n-1) + fibonacci(n-2)

'''
# lucas function
# Create a method that takes an input n
# If n = 1 then return 1
# If n = 0 then return 2
# return recursive function with "n-1" as arg and recursive function with "n-2" as arg
'''

def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas(n-1) + lucas(n-2)

'''
# Sum Series Function
#Create a method that takes in one required argument "n" and two optional "x,y"
# if n = 0
    - return x
# if n = 1
    - return y
# Return recursive function with "n-1",x,y as arguments and recursive function with "n-2",x,y as arguments
'''

def sum_series(n,x=0,y=1):
    if n == 0:
        return x
    if n == 1:
        return y
    return sum_series(n-1,x,y) + sum_series(n-2,x,y)
