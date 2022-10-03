# The main goal of args is to passing many arguments to a function 
# without matter what is the number of parameters
def sum_of(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(sum_of(1 , 2 , 4 , 7 , 30 , 39))