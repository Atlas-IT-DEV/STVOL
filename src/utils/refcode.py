import bcrypt


def hashinf(info: int or str) -> str:
    """
    Function for hash information.

    :param info: info which will hash. [int or str]

    :return: string.
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(f"{info}".encode('utf-8'), salt)
    return hashed.decode('utf-8')


def check_refcode(info: int or str, hashed: str) -> bool:
    """
    Function for validate hashing indormation.

    :param info: Info. [int or str]

    :param hashed: Info which was hashing. [str]

    :return: bool.
    """
    return bcrypt.checkpw(f"{info}".encode('utf-8'), hashed.encode('utf-8'))
