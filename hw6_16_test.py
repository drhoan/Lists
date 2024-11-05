import hw6_16

def test_hw6_16():
    assert hw6_16.has_duplicates([1, 2, 3, 4, 5]) == False
    assert hw6_16.has_duplicates([1, 2, 3, 4, 5, 5]) == True
    assert hw6_16.has_duplicates([1, 2, 3, 4, 5, 6]) == False
    assert hw6_16.has_duplicates(['a', 'b', 'c', 'd', 'e']) == False
    assert hw6_16.has_duplicates(['a', 'b', 'c', 'd', 'e', 'e']) == True

if __name__ == "__main__":
    test_hw6_16()
    print("hw6_16_test.py is done")