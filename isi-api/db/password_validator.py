import hashlib

def hash(password, password_encoding_salt):
    hashed = hashlib.sha256((password + password_encoding_salt).encode('utf-8')).hexdigest()
    return hashed
