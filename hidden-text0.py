# Text.encryption
Encrypt any text you want
#fuck_you_editor
import hashlib
message = "#text".encode()
print("MD5:", hashlib.md5(message).hexdigest())
print("SHA-256:", hashlib.sha256(message).hexdigest())
print("SHA-512:", hashlib.sha512(message).hexdigest())
                                                                                                
