

def is_pld(str1: str, str2: str):
    str1 = str(str1)
    str2 = str(str2)

    if len(str1) != len(str2):
        return False

    str1 = list(str1)
    str1.sort()

    str2 = list(str2)
    str2.sort()

    return str1 == str2

