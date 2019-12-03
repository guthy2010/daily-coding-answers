"""
Question 1:
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

# Build a set of k - num diffs and check if there is a match in set
def SumFinder(k,num_list):
    sum_finder_set = set()
    for num in num_list:
        if num in sum_finder_set:
            return True
        sum_finder_set.add(k-num)

num_list = [10, 15, 3, 7]
k = 20