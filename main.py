def main():
    book_name = "The Frankenstein"
    book_path = "books/frankenstein.txt"
    file_contents = read_book(book_path)
    # print(file_contents)           # Chapter 8
    word_count_result = word_count(file_contents)
    # print(f"{book_name} contains {word_count_result} words") # Chapter 9
    char_count_result = char_count(file_contents)
    print(char_count_result)

def read_book(book_path):
    with open(book_path) as f:
        return f.read()

def word_count(file_contents):
    count = file_contents.split()
    return len(count)

def char_count(file_contents):
    file_contents = file_contents.lower()
    char_count = {}

    for char in file_contents:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    return char_count


main()