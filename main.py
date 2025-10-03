import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
from stats import get_num_words
from stats import get_num_chars
from stats import get_sorted_chars
def main():
    with open(sys.argv[1]) as f:
        book_len = f.read()
    get_sorted_chars((get_num_chars(book_len)), (get_num_words(book_len)), (sys.argv[1]))
main()