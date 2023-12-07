def encode_string(input_string):
    encoded_string = ""
    for char in input_string:
        ascii_code = ord(char)
        encoded_char = chr(ascii_code - 1)
        encoded_string += encoded_char

    return encoded_string
input_str = "Hello, World!"
result = encode_string(input_str)
print(result)
