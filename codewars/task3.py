# The cockroach is one of the fastest insects.
# Write a function which takes its speed in km per hour and returns it in cm per second,
# rounded down to the integer (= floored).
# Note! The input is a Real number (actual type is language dependent) and is >= 0.
# The result should be an Integer.

def cockroach_speed(s):
    sm_sec = (s / 0.036)
    result = sm_sec.__floor__()
    return result


print(cockroach_speed(1.08))


