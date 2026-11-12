def remove_spaces(raw_string):
    char_list = [char for char in raw_string if char != " "]
    return "".join(char_list)


while True:
    user_input = input("Enter a string to delete spaces: ")
    if user_input:
        raw_string = user_input
        break

new_string = remove_spaces(raw_string)

print(new_string)