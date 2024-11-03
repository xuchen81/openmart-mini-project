def read_file(file_path):
    """Reads the content of a file and returns it."""
    with open(file_path, 'r') as file:
        content = file.read()
    return content


def write_to_file(file_path, content):
    """Writes the given content to a file."""
    with open(file_path, 'w') as file:
        file.write(content)


def int_to_base62(num):
    base62_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    if num == 0:
        return base62_chars[0]

    base62 = []
    while num > 0:
        num, rem = divmod(num, 62)
        base62.append(base62_chars[rem])

    return ''.join(reversed(base62))
