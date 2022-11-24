def to_str(bytes_or_str):
    return (
        bytes_or_str.decode('utf-8')
        if isinstance(bytes_or_str, bytes)
        else bytes_or_str
    )


def to_bytes(bytes_or_str):
    return (
        bytes_or_str.encode('utf-8')
        if isinstance(bytes_or_str, str)
        else bytes_or_str
    )
