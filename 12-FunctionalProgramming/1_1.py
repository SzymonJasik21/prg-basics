###
# Calculates arithmetic mean of two integer numbers
#
def mean(x,y):
   arithmetic_mean = (x+y)/2
   return arithmetic_mean

# takes two numbers from keyboard
n1 = int(input("Enter the first integer: "))
n2 = int(input("Enter the second integer: "))

# calculates arightmtic mean and print result
result = mean(n1,n2)
print(f'The arithmetic mean of the numbers {n1} and {n2} is {result}')