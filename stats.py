def get_num_words(book_text):
    words = book_text.split()
    return len(words)

def get_num_characters(book_text):
    char_counts = {}
    for char in book_text.lower():
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts
   
def make_sorted_list(char_counts):
    sort_list = [] 
    for key, value in char_counts.items():
        if key.isalpha():
            sort_list.append({"char": key, "num": value})
    def sort_on(item):
        return item["num"]
    
    sort_list.sort(reverse=True, key=sort_on)
    return sort_list