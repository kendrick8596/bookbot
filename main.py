from stats import get_num_words, get_num_characters, make_sorted_list
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    relative_path = sys.argv[1]
    book_text = get_book_text(relative_path)
    char_counts = get_num_characters(book_text)
    sorted_chars = make_sorted_list(char_counts)
    
    print("=========== BOOKBOT ===========")
    print(f"Analyzing book found at {relative_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_text)} total words")                            # Print the total number of words
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")   
    #print(book_text)                                               # Print the entire book text
    #print(f"Found {get_num_words(book_text)} total words")   
    #print(make_sorted_list(get_num_characters(book_text)))
main()