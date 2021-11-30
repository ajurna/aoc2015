def rule_1(password):
    index = 0
    while index < len(password) - 3:
        if password[index+1] - password[index] == 1 and password[index+2] - password[index+1] == 1:
            return True
        index += 1
    return False


def rule_2(password):
    i = ord('i')
    o = ord('o')
    l = ord('l')
    return not any([i in password, o in password, l in password])


def rule_3(password):
    index = 0
    first_match = False
    while index < len(password) - 1:
        if password[index] == password[index+1]:
            if first_match:
                return True
            else:
                first_match = True
                index += 2
        else:
            index += 1
    return False


def increment_password(password, index=None):
    a = ord('a')
    z = ord('z')
    i = ord('i')
    o = ord('o')
    l = ord('l')
    if not index:
        index = len(password)-1
    password[index] += 1
    if index < len(password)-1:
        for x in range(index+1, len(password)):
            password[x] = a
    if password[index] > z:
        return increment_password(password, index-1)
    if not rule_2(password):
        return increment_password(password, index=min([password.index(x) for x in [i, o, l] if x in password]))

    return password


def find_next_password(password):
    while not all([rule_1(password), rule_2(password), rule_3(password)]):
        password = increment_password(password)
    return password


if __name__ == "__main__":
    pw1 = 'cqjxjnds'
    pw = list(map(ord, pw1))

    new_password = find_next_password(pw)
    print("Part 1:", ''.join([chr(x) for x in new_password]))

    new_password = increment_password(new_password)
    new_password = find_next_password(new_password)
    print("Part 2:", ''.join([chr(x) for x in new_password]))
