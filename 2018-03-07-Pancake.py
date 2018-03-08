def get_input():
    input_string = '3 1 2'
    input_list = input_string.split()
    return input_list


def pancake_sort(data):
    count = 0
    for size in range(len(data), 1, -1):
        max_index = max(range(size))
        if max_index+1 != size:
            if max_index != 0:
                data[:max_index + 1] = reversed(data[:max_index + 1])
            data[:size] = reversed(data[:size])
        count += 1
    return count


data = get_input()
print(data)
print(pancake_sort(data))

