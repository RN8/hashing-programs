# WAP in python to generate hashes of sring data using 3 algorith from hashlib.
import hashlib
mystring = input('Enter string: ')
hash_of_md5_obj = hashlib.md5(mystring.encode())
print(hash_of_md5_obj.hexdigest())
hash_of_SHA1_obj= hashlib.sha1(mystring.encode())
print(hash_of_SHA1_obj.hexdigest())
hash_of_sha256_obj= hashlib.sha256(mystring.encode())
print(hash_of_sha256_obj.hexdigest())