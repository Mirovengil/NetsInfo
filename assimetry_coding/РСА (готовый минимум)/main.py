from func import *
a = Object()
b = Object()

#Общение напрямую (без арбитра):
print("WITHOUT ARBITER: ")
msg = str_to_int(input("DATA: "))
print('DIGITAL DATA: ', msg)
print('HASH OF DATA: ', a.__make_hash__(int_to_str(msg)))
hash_ = a.set_signature(int_to_str(msg))
msg = a.code_to(msg, b)
print('CODED DATA: ', msg)
print('SIGNATURE: ', hash_)
print('INVALID DECODED DIGITAL DATA: ', a.decode(msg.copy()))
print('VALID DECODED DIGITAL DATA: ', b.decode(msg.copy()))
print('VALID DECODED DATA: ', int_to_str(b.decode(msg.copy())))
print('INVALID OPENING OF SIGNATURE: ', b.check_that_signature_is_of(hash_, b))
print('VALID OPENING OF SIGNATURE: ', b.check_that_signature_is_of(hash_, a))
print("\n\n")

#Общение через арбитра:
print("WITH ARBITER:")

