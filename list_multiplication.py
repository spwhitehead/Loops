# Create three functions that take two lists of numbers of equal size and return a new list with
# the results of multiplying each matching position from the input lists

# 1- list_multiply_while(a: list[int], b: list[int] -> list[int] -- implements multiplication using a while loop
# 2- list_multiply_for(a: list[int], b: list[int] -> list[int] -- implements multiplication using a for loop (and range)
# 3- list_multiply_foreach(a: list[int], b: list[int] -> list[int] -- implements multiplication using a foreach loop (not using range)

a = [2,2,3]
b = [4,4,2]

def list_multiply_while(a,b):
    i = 0
    total = []
    while i <= len(a):
    total [i] = a[i] * b[i]
    return total 

def main():
    list_multiply_while(a,b)

if __name__ == "__main__":
    main()
