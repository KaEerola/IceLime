class UserInputError(Exception):
    pass

def validate_book(content):
    if int(content[3]) > 2024:
          raise UserInputError("This year hasn't come yet")
    
    for i in content:
        if i == "":
            raise UserInputError("You cannot have empty fields")
    
    
