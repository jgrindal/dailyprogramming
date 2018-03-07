def create_list_from_file(filename):
    with open(filename, 'r') as file:
        words = [word.strip('.,!?\"\';').upper() for word in file.read().split()]
    return words


def create_hashtable_from_list(word_list):
    word_hash = {}
    for word in word_list:
        if word not in word_hash:
            word_hash[word] = 1
        else:
            word_hash[word] += 1
    return word_hash


def find_word(filename, word_to_find):
    word_to_find = word_to_find.upper()
    word_list = create_list_from_file(filename)
    word_hash = create_hashtable_from_list(word_list)
    return word_hash[word_to_find]


print(find_word('hamlet.txt', 'give'))

