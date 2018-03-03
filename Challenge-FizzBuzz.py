for i in range(100):
    to_print = ''
    if i % 3 == 0:
        to_print += 'Fizz'
    if i % 5 == 0:
        to_print += 'Buzz'
    if not to_print:
        to_print = i
    print(to_print)
