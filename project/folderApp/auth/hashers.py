import hashlib
from django.contrib.auth.hashers import PBKDF2PasswordHasher


class CostumPBKDF2PasswordHasher(PBKDF2PasswordHasher):
    def encode(self, password, salt, secret_key):
        assert password is not None
        assert salt and secret_key
        password = f"{password}{secret_key}"
        hash = hashlib.pbkdf2_hmac(
            self.algorithm.split("_")[-1],
            password.encode(),
            salt.encode(),
            self.iterations
        )

        return f"{salt}${hash.hex()}"

    def verify(self, password, encoded, secret_key):
        salt, hash = encoded.split('$')
        return self.encode(password, salt, secret_key) == encoded
