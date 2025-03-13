import hashlib

data = "hello".encode()
hash_object = hashlib.sha256(data)
print("hello")
print(hash_object.hexdigest())
