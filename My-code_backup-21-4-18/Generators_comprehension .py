def square_numbers(nums):
    for i in nums:
        yield (i*i)

Number = square_numbers([1,2,3,4,5,6])

print list(Number)




'''
'''
#In Below You will se the concept of list comprehension
'''
S = [3, 4, 8, 0, 5, 7, 6, 2, 1]
M = [x for x in S if x % 2 == 0]    # OutPut:   [4, 8, 0, 6, 2]

print (M)

S = [x**2 for x in range(10)]
V = [2**i for i in range(13)]
print (S)
print (V)
'''