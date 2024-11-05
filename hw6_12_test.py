import hw6_12

def test_hw6_12():
    assert hw6_12.cumsum([1, 2, 3, 4, 5]) == [1, 3, 6, 10, 15]
    assert hw6_12.cumsum([1, 2, 3, 4, 5, 6]) == [1, 3, 6, 10, 15, 21]
    assert hw6_12.cumsum([1, 2, 3, 4, 5, 6, 7]) == [1, 3, 6, 10, 15, 21, 28]
    assert hw6_12.cumsum([2, 4, 6, 8, 10]) == [2, 6, 12, 20, 30]

if __name__ == "__main__":
    test_hw6_12()
    print("hw6_12_test.py is done")