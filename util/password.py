from passlib.hash import pbkdf2_sha256
import os
from binascii import hexlify

class Password:
    def get_hash(pw):
        return pbkdf2_sha256.hash(pw)

    def validate(pw, hash):
        return pbkdf2_sha256.verify(pw, hash)

    def create_authkey():
        return hexlify(os.urandom(32)).decode()