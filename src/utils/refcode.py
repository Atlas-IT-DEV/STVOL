import bcrypt


def hash_telegram_id(telegram_id: int) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(f"{telegram_id}".encode('utf-8'), salt)
    return hashed.decode('utf-8')


def check_refcode(telegram_id: int, hashed: str) -> bool:
    return bcrypt.checkpw(f"{telegram_id}".encode('utf-8'), hashed.encode('utf-8'))
