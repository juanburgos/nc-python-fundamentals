"""
Here's my example on using negative indices on lists. 
It's a simple count down using what I have learned so far.
"""

import time


def count_down():
    count = ["Blast off!", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    while len(count) != 0:
        print(count[-1])
        count.pop()
        time.sleep(1)


count_down()
