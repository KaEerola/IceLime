class UserInputError(Exception):
    pass

def validate_book(content):
    if int(content[4]) > 2024:
        raise UserInputError("This year hasn't come yet")
    if int(content[4]) < 0:
        raise UserInputError("You can't input a negative year")

    for i in range(4):
        if content[i] == "":
            raise UserInputError("You cannot have empty fields")
