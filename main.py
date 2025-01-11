def main():
    book_name = "The Frankenstein"
    book_path = "books/frankenstein.txt"
    file_contents = read_book(book_path)
    word_count_result = word_count(file_contents)
    char_count_result = char_count(file_contents)
    book_report(word_count_result, char_count_result)

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

def book_report(word_count_result, char_count_result):
    print(f"\t\tBegin Report\t\t\n")
    
    print(f"{word_count_result} words found in the document.\n")

    sorted_char_count = sorted(char_count_result.items(), key=lambda x: x[1], reverse=True)

    for char, count in sorted_char_count:
        print(f"Character {char} was found {count} times.")
    
    print("\n\t\tEnd Report\t\t")

main()
