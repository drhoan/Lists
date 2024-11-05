import hw6_9

def test_hw6_9():
    assert hw6_9.sumUntilEven([1, 2, 3, 4, 5])  == 1
    assert hw6_9.sumUntilEven([2, 4, 6, 8, 10])  == 0
    assert hw6_9.sumUntilEven([1, 3, 5, 7, 9])  == 25
    assert hw6_9.sumUntilEven([])  == 0
    assert hw6_9.sumUntilEven([1, 3, 5, 7, 9, 2])  == 25
    assert hw6_9.sumUntilEven([1, 3, 5, 7, 9, 2, 4])  == 25
    assert hw6_9.sumUntilEven([1, 3, 5, 7, 9, 2, 4, 6])  == 25

if __name__ == "__main__":
    test_hw6_9()
    print("hw6_9_test.py is done")