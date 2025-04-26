def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def num_words_in_book(file_contents: str) -> int:
    list_words = file_contents.split()
    return len(list_words)

def character_count(file_contents: str) -> dict:
    count_dict ={}
    lowered_contents = file_contents.lower()

    for char in lowered_contents:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    return count_dict

def sort_on(dict):
    return dict["num"]

def sort_dict(count_dict: dict):
    dict_list = []
    for key, value in count_dict.items():
        if key.isalpha():
            dict_list.append({"char": key, "num": value})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def print_report(dict_list, file_path, file_contents):

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words_in_book(file_contents)} total words")
    print("--------- Character Count -------")
    for item in dict_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
