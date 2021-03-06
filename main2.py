#!/usr/bin/python3
"""
this program is too slow to be practical
"""
import sys

words = list()
with open('words.txt') as fo:
    for line in fo:
        words.append(line.rstrip())


def find_word_match(curr_word):
    match_set = list()
    if len(curr_word) == 1:
        return False
    for i, c in enumerate(curr_word):
        semi_curr_word = curr_word[:i] + curr_word[i+1:]
        for i2, c2 in enumerate(words):
            if c2 == semi_curr_word:
                match_set.append(semi_curr_word)
    return(match_set)


def recursive_word_funnel(curr_word, length):
    best_l = length
    match_set = find_word_match(curr_word)
    if not match_set:
        return length
    else:
        for a_match_word in match_set:
            rec_l = recursive_word_funnel(a_match_word, length+1)
            if rec_l > best_l:
                best_l = rec_l
    return best_l


if __name__ == '__main__':
    sys.stdout.write("\rDoing thing 0")
    sys.stdout.flush()
    for index, w in enumerate(words):
        sys.stdout.write("\rDoing thing " + str(index))
        sys.stdout.flush()
        if len(w) < 10:
            pass
        elif recursive_word_funnel(w, 1) == 10:
            print(words[index], "has a word funnel of 10")
            break
    print("\nENDED")
