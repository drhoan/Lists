# Write a function sumUntilEven(lst) that takes a list of integers as a parameter 
# and returns the sum of all the numbers in the list up to the first even number
# but not including the first even number.
# If there are no even numbers in the list, the function should return the sum of all the numbers in the list.
# If the list is empty, the function should return 0.

def sumUntilEven(lst):
    # Replace the pass statement with your code
    pass

if __name__ == "__main__":
    print(sumUntilEven([1, 2, 3, 4, 5]))  # 1
    print(sumUntilEven([2, 4, 6, 8, 10]))  # 0
    print(sumUntilEven([1, 3, 5, 7, 9]))  # 25
    print(sumUntilEven([]))  # 0
    print(sumUntilEven([1, 3, 5, 7, 9, 2]))  # 25
    print(sumUntilEven([1, 3, 5, 7, 9, 2, 4]))  # 25
    print(sumUntilEven([1, 3, 5, 7, 9, 2, 4, 6]))  # 25
