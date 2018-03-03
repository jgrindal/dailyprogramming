from itertools import permutations
from time import time

DIGITS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def parse_problem(problem):
    words = problem.split(' + ')
    result = words[-1].split(' == ')[1]
    words[-1] = words[-1].split(' == ')[0]
    alphabet = sorted(list(set(''.join(words) + result)))
    word_summary = {i: 0 for i in range(len(alphabet))}
    for i, word in enumerate(words):
        words[i] = [alphabet.index(letter) for letter in word]
        for tens, letter in enumerate(reversed(words[i])):
            word_summary[letter] += 10 ** tens
    result = [alphabet.index(letter) for letter in result]
    result_summary = {i: 0 for i in range(len(alphabet))}
    for tens, letter in enumerate(reversed(result)):
        result_summary[letter] += 10 ** tens
    return (words, result, alphabet, word_summary, result_summary)


def solve(problem):
    words, result, alphabet, word_summary, result_summary = parse_problem(problem)
    nonzero = [word[0] for word in words + [result] if len(word) > 1]
    i = 0
    for p in permutations(DIGITS, len(alphabet)):
        i += 1
        for z in nonzero:
            if p[z] == 0:
                break
        target = sum([p[d] * result_summary[d] for d in range(len(p))])
        word_sum = sum([p[d] * word_summary[d] for d in range(len(p))])
        # print(target, word_sum)
        if target == word_sum:
            print('\ndone.')
            return {alphabet[i]: p[i] for i in range(len(alphabet))}
        if i % 1000 == 0:
            print('.', end='')


PROBLEM = "THIS + IS + HIS == CLAIM"

start = time()
solution = solve(PROBLEM)
print(time() - start)
if solution:
    for key in solution:
        print(f"{key}: {solution[key]}")
else:
    print('no solution found')
