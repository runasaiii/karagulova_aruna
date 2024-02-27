def snake_to_camel(snake_str):
    camel_str = snake_str.title().replace("_", "")
    camel_str = camel_str[0].lower() + camel_str[1:]
    return camel_str

snake_case_string = input("some string")
camel_case_string = snake_to_camel(snake_case_string)
print("Snake case string:", snake_case_string)
print("Camel case string:", camel_case_string)
