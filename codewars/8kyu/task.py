# Create a function that accepts a string and a single character, and returns an integer of the count of occurrences the 2nd argument is found in the first one.

# If no occurrences can be found, a count of 0 should be returned.

# ("Hello", "o")  ==>  1
# ("Hello", "l")  ==>  2
# ("", "z")       ==>  0

def str_count(strng, letter):
    res = 1
    for i in strng:
        if letter == i:
            res += 1
        else:
            res - 1

    return res - 1


print(str_count(strng="Hello", letter='z'))


# короткое решение
def strCount(string, letter):
    return string.count(letter)
