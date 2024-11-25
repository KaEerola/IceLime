class UserInputError(Exception):
    pass

def validate_book(content):
    if int(content[3]) > 2024:
          raise UserInputError("This year hasn't come yet")
    
    for i in range(4):
        if content[i] == "":
            raise UserInputError("You cannot have empty fields")
    
    
