def create_list_from_file(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
    return words


def create_hashtable_from_list(word_list):
    word_hash = {}
    for word in word_list:
        if word not in word_hash:
            word_hash[word] = 1
        else:
            word_hash[word] += 1
    return word_hash


word_list = create_list_from_file('hamlet.txt')
word_hash = create_hashtable_from_list(word_list)
print(word_hash)
