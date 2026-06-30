import numpy as np

def FizzBuzz(start, finish):

    nums = np.arange(start, finish, dtype=object)

    fizz = (nums.astype(int) % 3 == 0)
    buzz = (nums.astype(int) % 5 == 0)

    nums[fizz] = "fizz"
    nums[buzz] = "buzz"
    nums[fizz & buzz] = "fizzbuzz"

    return nums
