import numpy as np

def FizzBuzz(start, finish):

    nums = np.arange(start, finish + 1, dtype=object)

    values = nums.astype(int)

    fizz = values % 3 == 0
    buzz = values % 5 == 0

    nums[fizz] = "fizz"
    nums[buzz] = "buzz"
    nums[fizz & buzz] = "fizzbuzz"

    return nums
