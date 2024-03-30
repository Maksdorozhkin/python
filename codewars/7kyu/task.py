# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

# Examples:

# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false

# def solution(text, ending):
#     return text.endswith(ending)


# print(solution("sumo", "omo"))


# def solution(string, ending):
#     return ending in string[-len(ending):]

def solution(string, ending):
    # длинна второго значения отнимается от первого
    string1 = len(string) - len(ending)
    string2 = string[string1:]
    if string2 == ending:
        return True
    else:
        return False


print(solution("sumo", "umo"))
