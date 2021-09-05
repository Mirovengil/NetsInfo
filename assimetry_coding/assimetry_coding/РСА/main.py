from func import *
a = Object()
b = Object()
msg = str_to_int(input("DATA: "))
print(msg)
print(a.code_to(msg, b))
print(b.decode(msg))
msg = int_to_str(msg)
print(msg)
