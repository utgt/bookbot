def main():
    book_name = "The Frankenstein"
    book_path = "books/frankenstein.txt"
    file_contents = read_book(book_path)
    #print(file_contents)           # Chapter 8
    word_count_result = word_count(file_contents)
    print(f"{book_name} contains {word_count_result} words")


def read_book(book_path):
    with open(book_path) as f:
        return f.read()

def word_count(file_contents):
    count = file_contents.split()
    return len(count)

main()