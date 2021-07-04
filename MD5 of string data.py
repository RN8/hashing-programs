# WAP in python to generate MD5 of sring data.
import hashlib
mystring = input('Enter string: ')
hash_obj = hashlib.md5(mystring.encode())
print(hash_obj.hexdigest())