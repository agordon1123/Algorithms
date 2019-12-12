#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # largest_num = 0
  cur_smallest = 0
  max_payout = []

  for i in range(0, len(prices) - 1):
    cur_smallest = prices[i]

    for j in range(i + 1, len(prices)):
      max_payout.append(prices[j] - cur_smallest)

  return max(max_payout)



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))