class UserInputError(Exception):
    pass

def validate_book(content):
    if int(content[3]) > 2024:
        raise UserInputError("This year hasn't come yet")
    if int(content[3]) < 0:
        raise UserInputError("You can't input a negative year")

    if not content[0]:
        if not content[4]:
            raise UserInputError("You must provide at least one author or editor")

    for i in range(1, 4):
        if content[i] == "":
            raise UserInputError("You cannot have empty fields")

def validate_article(content):
    if int(content[3]) > 2024:
        raise UserInputError("This year hasn't come yet")
    if int(content[3]) < 0:
        raise UserInputError("You can't input a negative year")

    for i in range(4):
        if content[i] == "":
            raise UserInputError("You cannot have empty fields")

def validate_inproceeding(content):
    if int(content[4]) > 2024:
        raise UserInputError("This year hasn't come yet")
    if int(content[4]) < 0:
        raise UserInputError("You can't input a negative year")

    for i in range(4):
        if content[i] == "":
            raise UserInputError("You cannot have empty fields")

def validate_update(reference):
    if int(reference[3]) > 2024:
        raise UserInputError("This year hasn't come yet")
    if int(reference[3]) < 0:
        raise UserInputError("You can't input a negative year")

    if not reference[0]:
        raise UserInputError("You must provide at least one author")

    for i in range(1, 4):
        if reference[i] == "":
            raise UserInputError("You cannot have empty fields")
