int_num = 50
float_num = 7.5
# print(int_num + float_num)
str_val = "abc"
# print(int_num * str_val)


print(float_num.__mul__(str_val))
# # notimplemented
print(str_val.__rmul__(float_num))