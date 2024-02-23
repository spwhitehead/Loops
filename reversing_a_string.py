# Write three functions that take a string s and return a reversed copy of it.

#   1- reverse_while: Implements the reversing using a while loop.
#   2- reverse_for: Implements the reversing using a for loop (iterating over the string using indices (using range)).
#   3- reverse_foreach: Implements the reversing using a foreach loop (iterating over the actual characters in the string, not using range)

s = "hello"

def reverse_while(s):
    new_string = ""
    i = len(s)
    while i > 0:
        new_string += s[i-1]
        i -= 1
    return new_string

def reverse_for(s):
    new_string = ""
    for i in range(len(s) -1, -1, -1):
        new_string += s[i]
    return new_string

def reverse_foreach(s):
    new_string = ""
    for char in s:
        new_string = char + new_string
    return new_string



def main():
    print(reverse_while(s))
    print(reverse_for(s))
    print(reverse_foreach(s))


if __name__ == "__main__":
    main()
