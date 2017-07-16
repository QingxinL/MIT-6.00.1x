import string

print(type(string.ascii_lowercase))


def build_shift_dict(shift):
    map_cipher = {}
    # string.ascii_lowercase
    # string.ascii_uppercase
    # the key is the origin letter
    # the value is the letter after
    letters = string.ascii_uppercase + string.ascii_lowercase
    for char in letters:
        map_cipher[char] = ''
    for key, value in map_cipher.items():
        pos = letters.find(key)
        after = pos + shift

        if after > 25:
            after -= 26
        if key in string.ascii_uppercase:
            map_cipher[key] = letters[after]
        if key in string.ascii_lowercase:
            map_cipher[key] = letters[after].lower()
    return map_cipher

print(build_shift_dict(5))
print(build_shift_dict(0))

