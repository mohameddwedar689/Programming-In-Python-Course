# The main goal of kwargs is to passing many key:values arguments to a function 
# without matter what is the number of parameters
def sum_of(**kwargs):
    sum = 0
    for k , v in kwargs.items():
        sum += v
    return sum

print(sum_of(coffee = 2.99 , cake = 4.99 , juice = 2.99))