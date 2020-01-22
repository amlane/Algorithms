#!/usr/bin/python

import argparse

# this solution has a runtime of O(n^2)


def find_max_profit(prices):
    result = float('-inf')
# starting at the end of the list, compare each number
    for i in range(len(prices) - 1, -1, -1):
        for j in range(len(prices) - 1, -1, -1):
            # if i > j, subtract arr[i] - arr[j]
            if i > j:
              # if the value of i > j do this:
                if result < prices[i] - prices[j]:
                    # if the result is greater than the current value of temp var, store the result in a temp var
                    result = prices[i] - prices[j]
              # else if the value of j > i
# once index == 0 return temp var
    return result


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
