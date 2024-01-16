expression_result: bool = True
false_expression_result: bool = False

# print(expression_result)
print(false_expression_result)

expression_result = 3 >= 1
print(expression_result)

expression_result = 0 >= 1
print(expression_result)


# digit = int(input("input digit: "))
#
# expression_result = digit > 10
# print(expression_result)
#
# if expression_result:
#     print(f"{digit} > 10")
# else:
#     print(f"{digit} < 10")

#
# digit = int(input("input digit: "))
#
# if digit >10:
#     print(f"{digit} > 10")
# elif digit == 10:
#     print(f"{digit} == 10")
# elif digit == 11:
#     print(f"{digit} == 11")
# else:
#     print(f"{digit} < 10")

# user_list = ["user1", "user2"]
#
# if user_list:
#     print("user list not empy")
# else:
#     print("user list is empy")
#


user_list = [1,2,3]
user_dict = {"a":1}
if user_dict or user_list:
    print("user_dict or user_dict not empy")
else:
    print("user_dict and user_list is empy")

user_list: list = [1,2,3]
user_dict: dict = {}

if user_list and not user_dict:
    print("user_list is not empy and user_dict is empy")

a = "maks"

if a is True:
    print("a is true")
else:
    print(f"{a} - {bool(a)}")
