import hw6_11

def test_hw6_11():
    assert hw6_11.nested_sum([[1, 2], [3], [4, 5, 6]]) == 21
    assert hw6_11.nested_sum([[1, 2, 3], [4, 5, 6]]) == 21
    assert hw6_11.nested_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 45
    assert hw6_11.nested_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]) == 78

if __name__ == "__main__":
    test_hw6_11()
    print("hw6_11_test.py is done")