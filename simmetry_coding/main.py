from func import *
data = ""
data = input("DATA: ")
key = input("YOUR KEY: ")
key = key_to_int(key)
data = prepare_str(data)
to_code = fill_mass(data)
to_code = mass_to_int(to_code)
print("DATA")
print_mass_in_char(to_code)
print("DATA IN HEX")
print_mass_in_hex(to_code)
to_code = code_mass(to_code)
print("CODED DATA")
print_mass_in_hex(to_code)
to_code = mix_mass(to_code)
print("MIXED DATA")
print_mass_in_hex(to_code)
to_code = xor_mass_with_key(to_code, key)
print("YOUR KEY")
print_key_in_hex(key)
print("XORED DATA")
print_mass_in_hex(to_code)
data = mass_to_str(to_code)
print("CODED DATA:", end = '')
print(data)
