# Write three functions that take two strings, "target" and "c"(which will be a single character).
# The functions will count how many times "c" appears in "target", returning the result.

#	1- char_count_while: implements the character counting using a while loop
#	2- char_count_for: implements the character counting using a for loop (iterating over the string using indices using (range))
#   3- char_count_foreach: implements the character counting using a foreach loop (iterating over each character instead of using range)

target = "webdevelopment"
c = "e"

def char_count_while(target, c):
    i = 0
    count = 0
    while i < len(target):
        if target[i] == c:
            count += 1
        i += 1
    return count

def char_count_for(target, c):
    count = 0
    for i in range(len(target)):
        if target[i] == c:
            count += 1
    return count

def char_count_foreach(target,c):
    count = 0
    for char in target:
        if char == c:
            count += 1
    return count



def main():
    print(char_count_while(target, c))
    print(char_count_for(target, c))
    print(char_count_foreach(target,c))


if __name__ == "__main__":
    main()

