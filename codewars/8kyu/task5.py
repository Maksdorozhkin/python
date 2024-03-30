# Create a function that always returns True/true for every item in a given list.
# However, if an element is the word 'flick',
# switch to always returning the opposite boolean value.
#
# Examples
# ['codewars', 'flick', 'code', 'wars'] ➞ [True, False, False, False]
#
# Notes
# "flick" will always be given in lowercase.
# A list may contain multiple flicks.
# Switch the boolean value on the same element as the flick itself.




def flick_switch(lst):
    result = True
    output = []
    for item in lst:
        if item == 'flick':
            result = not result
        output.append(result)

    return output

lst = ['codewars', 'flick', 'code', 'wars']
print(flick_switch(lst))


