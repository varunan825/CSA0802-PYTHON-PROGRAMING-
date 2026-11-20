from io import StringIO

def wrong_method():
    log = StringIO()
    log.write("Book A")
    log.write("Book B")
    log = StringIO()  # Replacing the buffer discards the earlier content.
    log.write("Book C")
    print("Original Output:")
    print(log.getvalue())

def correct_method():
    log = StringIO()
    for books in [["Book A", "Book B"], ["Book C"], ["Book D", "Book E"]]:
        for book in books:
            log.write(book + "\n")
    print("\nCorrected Output:")
    print(log.getvalue())

wrong_method()
correct_method()
