# Create three functions that take two lists of numbers of equal size and return a new list with
# the results of multiplying each matching position from the input lists

# 1- list_multiply_while(a: list[int], b: list[int] -> list[int] -- implements multiplication using a while loop
# 2- list_multiply_for(a: list[int], b: list[int] -> list[int] -- implements multiplication using a for loop (and range)
# 3- list_multiply_foreach(a: list[int], b: list[int] -> list[int] -- implements multiplication using a foreach loop (not using range)

a = [2,2,3]
b = [4,4,2]

def list_multiply_while(a,b):
    i = 0
    product = []
    while i < len(a):
        product.append(a[i] * b[i])
        i += 1
    return product 

def list_multiply_for(a,b):
    product = []
    for i in range(len(a)):
        product.append(a[i] * b[i])
    return product

def list_multiply_foreach(a,b):
    product = []
    i = 0
    for num in a:
        product.append(num * b[i])
        i += 1
    return product



def main():

    print(list_multiply_while(a,b))
    print(list_multiply_for(a,b))
    print(list_multiply_foreach(a,b))




if __name__ == "__main__":
    main()
