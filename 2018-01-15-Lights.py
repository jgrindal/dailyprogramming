def parse_input_into_2d_list():
    visitors = []
    with open('input.txt', 'r') as file:
        lines = file.readlines()
    for line in lines:
        visitors += [[int(x) for x in line.split()]]
    return visitors


def main():
    visitors = parse_input_into_2d_list()
    total_hours = 0
    number_in_room = 0
    for hour in range(0, 24):
        for visitor in visitors:
            if visitor[0] == hour:
                number_in_room += 1
            if visitor[1] == hour:
                number_in_room -= 1
        if number_in_room > 0:
            total_hours += 1
    print(total_hours)


if __name__ == "__main__":
    main()
