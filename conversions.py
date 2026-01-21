# conversion file
import register_store

def dec_to_string(value):

    encoding_type = register_store.get_register_value(65004) # encoding type 0-> ASCII, 1-> UTF-8, 2-> UTF-16, 3-> UTF-32

    match encoding_type:
        case 0:
            return int32_to_ascii_string(value)
        case 1:
            return int32_to_utf8_string(value)
        case 2:
            return int32_to_utf16_string(value)
        case 3:
            return int32_to_utf32_string(value)
        case _: 
            return -1 


def int32_to_ascii_string(value):
    """
    Convert a 32-bit integer to an ASCII string.
    Treats the 32-bit value as 4 bytes (big-endian), decodes as ASCII.
    """
    bytes_data = value.to_bytes(4, 'big')
    try:
        return bytes_data.decode('ascii')
    except (UnicodeDecodeError, ValueError):
        return None


def int32_to_utf8_string(value):
    """
    Convert a 32-bit integer to a UTF-8 string.
    Treats the 32-bit value as 4 bytes (big-endian), decodes as UTF-8.
    """
    bytes_data = value.to_bytes(4, 'big')
    try:
        return bytes_data.decode('utf-8')
    except (UnicodeDecodeError, ValueError):
        return None

def int32_to_utf16_string(value):
    """
    Convert a 32-bit integer to a UTF-16 string.
    Treats the 32-bit value as 4 bytes (big-endian), decodes as UTF-16 big-endian.
    """
    bytes_data = value.to_bytes(4, 'big')
    try:
        return bytes_data.decode('utf-16-be')
    except (UnicodeDecodeError, ValueError):
        return None

def int32_to_utf32_string(value):
    """
    Convert a 32-bit integer to a UTF-32 string.
    Treats the 32-bit value as 4 bytes (big-endian), decodes as UTF-32 big-endian.
    """
    bytes_data = value.to_bytes(4, 'big')
    try:
        return bytes_data.decode('utf-32-be')
    except (UnicodeDecodeError, ValueError):
        return None