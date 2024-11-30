from entities.book import Book

from export import Bibtex


kirja = Book("13","1324","123","123","123","123","123","123","123","123","123")

kirja2 = Book("11","1324","123","123","123","123","123","123","123","123","123")

bibtex = Bibtex()
bibtex.create_book_bibtex([kirja])

bibtex.create_book_bibtex([kirja2])

txt = '''@book{book13,
    author = {1324},
    title = {123},
    year = {123},
    publisher = {123},
    editor = {123},
    volume = {123},
    number = {123},
    pages = {123},
    month = {123},
    note = {123}
}


@book{book11,
    author = {1324},
    title = {123},
    year = {123},
    publisher = {123},
    editor = {123},
    volume = {123},
    number = {123},
    pages = {123},
    month = {123},
    note = {123}
}


'''

with open("src/bibtex.bib","r",encoding= 'utf-8') as file:

    text = file.read()

print(txt == text)

# for i in range(14):
#     print(text[i] + " " + txt[i]+ "\n")
#     print(text[i] == txt[i])

    
#print(text, txt)
#print(len(txt))
