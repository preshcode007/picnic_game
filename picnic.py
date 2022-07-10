#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Print items on picnic
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='items we are bringing',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # our prg is not going to run if not supplied with at least 1 argument...
    # the "nargs="+" makes sure of that so there is not need to accomodate...
    # it in the code.
    parser.add_argument('items',
                        metavar='str',
                        type=str,
                        nargs="+",
                        help='Items we re to bring')

    parser.add_argument('-s',
                        '--sorting',
                        help='Whether to get sorted',
                        action='store_true')

    parser.add_argument('-c',
                        '--comma',
                        help='Whether to ignore the Oxford Comma',
                        action='store_true')

    parser.add_argument('-ch', '--character', help='Character to add',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.items
    sorting = args.sorting
    comma = args.comma
    character = args.character

    # it can be a bit time inefficient if we keep calling the len function...
    # on items several times,hence we put it in a variable num_items
    num_items = len(items)

    bringing = ""
    # print(items)
    # print (sorted)

    # the variable "sorted" will be false if the argument is  ...
    # not provided on command line.

    if sorting:
        items.sort()

    if num_items == 1:
        # print(f'You are bringing {items[0]}.')
        bringing = items[0]

    elif num_items == 2:
        # print(f"You are bringing {items[0]} and {items[1]}.")
        # bringing = f'{items[0]} and {items[1]}'
        bringing = " and ".join(items)

    elif comma:
        bringing = ", ".join(items[:-1]) + " and " + items[-1]

    elif character:
        bringing = ":".join(items[0:])

    else:
        # print(f"You are bringing {items[0]}, {items[1]}, and {items[2]}.")
        # it is good practise not to mutate the LIST
        bringing = ", ".join(items[:-1]) + ", and " + items[-1]

    # I noticed that where this particular IF statement is ...
    # placed affects success of my test when placed ...
    # above the other IF statements my test fails but when
    # placed below the other IF statements my test becomes successful....WHY?
    # ANSWER: ELIF statement should be used instead !!!!

    # if comma:
    #     bringing = ", ".join(items[:-1]) + " and " + items[-1]

    print(f"You are bringing {bringing}.")

# --------------------------------------------------


if __name__ == '__main__':
    main()
