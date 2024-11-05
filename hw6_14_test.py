import hw6_14

def test_hw6_14():
    assert hw6_14.is_sorted([1, 2, 3, 4, 5]) == True
    assert hw6_14.is_sorted([1, 2, 3, 5, 4]) == False
    assert hw6_14.is_sorted([1, 2, 3, 4, 5, 6]) == True
    assert hw6_14.is_sorted(['b', 'a']) == False

if __name__ == "__main__":
    test_hw6_14()
    print("hw6_14_test.py is done")