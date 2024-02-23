# Write 2 functions that take in a number "n" and sum up all the numbers between 1 -> n.
# 1- summation_while: implements the summation using a while loop
# 2- summation_for: Implements the summation using a for loop

def summation_while(n):
    total = 0
    i = 0
    while i <= n:
        total += i
        i += 1
    return total



def summation_for(n):
    total = 0
    for i in range(n+1):
        total += i
    return total

print(summation_for(5))
print(summation_while(5))
