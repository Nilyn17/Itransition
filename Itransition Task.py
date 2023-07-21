"""
Task 1
Implement the function to find the combination of 4 digits in a row which gives the max multiplication. If
object is not a string or there are no combinations found - return nil. If combination is found - return it's
multiplication result.
E.g.
max_multiplication('abc12345def') => 120 # 2*3*4*5
max_multiplication('a1b2c3d4e') => nil
"""

def find_max_product(string):

    if not isinstance(string, str):
        return None
    
    max_product = 0

    for i in range(len(string) - 3):
        product = 1
        for ch in string[i:i+4]:
            if ch.isdigit():
                product *= int(ch)
            else:
                product = 0
                break
        
        if product > max_product:
            max_product = product
    
    if max_product == 0:
        return None
    
    return max_product

print(find_max_product("123456789"))
print(find_max_product("abc12345def"))
print(find_max_product("a1b2c3d4e"))
print(find_max_product("abcdef"))



"""
Task 2
Implement the function to sort array of numbers by amount of '1' in its binary representation. Numbers
with identical amount of '1's should be ordered by decimal representation.
E.g.
# 3 = 11, 7 = 111, 8 = 1000, 9 = 1001
sort([3,7,8,9]) => [8,3,9,7] # 1000, 11, 1001, 111
"""

def binary_sort(array):
    
    def count(number):
        return bin(number).count('1')
    
    def key(number):
        return (count(number), number)
    
    sorted_array = sorted(array, key=key)
    
    return sorted_array


print(binary_sort([3,7,8,9]))
print(binary_sort([1,2,3,4]))
print(binary_sort([90, 24, 1, 5]))