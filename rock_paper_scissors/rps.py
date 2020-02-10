#!/usr/bin/python

import sys

# Solution is O(n^2) due to list comprehension inside of for loop


def rock_paper_scissors(n):
    choices = [["rock"], ["paper"], ["scissors"]]
    # base case for 0
    if n == 0:
        return [[]]
    if n == 1:
        return choices
    for i in range(1, n):
        # break into 3 separate lists
        # add rock to the beginning of every list in rock_list
        rock_list = [['rock'] + item for item in choices]
    # add paper to the beginning of every list in paper_list
        paper_list = [['paper'] + item for item in choices]
    # add scissors to the beginning of every sub array in scissor_list
        scissor_list = [['scissors'] + item for item in choices]
    # concatenate lists
        choices = rock_list + paper_list + scissor_list
    return choices


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
