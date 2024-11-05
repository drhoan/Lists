import hw6_13

def test_hw6_13():
    assert hw6_13.middle([1, 2, 3, 4, 5]) == [2, 3, 4]
    assert hw6_13.middle([1, 2, 3, 4, 5, 6]) == [2, 3, 4, 5]
    assert hw6_13.middle([1, 2, 3, 4, 5, 6, 7]) == [2, 3, 4, 5, 6]

if __name__ == "__main__":
    test_hw6_13()
    print("hw6_13_test.py is done")