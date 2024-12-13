from repositories.book_repository import get_book_keys
from repositories.article_repository import get_article_keys
from repositories.inproceeding_repository import get_inproceeding_keys

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
    if int(content[3]) > 2024:
        raise UserInputError("This year hasn't come yet")
    if int(content[3]) < 0:
        raise UserInputError("You can't input a negative year")

    for i in range(4):
        if content[i] == "":
            raise UserInputError("You cannot have empty fields")

def validate_update(reference):
    print(reference)
    if int(reference[3]) > 2024:
        raise UserInputError("This year hasn't come yet")
    if int(reference[3]) < 0:
        raise UserInputError("You can't input a negative year")

    if not reference[0]:
        if not reference[4]:
            raise UserInputError("You must provide at least one author or editor")

    for i in range(1, 4):
        if reference[i] == "":
            raise UserInputError("You cannot have empty fields")

def validate_key(ref_key):
    if not ref_key:
        raise UserInputError("You must choose a key for the reference")

    book_keys = get_book_keys()
    article_keys = get_article_keys()
    inproceeding_keys = get_inproceeding_keys()
    for key in book_keys + article_keys + inproceeding_keys:
        if ref_key == key[0]:
            raise UserInputError("You have already used this key")

def validate_update_key(current_key, new_key):
    if not new_key:
        raise UserInputError("You must have a key for the reference")

    if current_key != new_key:
        book_keys = get_book_keys()
        article_keys = get_article_keys()
        inproceeding_keys = get_inproceeding_keys()
        for key in book_keys + article_keys + inproceeding_keys:
            if new_key == key[0]:
                raise UserInputError("You have already used this key")
