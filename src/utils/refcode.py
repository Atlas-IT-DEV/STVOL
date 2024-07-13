import bcrypt


def hash_phone(phone: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(phone.encode('utf-8'), salt)
    return hashed.decode('utf-8')


def check_refcode(phone: str, hashed: str) -> bool:
    return bcrypt.checkpw(phone.encode('utf-8'), hashed.encode('utf-8'))
