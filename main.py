import sys
from stats import get_book_text, print_report, sort_dict, character_count

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    file_contents = get_book_text(file_path)
    count_dict = character_count(file_contents) 
    dict_list = sort_dict(count_dict) 
    print_report(dict_list,file_path,file_contents)

main()
