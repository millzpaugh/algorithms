# Complete the search function so that it implements a binary search, following the pseudo-code below (this pseudo-code was described in the previous article):
# 1. Let min = 0 and max = n-1.
# 2. If max < min, then stop: target is not present in array. Return -1.
# 3. Compute guess as the average of max and min, rounded down (so that it is an integer).
# 4. If array[guess] equals target, then stop. You found it! Return guess.
# 5. If the guess was too low, that is, array[guess] < target, then set min = guess + 1.
# 6. Otherwise, the guess was too high. Set max = guess - 1.
# 7. Go back to step 2.

# Returns either the index of the location in the array,
#   or -1 if the array did not contain the targetValue 
import unittest 

var result = search(primes, 73);
print("Found prime at index " + result);

def search(array, target_value):
  min = 0 
  max = len(array) - 1 
  guesses = []

  while min <= max: 
    guess = min + max / 2 
    if array[guess] == target_value: 
      return "It took" + str(len(guesses)) + "guesses to find the number" + str(array[guess]) 
    elif array[guess] < target_value: 
      min = guess + 1 
    else: 
      max = guess - 1 
  else: 
    return - 1 

class Test(unittest.TestCase): 
  primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 
    41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97] 

  def test_binary_search(self): 
    index_value = search(self.primes, 73)
    self.assertEqual(index_value_of_guess, 20)

    index_value_1 = search(self.primes, 41)
    self.assertEqual(index_value_1, 12)


