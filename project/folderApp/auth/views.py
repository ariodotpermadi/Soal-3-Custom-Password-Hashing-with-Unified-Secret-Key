from django.http import JsonResponse
from folderApp.auth.hashers import CostumPBKDF2PasswordHasher


def validate_password_sso(password, stored_hashes, secret_keys):
    custom_hasher = CostumPBKDF2PasswordHasher()

    for stored_hash, secret_key in zip(stored_hashes, secret_keys):
        try:
            if custom_hasher.verify(password, stored_hash, secret_key):
                return True
        except Exception as e:
            continue

    return False
