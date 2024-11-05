import hw6_8

def test_hw6_8():
    assert hw6_8.sumNegatives([1, 2, 3, 4, 5]) == 0
    assert hw6_8.sumNegatives([-1, -2, -3, -4, -5]) == -15
    assert hw6_8.sumNegatives([1, -2, 3, -4, 5]) == -6
    assert hw6_8.sumNegatives([1, 2, 3, 4, 5, -6]) == -6
    assert hw6_8.sumNegatives([1, 2, 3, 4, 5, -6, -7]) == -13

if __name__ == "__main__":
    test_hw6_8()
    print("hw6_8_test.py is done")