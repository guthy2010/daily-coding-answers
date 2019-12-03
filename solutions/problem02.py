"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""
from functools import reduce

#Create a list of products using reduce
def ProductListReturn(num_list) -> list:
    product_list = []
    for index in range(len(num_list)):
        sliced_num_list = num_list[:index] + num_list[index+1:]
        product = reduce(lambda x,y : x*y, sliced_num_list)
        product_list.append(product)

    return product_list

#Create a list of products without reduce
def WithoutReduce(num_list) -> list:
    product_list = []
    for index in range(len(num_list)):
        sliced_num_list = num_list[:index] + num_list[index+1:]
        result = 1
        for num in sliced_num_list:
            result *= num
        product_list.append(result)

    return product_list



num_list = [1, 2, 3, 4, 5]

print(
ProductListReturn(num_list),
WithoutReduce(num_list),
sep='\n'
)