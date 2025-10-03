def get_num_words(book):
    book_words_list = book.split()
    return(f"Found {len(book_words_list)} total words")
def get_num_chars(book):
    book = book.lower()
    chars = {}
    for letter in book:
        chars[letter] = chars.get(letter, 0) + 1
    return chars
def get_sorted_chars(chars_dict, words, book_name):
    chars_list = []
    for k, v in chars_dict.items():
        if k.isalpha() == False:
            continue
        chars_list.append({"char": k, "num": v})
    chars_list.sort(reverse=
    True, key=get_sorted_num)

    print(f"""
    ============ BOOKBOT ============
    Analyzing book found at {book_name}...
    ----------- Word Count ----------
    {words} 
    --------- Character Count -------""")
    for item in chars_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
def get_sorted_num(dict):
    return dict["num"]
