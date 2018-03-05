def get_input():
    with open('2018-03-05-input.txt', 'r') as file:
        data = [line.strip() for line in file.readlines()]
        data.pop(0)
    return data


def hamming_distance(string1, string2):
    distance = 0
    for index in range(len(string1)):
        if string1[index] != string2[index]:
            distance += 1
    return distance


def index_of_lowest_distance(list_of_strings):
    distances = []
    for string1 in list_of_strings:
        current_distance = 0
        for string2 in list_of_strings:
            current_distance += hamming_distance(string1, string2)
        distances.append(current_distance)
    return distances.index(min(distances))


problem = get_input()
target_index = index_of_lowest_distance(problem)
print(problem[target_index])